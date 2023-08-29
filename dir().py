#capitalize():
text = "hello, world!"
result = text.capitalize()
print (result)

#casefold():
text = 'hello, WORLD!'
result = text.casefold()
print (result)

#center(width[, fillchar]):
text = 'Asombroso'
result = text.center(20, "*")
print (result)

#count(sub[, start[, end]]):
text = 'Asombroso'
result = text.count('o')
print (result)

#encode([encoding[, errors]]):
text = 'Hello, world!'
result = text.encode(encoding='utf-8')
print (result)

#endswith(suffix[, start[, end]]):
text = 'Hola, Mundo!'
result = text.endswith ('o!')
print (result)

#expandtabs([tabsize]):
text = 'Hello\tworld!'
result = text.expandtabs(8)
print (result)
#expandtabs([tabsize]) + replace()
text = 'hello\tworld!'
result = text.expandtabs(4)
result_replace = result.replace('', '*')
print (result_replace)
#expandtabs([tabsize]) + replace()
text = 'hello\tworld!'
result = text.expandtabs(tabsize=4)
result_with_stars = result.replace(' ', '*')
print(result_with_stars)

#find(sub[, start[, end]]):
text = 'Asombroso'
result = text.find('so')
print (result)

#format(*args, **kwargs):
nombre = "Lana"
edade = 38
result = "Mi nombre es {} y tengo {} años.".format(nombre, edade)
print (result)

#format_map(mapping):
data = {'nombre': 'Lana', 'edade': 38}
result = "Mi nombre es {nombre} y tengo {edade} años.".format_map(data)
print (result)

#index(sub[, start[, end]]):
text = 'hello, world!'
result = text.index('w')
print (result)

#isalnum():
text = 'LANA'
result = text.isalnum()
print (result)
#isalpha():
result = text.isalpha()
print (result)
#isascii():
result = text.isascii()
print (result)
#isidentifier():
result = text.isidentifier()
print (result)
#islower():
result = text.islower()
print (result)

#isdecimal():
text = '177674'
result = text.isdecimal()
print (result)
#isdigit():
result = text.isdigit()
print (result)
#isnumeric():
result = text.isnumeric()
print (result)
#isprintable(:)
result = text.isprintable()
print (result)
#isspace():
result = text.isspace()
print (result)

#istitle():
text = 'Americana'
result = text.istitle()
print (result)
#isupper():
result = text.isupper()
print (result)

#join(iterable):
words = ['lovely', 'world']
result = ', '.join(words)
print (result)

#ljust(width[, fillchar]):
result = text.ljust(14, '+')
print (result)
#lower():
result = text.lower()
print (result)

#lstrip([chars]):
text = "    hello Japanese!  "
result = text.lstrip()
print (result)

#maketrans(x[, y[, z]]):
text = "hello Japanese!"
trans_table = str.maketrans('eoa', '304')
result = text.translate(trans_table)
print (result)
#partition(sep):
result = text.partition(" ")
print (result)
#removeprefix(prefix):
result = text.removeprefix('hello ')
print (result)
#removesuffix(suffix):
result = text.removesuffix('Japanese!')
print (result)
#replace(old, new[, count]):
result = text.replace('e', '3')
print (result)
#rfind(sub[, start[, end]]):
result = text.rfind('o')
print (result)
#rindex(sub[, start[, end]]):
result = text.rindex('e')
print (result)
#rjust(width[, fillchar]):
result = text.rjust(25, '>')
print (result)
#rpartition(sep):
result = text.rpartition('.')
print (result)
#rsplit([sep[, maxsplit]]):
result = text.rsplit('-')
print (result)
#rstrip([chars]):
result = text.rsplit(   )
print (result)
#split([sep[, maxsplit]]):
result = text.split(' ')
print (result)
#startswith(prefix[, start[, end]]):
result = text.startswith('Hola')
print (result)

#splitlines([keepends]):
multi_line_text = "Hello 1\nMy 2\nBeautiful 3\nJapan! 4\n"
result = multi_line_text.splitlines()
print (result)

#strip([chars]):
text = "    Me Amor!   "
result = text.strip()
print (result)

#swapcase():
text = "Hello My Beautiful Japan!"
result = text.swapcase()
print (result)

#swapcase():
text = "hELLO mY bEAUTIFUL jAPAN!"
result = text.swapcase()
print (result)

#upper():
text = "Hello My Beautiful Japan!"
result = text.upper()
print (result)

#title():
text = 'te amo lana'
result = text.title()
print (result)
#translate(table):
trans_table = str.maketrans('aa', 'AA')
result = text.translate(trans_table)
print (result)
#zfill(width):
result = text.zfill(50)
print (result)

