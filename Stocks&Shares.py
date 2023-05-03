given_data = input("find cp enter 1 or find sv enter 2 or find invmt enter 3 ")

if given_data =="1":
    fv = float(input("enter the facevalue : "))
    dis = float(input("enter the discount : "))
    brok= float(input("enter the brokerage : "))
    cp =float(fv - dis + brok )
    print("costprice : " + str(cp))

if given_data =="2":
    sp = float(input("enter the sellingPrice : "))
    brok = float(input("enter the brokerage : "))
    sv = float(sp - brok)
    print("stockvalue : " + str(sv))

if given_data =="3":
    ic1 = float(input("income1 or earn1 :"))
    invt1 = float(input("investment1 or stock1: "))
    ic2 = float(input("income2 or earn2 : "))
    invt2 = float((invt1 / ic1) * ic2)
    print("investment2 or stock2 :" + str(invt2))