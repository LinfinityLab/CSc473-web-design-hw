import re

dicEngToTut = {'b': 'bub','c': 'coch','d': 'dud','f': 'fuf','g': 'gug','h': 'hash','j': 'jug','k': 'kuck',
'l': 'lul','m': 'mum','n': 'nun','p': 'pup','q': 'quack','r': 'rur','s': 'sus','t': 'tut','v': 'vuv',
'w': 'wack','x': 'xux','y': 'yub','z': 'zug'}

dicTutToEng = {a:b for b, a in dicEngToTut.items()}
dicTutToEng['squa'] = '|'

def exception(func):
	def translate(string):
		for i in string:
			if i == "|":
				raise Exception("Input contains a \"|\"")
		return func(string)
	return translate

@exception
def encode(x):
	List = []
	for char in x.lower():
		if char in dicEngToTut:
			List.append(dicEngToTut[char])
			if len(List) > 1:
				if List[-1] == List[-2]:
					del List[-1]
					del List[-1]
					List.append("squa" + char)
		else:
			List.append(char)
	return ''.join(List)

@exception
def decode(x):
	for char in dicTutToEng:
		x = re.sub(char, dicTutToEng[char], x)
	new_x =''
	i = 0
	for char in x:
		if char == '|' and i == 0:
			i += 1
		elif i == 1:
			new_x += 2 * char
			i = 0
		else:
			new_x += char
	return new_x
	