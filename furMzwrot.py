# petla, uzytkownik wpisuje wpisuje, 10s,
# to do tablicy, z tego tuple, pobierz date, zapisz do pliki w dokumentach, samogloska / jesli cyfra to podzielne przez 3

import time

f = open("C:\\Users\\MASTER\\Documents\\furMichal.txt", "w+") #next time


def veryfication(full_list, final_list):

    all_digits = ('1', '2', '3', '4', '5', '6', '7', '8', '9','0')
    all_vowels = ('a', 'o', 'i', 'e', 'u', 'y')
    for sign in full_list:
        if sign in all_vowels:
            final_list.append(sign)
        elif sign in all_digits:
            if int(sign) % 3 == 0:
                final_list.append(sign)

final_list = []
full_list = []

start_time = time.time()

while time.time() - start_time < 10:
    sign = input('Put one sign: ')
    full_list.append(sign)

veryfication(full_list, final_list)

final_tuple = tuple(final_list)

f.write("Elements in Tuple: ")
for element in final_tuple:
    f.write(str(element)+" ")

local_time = time.asctime(time.localtime(time.time()))
f.write("\nLocal time is: " + local_time)

# this program steal user time to check symbols
# move operational part after while() ...
# make this whole program a one big func and run it on down of the file
# like so:
# if __name__ == '__main__':
#    ... place for your func call...
# place this script on github and send me link instead of files

# prog looks good, and does the job
