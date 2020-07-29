# petla, uzytkownik wpisuje wpisuje, 10s,
# to do tablicy, z tego tuple, pobierz date, zapisz do pliki w dokumentach, samogloska / jesli cyfra to podzielne przez 3

f = open("C:\\Users\\MASTER\\Documents\\furMichal.txt", "w+")

import time
def makingTuple(finalList, a):
    digits = ('1', '2', '3', '4', '5', '6', '7', '8', '9','0')
    vowels = ('a', 'o', 'i', 'e', 'u', 'y')

    if a in vowels:
        finalList.append(a)
    elif a in digits:
        if int(a) % 3 == 0:
            finalList.append(a)

functionStart = time.time()
finalList = []

while time.time() - functionStart < 10:
    a = input('Put one sign: ')
    makingTuple(finalList, a)

finalTuple = tuple(finalList)

f.write("Elements in Tuple: ")
for i in finalTuple:
    f.write(str(i)+" ")

localTime = time.asctime(time.localtime(time.time()))
f.write("\nLocal time is: " + localTime)

# this program steal user time to check symbols
# move operational part after while() ...
# make this whole program a one big func and run it on down of the file
# like so:
# if __name__ == '__main__':
#    ... place for your func call...
# place this script on github and send me link instead of files

# prog looks good, and does the job
