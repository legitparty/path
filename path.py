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
		self.children = []

	def set_frequency(self, f):
		if self.f is None:
			self.f = float(f)
		elif self.f != f:
			print "frequency mismatch on %i %r != %r" % (self.n, self.f, f)

	def get_interval(self, delta):
		return self.notes[self.n + delta]

	def rel_tune(self, delta, n, d):
		parent = self.get_interval(delta)

		if parent.f is None:
			self.notes.report()
			raise IndexError("reference parent note %i has no frequency" % parent.n)

		f = float(parent.f) * n / d

		if self.parent is not None:
			self.parent = self
			self.f = f
		else:
			self.set_frequency(f)
		

class Notes:
	def __init__(self):
		self.notes = [
			Note(self, n, None, inharmonicity_coefficient_2nd_harmonic)
			for n in range(150)
		]

	def __getitem__(self, n):
		return self.notes[n]

	def report(self):
		total_key = lambda d, k: d.setdefault(k, [0])[0]
		def inc_key(d, k):
			d.setdefault(k, [0])[0] = total_key(d, k) + 1

		interval_just_count = {}
		interval_consonant_count = {}
		interval_dissonant_count = {}
		interval_total = {}

		import math
		for note in self.notes:
			if note.f is not None:
				octave = note.n / 12
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
					interval_note = note.get_interval(delta)
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

				print

		for octave, n, d in sorted(interval_total.keys()):
			total     = total_key(interval_total,           (octave, n, d))
			just      = total_key(interval_just_count,      (octave, n, d))
			consonant = total_key(interval_consonant_count, (octave, n, d))
			dissonant = total_key(interval_dissonant_count, (octave, n, d))
			print "%i %i/%i percent just:      %f" % (octave, n, d, float(just)      * 100 / total)
			print "%i %i/%i percent consonant: %f" % (octave, n, d, float(consonant) * 100 / total)
			print "%i %i/%i percent dissonant: %f" % (octave, n, d, float(dissonant) * 100 / total)
			print "%i %i/%i percent obscured:  %f" % (octave, n, d, float(total - consonant - dissonant) * 100 / total)




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


	

def main():
	anotes = ANotes(False)
	anotes.report()

if __name__ == "__main__":
	main()
