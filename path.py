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




class ANotes(Notes):
	def __init__(self):
		Notes.__init__(self)
		C4 = self[60]
		# anchor C to 256 Hz
		C4.set_frequency(256)

		self.init_leaf(C4)

		#self.report()

		Cs5 = C4.get_interval(25)
		# anchor leaf from octave below
		Cs5.rel_tune(-12, 2, 1)

		self.init_leaf(Cs5)

		B1 = C4.get_interval(-25)
		# anchor leaf from 3 octaves above
		B1.rel_tune(36, 1, 8)

		self.init_leaf(B1)

	def init_leaf(self, note):

		start = note

		for x in range(7):
			print start, note

			note = note.get_interval(7)
			note.rel_tune(-7, 3, 2)
			note = note.get_interval(7)
			note.rel_tune(-7, 3, 2)

			chain_5th_end = note

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

	def report(self):
		import math
		for note in self.notes:
			if note.f is not None:
				ref_f = 256 * 2 ** (float(note.n - 60) / 12) 
				diff_f = ref_f - note.f
				diff_r = ref_f / note.f
				cents = 1200.0 * math.log(diff_r) / math.log(2)
				print "%i: %f, %f, %f, %f" % (note.n, note.f, ref_f, diff_f, cents)
				for delta, n, d in [
					(12, 2, 1),
					(7,  3, 2),
					#(5,  4, 3),
					(4,  5, 4),
				]:
					interval_note = note.get_interval(delta)
					if note.f is not None and interval_note.f is not None:
						interval_diff_f = note.f * n / d - interval_note.f
						interval_diff_r = note.f * n / d / interval_note.f
						cents = 1200.0 * math.log(interval_diff_r) / math.log(2)
						print "\t%i/%i offset: %f, %f" % (n, d, interval_diff_f, cents)


	

def main():
	anotes = ANotes()
	anotes.report()

if __name__ == "__main__":
	main()
