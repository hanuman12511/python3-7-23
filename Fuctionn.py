def login(data):
    email =input("enter email")
    if(email in data):
        print("login")

data=["u1@g.c","u2@g.c"]
login(data)
        


#
# default function without return
"""def Add():
    n1=3
    n2=7
    r=n1+n2
    print(r)

Add()
"""
# return
"""

def Add():
    n1=3
    n2=7
    r=n1+n2
    return r
sss =Add()
print(sss)
"""
"""
def Add(n1,n2):
    r=n1+n2
    print(r)

n1=5
n2=2
Add(n1,n2)
"""
""" def Add(n1,n2):
    r=n1+n2
    return r

n1=5
n2=2
r =Add(n1,n2)
print(r) """


