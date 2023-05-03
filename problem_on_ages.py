given_data = input("find X value of son age enter 1 or find Present Age Difference enter 2  ")

if given_data =="1":
    # Problem(22). Let son's age be X and i.e; mother's age is 2X
    a= int(input("No of years ago : "))
    b = int(input("no of times elder : "))
    x = int((a * (b -1)) / (b-2))
    print(" Son's Age X : " + str(x))

if given_data =="2":
    #Problem(18).
    a = int(input("Numerator1 : "))
    b = int(input("Denominator1 : "))
    c = int(input("After How many Years : "))
    d = int(input("Numerator2 : "))
    e = int(input("Denominator2 : "))
    x = int((c*(d-e)) / ((a*e)-(b*d)))
    y = int((a*x)-(b*x))
    print("Age Difference b/w Present Age : " + str(y))

