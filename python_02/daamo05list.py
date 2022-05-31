
# 列表
# 格式  变量名 = []

alst = []   #定义空列表
blst = ['red',11,10.2,None]

print(alst)
print(blst)

# 循环列表
for x in blst:
    print("列表中的值:",x)

# 列表的方法
clst = ['red','green','blue']

# 在列表末尾添加新元素 list.append(obj)
clst.append('black')
print(clst)

# 在列表末尾追加另一个列表的值 list.extend(sep)
clst.extend(blst)
print(clst)

# 翻转列表中的元素 list.reverse()
clst.reverse()
print(clst)

# 统计元素在列表出现的次数  list.count(obj)
print(clst.count('red'))

# 在列表中查出某个元素的位置 list.index(obj)
print(clst.index('blue'))

# 在列表中向某个位置插入元素 list.insert(index,obj)
clst.insert(1,"hello")
print(clst)

# 列表排序 ：list.sort()  ,里面的元素必须是同类型的
dlst = ['a','cd','dx','bh']
print(dlst)
dlst.sort()
print("排序后的结果:",dlst)


# 打印1-10的所有数
for x in [1,2,3,4,5,6,7,8,9,10]:
    print(x)






