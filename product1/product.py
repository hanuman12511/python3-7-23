def product(productdata):
    data_num = len(productdata)
    for i in range(data_num):
        for data in productdata[i].values():
            for k in data:
               print(k,end="\t")
            print()
    print(productdata[0]['productname'])
    pname = input("enter product")
    if pname in productdata[0]['productname']:
                print("product found ")
                return "add to cart"
    return "no product found"