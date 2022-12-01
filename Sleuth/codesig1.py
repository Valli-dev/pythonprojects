from sqlite3 import Binary


a=17
b=13
print(a/b)
b_num=bin(a)[2:]
num_len=len(b_num)
print(num_len)
print(not (a==b))
print(a == (not b))
#print(a == not b)
print( not a == b)
xs=[(),3]
print((xs))
res = [False] *2
print(res)
if xs:
    res[0]=True
    print("hi")
if xs[0]:
    res[1]=True
    print("hello")