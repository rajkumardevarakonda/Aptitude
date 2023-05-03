given_data = input("find X value of son age enter 1 ")

if given_data =="1":
    # Problem22.Let son's age be X and i.e; mother's age is 2X
    a= int(input("No of years ago : "))
    b = int(input("no of times elder : "))
    x = int((a * (b -1)) / (b-2))
    print(" Son's Age X : " + str(x))

