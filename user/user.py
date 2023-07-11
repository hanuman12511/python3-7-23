def userdata(udata):
   
    userd = udata[0]
    print(userd)
    name =input("enter username")
    if(name in userd['username']):
        print("user found")
        return True
    
    return False