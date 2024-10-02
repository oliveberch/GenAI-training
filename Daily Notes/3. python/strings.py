# word
print('Hello')

# sentences
print("Hello there, how you doing!!")

# paragraph
print("""
      And thus began the war of troy
      And loss of a culture of millenia
      And yes it's funny!!
      """)

print('''
      And thus began the war of troy
      And loss of a culture of millenia
      And yes it's funny!!
      ''')

var = "ikagai is a good book"

print(var[3])

print(len(var))

for ch in var:
    print()

for x in "banana":
  print(x)

print()



#slicing operation

var = "helloworld"
#print(var[1:5])
print(var[-5:])


# Q. 
inp = "hi all good day"
op = "ih lla good yad"

test = inp[::-1]
print(test)

def rev_words(sentence):
    words = sentence.split()
    rev_words = [word[::-1] for word in words]
    rev_str = ' '.join(rev_words)
    return rev_str

sentence = "hi all good day"
print(rev_words(sentence))