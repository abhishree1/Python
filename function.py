def greet(name):
	return f"hey {name}!"

print(greet('abhi'))

def reverse(str):
	return str[::-1]
def uppercase_and_reverse(str):
	str =reverse(str)
	return str.upper()

print(uppercase_and_reverse('abhi'))

