# list []
listData = ["user","user1","user2"]
f=False
while True:
    username = input("enter name")
    if username in listData:
        print("login")
        f=True
        break
    else:
        print("not login")
product=["product1","product2"]

if f:
    print(product)
else:
    print("not")
    


""" print(listData)
for d in listData:
    print(d)
 """ 
#data =[3,2,5,4,6]
""" add=0
for i in data:
    print(i)
    add+=i
print(add) """
""" print(data)
print(sum(data))
print(max(data))
print(min(data))
print(len(data))
 """
""" num = int(input("Enter number"))

data.append(num)
print(data)
pos=int(input("enter item pos"))
num = int(input("Enter number"))
data.insert(pos,num)
print(data)
data.pop()
print(data) """
""" n=int(input("enter  delete num"))
data.remove(n)
print(data)
 """
