# {}是映射类型 字典

b = ['1','2','3']
s = ['a','b','c']
print('1: ',s[b.index('3')])
1:  c

 dict1 = {'1':'2', '3':'4', '5':'6'}
##print('1后面是：', dict1['1'])
##1后面是： 2

##fromkeys() 创建并返回一个新的字典
##dict1 = {}
##dict1.fromkeys((1, 2, 3))
##{1: None, 2: None, 3: None}
##dict1.fromkeys((1, 2, 3),'Number')
##{1: 'Number', 2: 'Number', 3: 'Number'}
##dict1.fromkeys((1, 2, 3),('one', 'two', 'three'))
##{1: ('one', 'two', 'three'), 2: ('one', 'two', 'three'), 3: ('one', 'two', 'three')}

##dict1 = dict1.fromkeys(range(5),'niuwa')
##dict1
##{0: 'niuwa', 1: 'niuwa', 2: 'niuwa', 3: 'niuwa', 4: 'niuwa'}
##
##for eachKey in dict1.keys():
##    print(eachKey)
##
##    
##0
##1
##2
##3
##4
##for eachValue in dict1.values():
##    print(eachValue)
##
##    
##niuwa
##niuwa
##niuwa
##niuwa
##niuwa
##for eachItem in dict1.items():
##    print(eachItem)
##
##    
##(0, 'niuwa')
##(1, 'niuwa')
##(2, 'niuwa')
##(3, 'niuwa')
##(4, 'niuwa')
##
##print(dict1[4])
##niuwa
##print(dict1[5])
##Traceback (most recent call last):
##  File "<pyshell#22>", line 1, in <module>
##    print(dict1[5])
##KeyError: 5
##dict1.get(5)
##print(dict1.get(5))
##None
##
##4 in dict1
##True
##5 in dict1
##False

##dict1.clear()
##dict1
##{}

