# 条件表达式
# samll =  x if x < y else y

# 断言
# 程序自动崩溃，检测用
# assert 3 > 4

# range
# range([strat,] stop[, step=1])
# 配合for使用，rang生成从strat到stop的数字序列，不包括stop的数字
# range(5)/range(0,5)/rang(0,5,1)
##list(range(5))
##[0, 1, 2, 3, 4]

# break
##b = 'niubi'
##a = input('shuru:')
##
##while True:
##    if a == b:
##        break
##    a = input('zaicishuru:')
##
##print('tongguo')

# continue
##for i in range(10):
##    if i%2 != 0:
##        print(i)
##        continue
##    i += 2
##    print(i)
# 此算法可做偶数项上的操作 i += 2

member = []
member.append('123') # 自动追加在末尾
member.extend(['456','789','101112']) # 自动追加在末尾
member.insert(0,'012') # 插入到第一个
member
['012', '123', '456', '789', '101112']
# 以上为插入，下面为删除
member.remove('012') # 删除某项
del member[1] # 删除第二个
member.pop() # 空的删除最后一个，返回删除字符
 列表分片
member[1:3] # 1开始位置，3结束位置，不包括3，相当于生成新的列表
member[:] # 拷贝一次列表
# 注意
member1 = member # 前与后有关联，用的实际是同一个列表，新的名字而已
member2 = member[:] # 前与后无关，单独复制出的一个新的列表

list1 = [123,456,['niubi','qiang']] # 列表中有列表
123 in list1 # true
123 not in list1 # false
'niubi' in list1 # false
'niubi' in list1[2] # true
'qiang' in list1[2][1] # true

list2 = [1, 2, 3, 5, 4, 6, 8]
list2.sort() # 列表从小到大排列
list2
[1, 2, 3, 4, 5, 6, 8]
list2.reverse() # 列表顺序倒转
list2
[8, 6, 5, 4, 3, 2, 1]
list2.sort(reverse=True) # 列表从小到大排列再顺序倒转
list2
[8, 6, 5, 4, 3, 2, 1]

tuple1 = (1, 2, 3, 4, 5) # 元组
tuple2 = 1, # 元组
tuple3 = () # 元组
tuple4 = ('123','456','789')
tuple4 = tuple4[:2] + ('678',) + tuple4[2:]
tuple4
('123', '456', '678', '789')
del tupel4
8*(8,)
(8, 8, 8, 8, 8, 8, 8, 8)

