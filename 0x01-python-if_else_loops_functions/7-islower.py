#!/usr/bin/python3
def slower(c):
	"""Function that checks for lowercase characters."""
	if ord(c) >= 97 and ord(c) <= 122:
		return True
	else:
		return False
