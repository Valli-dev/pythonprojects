l=[2]
m=[]
m=sorted(l+m)
print(m)
length=len(m)
print(len(m))
if len(m)%2 == 0:
    mid= len(m)//2
    print(m[mid])
    mid2=mid-1
    print(m[mid2])
    
    median=(m[mid]+m[mid2])/2
    print("median= ", median)
if len(m)==1:
    print("median = ", m[0])
   
else:
    mid=(len(m)+1) //2
    print("mid", mid)
    print("median= " , m[mid]/2)
   
#print(l*5)
#add= l+5
#print(add)

class Solution:
    def reverse(self, x: int) -> int:
        flag=0
        if x<0:
            x=abs(x)
            flag=1
        s=x%10
        x=x-s
        t=(x%100)//10
        h=x//100
        if flag== 1:
            return -(s*100+t*10+h)
        else:
            return (s*100+t*10+h)    
        
s = Solution()
print(s.reverse(500))