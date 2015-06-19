# Numeric expressions
2015
2000 + 15
1 * 2 * ((3 * 4 * 5 // 6) ** 3) + 7 + 8

# Call expressions
max(2.0, 1.5)
pow(100, 2)
pow(2, 100)
max(1, -2, 3, -4)
max(min(1, -2), min(pow(3, 5), -4))

# Importing and arithmetic with call expressions
from operator import add, mul
add(1, 2)
mul(3, 3)
mul(add(2, mul(4, 6)), add(3, 5))
mul(10, add(mul(add(2, mul(4, 6)), add(3, 5)), -6.5))

from math import sqrt
sqrt(169)

# Objects
# Note: Download from http://composingprograms.com/shakespeare.txt
shakes = open('shakespeare.txt')
text = shakes.read().split()
len(text)
text[:15]
text.count('the')
text.count('thou')
text.count('you')
text.count('forsooth')
text.count(',')

# Sets
words = set(text)
len(words)
max(words)
max(words, key=len)

# Reversals
'draw'[::-1]
{w for w in words if w == w[::-1] and len(w)>4}
{w for w in words if w[::-1] in words and len(w) == 4}
{w for w in words if w[::-1] in words and len(w) > 6}
