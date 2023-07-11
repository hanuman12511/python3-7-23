import product1.product as p
import user.user as u
def Login_user(userdata):
    if(u.userdata(userdata['user'])):
        print(p.product(userdata["product"]))



userdata={
    "user":[{"username":["user1","user2"],"password":[1234,5678]}],
    "product":[{"productname":["product1","product2"]},
               {"productrate":[100,200]}],
    "addtocart":[{"addtoproduct":[],"addtoqty":[]}]
    
}


Login_user(userdata)