# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "
we=(word[1:3])
s=(word[7])
ee=(word[2:4])
t=(word[0])
r=(word[6])
happy=(we + " " + s + ee + " " + t + r + ee + s)
print(happy)