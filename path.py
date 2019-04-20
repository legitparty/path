# inharmonicity model
# http://daffy.uah.edu/piano/page4/page8/index.html

stretch_interval = ((1.5 ** 12) / (2.0 ** 7)) ** (1.0/7)
stretch_interval
1.0019377369015756

inharmonicity_coefficient_ratio = lambda harmonic, coeff: harmonic * (1.0 + 0.5 * (harmonic ** 2 - 1) * coeff)

stretch_coeff_2 = lambda stretch_interval: (stretch_interval - 1) / 1.5
inharmonicity_coefficient_2nd_harmonic = stretch_coeff_2(stretch_interval)
0.0012918246010504102
inharmonicity_coefficient_ratio(2, stretch_coeff_2(stretch_interval)) / 2
1.0019377369015756

stretch_coeff_3 = lambda stretch_interval: (stretch_interval - 1) / 4
inharmonicity_coefficient_3rd_harmonic = stretch_coeff_3(stretch_interval)
0.0004844342253939038
inharmonicity_coefficient_ratio(3, stretch_coeff_3(stretch_interval)) / 3
1.0019377369015756

pyth_n = lambda v, o: 7 * v - 12 * o
pyth_r = lambda v, o, stretch_interval: (1.5 ** v) / (2.0 * stretch_interval) ** o
pyth   = lambda v, o, stretch_interval: (pyth_n(v, o), pyth_r(v, o, stretch_interval))




class Note:
	def __init__(self, notes, midi_n, note_frequency = None, inharmonicity_coeff = 0.0):
		self.notes = notes
		self.n = midi_n
		self.f = float(note_frequency) if note_frequency is not None else None
		self.coeff  = inharmonicity_coeff
		self.octave = inharmonicity_coefficient_ratio(2, self.coeff)
		self.parent = None
		self.children = set()

	def set_frequency(self, f):
		if self.f is None:
			self.f = float(f)
		elif self.f != f:
			print "frequency mismatch on %i %r != %r" % (self.n, self.f, f)

	def get_interval(self, delta):
		return self.notes[self.n + delta]

	def get_interval_path(self, delta):
		return self.notes.get_interval_path(self, self.get_interval(delta))

	def add_child(self, child):
		self.children.add(child)

	def set_parent(self, parent):
		self.parent = parent
		parent.add_child(self)

	def rel_tune(self, delta, n, d):
		parent = self.get_interval(delta)

		if parent.f is None:
			self.notes.report()
			raise IndexError("reference parent note %i has no frequency" % parent.n)

		f = float(parent.f) * n / d

		if self.parent is None:
			self.set_parent(parent)
			self.set_frequency(f)
		else:
			self.notes.report()
			print "parent is already assigned on %i (existing parent is %i, attempting to set %i)" % (self.n, self.parent.n, parent.n)
			raise KeyError

	def seq_tune(self, delta, n, d):
		note = self.get_interval(delta)
		note.rel_tune( - delta, n, d)

		return note
		
	def get_parent(self):
		return self.parent

	def get_ancestry(self):
		# include self in ancestry
		yield self

		node = self
		while True:
			ancestor = node.get_parent()
			if not ancestor:
				break

			yield ancestor

			node = ancestor

class Notes:
	def __init__(self):
		self.notes = [
			Note(self, n, None, inharmonicity_coefficient_2nd_harmonic)
			for n in range(150)
		]

	def __getitem__(self, n):
		return self.notes[n]

	def get_interval_path(self, noteA, noteB):
		from collections import deque
		noteA_ancestry = deque(noteA.get_ancestry())
		noteB_ancestry = deque(noteB.get_ancestry())
		#print "noteA %r noteB %r" % (noteA_ancestry, noteB_ancestry)
		while True:
			if len(noteA_ancestry) > 0 and len(noteB_ancestry) > 0 and noteA_ancestry[-1] is noteB_ancestry[-1]:
				# remove oldest common ancestor
				noteA_ancestry.pop()
				noteB_ancestry.pop()
			else:
				# all common ancestors removed
				break

		#print "common removed noteA %r noteB %r" % (noteA_ancestry, noteB_ancestry)
		# traverse down the noteA_ancestry, toward noteB
		for note in noteA_ancestry:
			yield note

		# traverse up the noteB_ancestry, toward noteB
		for note in reversed(noteB_ancestry):
			yield note

	def report(self):
		total_key = lambda d, k: d.setdefault(k, [0])[0]
		def inc_key(d, k):
			d.setdefault(k, [0])[0] = total_key(d, k) + 1

		interval_just_count = {}
		interval_consonant_count = {}
		interval_dissonant_count = {}
		interval_path_count = {}
		interval_total = {}

		import math
		for note in self.notes:
			if note.f is not None:
				octave = note.n / 12 - 1 # MIDI octave to piano octave
				ref_f = self.notes[60].f * 2 ** (float(note.n - 60) / 12) 
				diff_f = ref_f - note.f
				diff_r = ref_f / note.f
				cents = 1200.0 * math.log(diff_r) / math.log(2)
				print "%i: %f, %f, %f, %f" % (note.n, note.f, ref_f, diff_f, cents)
				for delta, n, d, c in [
					(12, 2,  1,  "c"),
					(7,  3,  2,  "c"),
					(5,  4,  3,  "d"),
					(4,  5,  4,  "c"),
					(3,  6,  5,  "d"),
					(2,  9,  8,  "c"),
					(1,  17, 16, "c"),
				]:
					try:
						interval_note = note.get_interval(delta)
					except IndexError:
						continue

					if note.f is not None and interval_note.f is not None:
						interval_diff_f = note.f * n / d - interval_note.f
						interval_diff_r = note.f * n / d / interval_note.f
						cents = 1200.0 * math.log(interval_diff_r) / math.log(2)
						print "\t%i/%i[%s] offset: %f, %f" % (n, d, c, interval_diff_f, cents)
						inc_key(interval_total, (octave, n, d))

						if interval_diff_f == 0.0:
							inc_key(interval_just_count, (octave, n, d))

						if abs(interval_diff_f) < 0.5:
							inc_key(interval_consonant_count, (octave, n, d))

						if abs(interval_diff_f) > 2.0 and abs(interval_diff_f) < 20.0:
							inc_key(interval_dissonant_count, (octave, n, d))

						print "path for %i" % note.n
						for ancestor in note.get_interval_path(delta):
							print "\t%i" % ancestor.n

						for ancestor in note.get_interval_path(delta):
							inc_key(interval_path_count, (octave, n, d))

				print

		for octave, n, d in sorted(interval_total.keys()):
			total     = total_key(interval_total,           (octave, n, d))
			just      = total_key(interval_just_count,      (octave, n, d))
			consonant = total_key(interval_consonant_count, (octave, n, d))
			dissonant = total_key(interval_dissonant_count, (octave, n, d))
			path      = total_key(interval_path_count,      (octave, n, d))
			print "%i %i/%i percent just:      %f" % (octave, n, d, float(just)      * 100 / total)
			print "%i %i/%i percent consonant: %f" % (octave, n, d, float(consonant) * 100 / total)
			print "%i %i/%i percent dissonant: %f" % (octave, n, d, float(dissonant) * 100 / total)
			print "%i %i/%i percent obscured:  %f" % (octave, n, d, float(total - consonant - dissonant) * 100 / total)
			print "%i %i/%i average path:      %f" % (octave, n, d, float(path) / total)
			print




class ANotes(Notes):
	def __init__(self, use_4ths = True):
		Notes.__init__(self)
		C4 = self[60]
		# anchor C to 256 Hz
		C4.set_frequency(256)

		self.init_leaf(C4, use_4ths)

		up1 = C4.get_interval(25 if use_4ths else 21)
		# anchor leaf from octave below
		up1.rel_tune(-12, 2, 1)

		self.init_leaf(up1)

		down1 = C4.get_interval(-25 if use_4ths else -21)
		if use_4ths:
			# anchor leaf from 3 octaves above
			down1.rel_tune(36, 1, 8)
		else:
			# anchor leaf from 3 octaves above
			down1.rel_tune(36, 1, 8)

		self.init_leaf(down1)
			

	def init_leaf(self, note, use_4ths = True):

		start = note

		for x in range(7):
			note = note.get_interval(7)
			note.rel_tune(-7, 3, 2)
			note = note.get_interval(7)
			note.rel_tune(-7, 3, 2)

			chain_5th_end = note

			if use_4ths:
				note = note.get_interval(5)
				note.rel_tune(-5, 4, 3)
				note = note.get_interval(5)
				note.rel_tune(-5, 4, 3)

			if x == 1: # second time
				# anchor the next sequence by 5/4 against `start`
				note = start.get_interval(4)
				note.rel_tune(-4, 5, 4)
			else:
				# anchor the next sequence down an octave from `k`
				note = chain_5th_end.get_interval(-12)
				note.rel_tune(12, 1, 2)

class EvenNotes(Notes):
	def __init__(self):
		Notes.__init__(self)

		for note in self.notes:
			note.f = 256.0 * 2.0 ** ((note.n - 60) / 12.0)


class PATHNotes(Notes):
	def __init__(self):
		Notes.__init__(self)

		self.init_leaf3()

		self.init_leaf4()

		self.init_leaf2()

		self.init_leaf5()

		self.init_leaf1()

	def init_leaf1(self):
		A1 = self[60 - 12 - 12 - 3]
		for note in [A1.get_interval(- i) for i in range(13)]:
			note.rel_tune(12, 1, 2)
	
	def init_leaf2(self):
		F3 = self[60 - 7]
		F2 = F3.seq_tune(-12, 1, 2)

		note = F2.seq_tune(-7, 2, 3)    # A#1
		note = F2.seq_tune(7, 3, 2)     # C3
		note = note.seq_tune(-12, 1, 2) # C2
		note = note.seq_tune(7, 3, 2)   # G2
		note = note.seq_tune(7, 3, 2)   # D3

		A3 = self[60 - 3]
		A2 = A3.seq_tune(-12, 1, 2)

		note = A2.seq_tune(-7, 2, 3)    # D2
		note = A2.seq_tune(7, 3, 2)     # E3
		note = note.seq_tune(-12, 1, 2) # E2
		note = note.seq_tune(7, 3, 2)   # B2
		
		Fs3 = self[60 - 6]
		Fs2 = Fs3.seq_tune(-12, 1, 2)

		note = Fs2.seq_tune(-7, 2, 3)   # B1
		note = Fs2.seq_tune(7, 3, 2)    # C#3
		note = note.seq_tune(-12, 1, 2) # C#2
		note = note.seq_tune(7, 3, 2)   # G#2
		note = note.seq_tune(7, 3, 2)   # D#3
		
		As3 = self[60 - 2]
		As2 = As3.seq_tune(-12, 1, 2)

		note = As2.seq_tune(-7, 2, 3)   # D#2
		

	def init_leaf3(self):
		C4 = self[60]
		# anchor C to 256 Hz
		C4.set_frequency(256)

		note = C4.seq_tune(-7, 2, 3)    # F3
		note = C4.seq_tune(7, 3, 2)     # G4
		note = note.seq_tune(-12, 1, 2) # G3
		note = note.seq_tune(7, 3, 2)   # D4
		note = note.seq_tune(7, 3, 2)   # A4
		note = note.seq_tune(-12, 1, 2) # A3
		# use 5/4 from C4, rather than pure pythagorean via 5ths, to roll back a syntonic comma across the circle. (80/64 instead of 81/64)
		note = C4.seq_tune(4, 5, 4)     # E4
		note = note.seq_tune(7, 3, 2)   # B4
		note = note.seq_tune(-12, 1, 2) # B3
		note = note.seq_tune(7, 3, 2)   # F#4
		note = note.seq_tune(-12, 1, 2) # F#3
		note = note.seq_tune(7, 3, 2)   # C#4
		note = note.seq_tune(7, 3, 2)   # G#4
		note = note.seq_tune(-12, 1, 2) # G#3
		note = note.seq_tune(7, 3, 2)   # D#4
		note = note.seq_tune(7, 3, 2)   # A#4
		note = note.seq_tune(-12, 1, 2) # A#3
		note = note.seq_tune(7, 3, 2)   # F4

	def init_leaf4(self):
		G4 = self[60 + 7]
		G5 = G4.seq_tune(12, 2, 1)

		note = G5.seq_tune(-7, 2, 3)    # C5
		note = G5.seq_tune(7, 3, 2)     # D6
		note = note.seq_tune(-12, 1, 2) # D5
		note = note.seq_tune(7, 3, 2)   # A5
		note = note.seq_tune(7, 3, 2)   # E6

		E4 = self[60 + 4]
		E5 = E4.seq_tune(12, 2, 1)

		note = E5.seq_tune(7, 3, 2)     # B5
		note = note.seq_tune(7, 3, 2)   # F#6
		note = note.seq_tune(-12, 1, 2) # F#5
		note = note.seq_tune(7, 3, 2)   # C#6

		Cs4 = self[60 + 1]
		Cs5 = Cs4.seq_tune(12, 2, 1)

		note = Cs5.seq_tune(7, 3, 2)    # G#5
		note = note.seq_tune(7, 3, 2)   # D#6
		note = note.seq_tune(-12, 1, 2) # D#5
		note = note.seq_tune(7, 3, 2)   # A#5
		note = note.seq_tune(7, 3, 2)   # F6

		F4 = self[60 + 5]
		F5 = F4.seq_tune(12, 2, 1)

		note = F5.seq_tune(7, 3, 2)   # C6	

	def init_leaf5(self):
		D6 = self[60 + 12 + 12 + 2]
		D7 = D6.seq_tune(12, 2, 1)

		note = D7.seq_tune(-7, 2, 3)    # G6
		note = D7.seq_tune(7, 3, 2)     # A7
		note = note.seq_tune(-12, 1, 2) # A6
		note = note.seq_tune(7, 3, 2)   # E7
		note = note.seq_tune(7, 3, 2)   # B7

		B5 = self[60 + 12 + 11]
		B6 = B5.seq_tune(12, 2, 1)

		note = B6.seq_tune(7, 3, 2)     # F#7
		# C#8 does not exist
		note = note.seq_tune(-5, 3, 4)  # C#7 (down a 4th, rather than up a 5th and down an 8th)
		note = note.seq_tune(7, 3, 2)   # G#7

		Gs5 = self[60 + 12 + 8]
		Gs6 = Gs5.seq_tune(12, 2, 1)

		note = Gs6.seq_tune(7, 3, 2)    # D#7
		note = note.seq_tune(7, 3, 2)   # A#7
		note = note.seq_tune(-12, 1, 2) # A#6
		note = note.seq_tune(7, 3, 2)   # F7
		note = note.seq_tune(7, 3, 2)   # C8

		C6 = self[60 + 12 + 12]
		C7 = C6.seq_tune(12, 2, 1)

		note = C7.seq_tune(7, 3, 2)     # G7
		

def main():
	#evennotes = EvenNotes()
	#evennotes.report()

	#anotes = ANotes(False)
	#anotes.report()

	pathnotes = PATHNotes()
	pathnotes.report()

if __name__ == "__main__":
	main()
