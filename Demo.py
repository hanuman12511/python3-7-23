""" print("hello",end="\t")
print("program")
empid =100
print(empid) """
# add program
""" num1 =6
num2 =4
r=num1+num2
print(r) """
# + - * /(float) //(int) %
# += -= *= /= //= %=

""" num1 =8
num1+=3
print(num1) """

# > < >= <= != == true false
""" num1 =5
num2 =7
print(num1>num2) """

# and or not
#num1 =5
#num2 =7
#print(num1>10 and num2<10)
#print(num1>10 or num2<10)
#print(not(num1>num2))


""" if False:
    print("true")

n =10
if n>=10:
    print("num is 10")
pin = 190
if pin ==100:
    print("login")
else:
    print("not login")
 """
""" 
user =  input("enter username")
if user =="admin":
    password = input("enter password")
    if password =="admin123":
        print("login")
    
    else:
        print("enter right password")
else:
    print("enter right user") """
""" 
user = input ("enter user & email")
if(user == "admin"):
    print("login")
elif user == "admin@gmail.com":
    print("login")
else:
    print("not login") """
    
""" print("1")
print("2")
print("3") """

# loop while
# 1 2 3 4 5
# start i=1   end i<=5
""" 
i=1
T=4
while i<=10:
    print(i*T)
    i+=1



i=1
sum1=0
while i<=10:
    if i%2==0:
        sum1 =sum1+i
    i+=1
print(sum1)

num =int(input("enter number"))

output 246 """


#  i=0, i+=1, i<10
""" for  num in range(1,10,2):
    print(num) """
    
#list  []
data =[1,5,2,6]
      # 0  1 2 3
      #-4 -3-2-1       
#print(data)
""" 
add=0
for data1 in data:
    print(data1)
    add=add+data1
print(add) """

""" print(sum(data))
print(max(data))
print(min(data))
print(len(data)) """

""" data.append(7)
print(data)
data.insert(2,5)
print(data)
data.pop()
print(data) """


user =["user1","user2"]
password =[123,456]
while True:
    username =input("Enter name")
    pos =user.index(username)
    if username in user:
        password1=int(input("Enter password"))
        if password1 == password[pos]:
            print("login")
            break
            
    else :
        print("not login")
