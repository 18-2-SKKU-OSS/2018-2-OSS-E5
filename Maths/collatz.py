"""Collatz sequence.
@author: Pablo Trinidad <github.com/pablotrinidad>
"""

def collatz(n):
	"""Sequence generation."""
	l = []
	while n > 1: #iteration
		l.append(n)	
		if n % 2 == 0: # n is even
			n = n / 2
		else:
			n = (3 * n) + 1
		
	l.append(n)
	return l

