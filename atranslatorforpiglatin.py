#take the users input
words = raw_input("enter some text to translate to pig latin: ")
print "you entered: ", words

#now i need to break apart the words into a list
words = words.split(' ')

#now words is a list, so i can manipulate each one using a loop

for i in words:
  if len(i) >= 3: #i only want to translate words greater than 3 characters
    i = i + "%say" % (i[0])
    i = i[1:]
    print i
  else:
    pass
