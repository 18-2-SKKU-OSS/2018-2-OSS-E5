"""Collatz sequence.
@author: Pablo Trinidad <github.com/pablotrinidad>
"""

def collatz(n):
	"""Sequence generation."""
	l = []
	while n > 1: #iteration
		l.append(n)	
		if n % 2 == 0: # n is even
