import random
from string import punctuation


def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)


upperLetter1 = chr(random.randint(65, 90))
upperLetter2 = chr(random.randint(65, 90))

lowerLetter1 = chr(random.randint(97, 122))
lowerLetter2 = chr(random.randint(97, 122))


digit1 = chr(random.randint(48, 57))
digit2 = chr(random.randint(48, 57))


punctuationSign1 = chr(random.randint(33, 47))
punctuationSign2 = chr(random.randint(33, 47))


password = upperLetter1 + upperLetter2 + \
    lowerLetter1 + lowerLetter2+digit1+digit2+punctuationSign1+punctuationSign2
password = shuffle(password)

print(password)
