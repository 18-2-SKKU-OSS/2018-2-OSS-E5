"""A Ducci sequence is a sequence of n-tuples of integers, sometimes known as "the Diffy game", because it is based on sequences."""


"""From the second n-tuple onwards, it is clear that every integer in each n-tuple in a Ducci sequence is greater than or equal to 0 and is less than or equal to the difference between the maximum and minimum members of the first n-tuple. As there are only a finite number of possible n-tuples with these constraints, the sequence of n-tuples must sooner or later repeat itself. Every Ducci sequence therefore eventually becomes periodic."""
def ducci_sequence(*ns):
	    while True:
	    	yield ns
	    	ns = tuple(abs(ns[i - 1] - ns[i]) for i in range(len(ns)))
		
def ducci(*ns):
	known = set()
	for ns in ducci_sequence(*ns):
		print(ns)
		if ns in known or set(ns) == {0}:
			break
			
		known.add(ns)
	return len(known) + 1

print(str(ducci(0, 653, 1854, 4063)) + " steps")
