

# f = open('a.txt')   #打开文件
#
# t = f.read()      #读内容
# print(t)
#
# f.close()     #关闭文件

a = open('a.txt','w')
a.write("nice\n")
a.write("god")

a.close()


def add(x,y,*args):
    x = 1
    y = 2
    return x ,y
add(1,2,3)



print(add(1,2,4))
