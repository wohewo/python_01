

# def add(x,y):
#     return x+y
#
# print(add(2,5))

from hanshu import add

print(add(2,3))

from _datetime import datetime
print(datetime.now())

from hanshu import Students2

s = Students2()
print(s.name)
print(s.great)


import os
print(os.listdir())

f = open('a.txt')

while True:
    l = f.readline()     #mreadline ⽅法可以⼀次读取⼀⾏内容

    print(l,end="")
    if not l:
        break

f.close()


