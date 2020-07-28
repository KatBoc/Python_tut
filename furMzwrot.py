#petla, uzytkownik samoglowki wpisuje, 10s,
#to do tablicy, tuple, pobierz date, zapisz do pliki w dokumentach, jesli cyfra to podzielne przez 3

import time; # fixme - NO SEMICOLONS !

listForTuple = [] # fixme name of this variable should tell what it contains
myTuple = () #fixme names

listS=['a', 'o', 'i', 'e', 'u', 'y'] # fixme if this is immutable past the whole program - those lists could be tuples, name!
listI=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] # fixme names!

startF = time.time() #names!

while (time.time() - startF < 10): # no need for parenthesis
    a = input('wpisz jeden znak: ') # Case in Polish grammar - make nice-look messages for user, names
    #if a in listS:s  fixme - what does this s do ? - test your program before sending to examine
    if a in listS:
        listForTuple.append(a)
    elif a in listI:
        if int(a) % 3 == 0:
           listForTuple.append(a)

myTuple = tuple(listForTuple) # FIXME - NAMES !!
print (myTuple) # TODO - did not ask for print

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime) #todo -  did not ask for that

#todo
# this program steal user time to check symbols
# move operational part after while() ...
# make this whole program a one big func and run it on down of the file
# like so:
# if __name__ == '__main__':
#    ... place for your func call...
# place this script on github and send me link instead of files

# prog looks good, and does the job