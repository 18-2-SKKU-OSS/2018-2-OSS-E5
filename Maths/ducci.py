"""A Ducci sequence is a sequence of n-tuples of integers, sometimes known as "the Diffy game", because it is based on sequences."""

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



