from fractions import Fraction
given_data = input("find SonAge(X) enter 1 or find Present Age Difference enter 2 or find Ratio of Ages enter 3 ")

if given_data =="1":
    # Problem(22). Let son's age be X and i.e; mother's age is 2X
    a= int(input("No of years ago : "))
    b = int(input("no of times elder : "))
    x = int((a * (b -1)) / (b-2))
    print(" Son's Age X : " + str(x))

if given_data =="2":
    # Problem(18).
    a = int(input("Numerator1 : "))
    b = int(input("Denominator1 : "))
    c = int(input("After How many Years : "))
    d = int(input("Numerator2 : "))
    e = int(input("Denominator2 : "))
    x = int((c*(d-e)) / ((a*e)-(b*d)))
    y = int((a*x)-(b*x))
    print("Age Difference b/w Present Age : " + str(y))

if given_data =="3":
    # Problem35.
    a = int(input("Numerator : "))
    b = int(input("Denominator : "))
    c = int(input("Product of their Ages : "))
    d = int(input("Year' After ? : "))
    x = (c/(a*b))**0.5
    y = Fraction(((a*x)+d)/((b*x)+d))
    print("Ratios of Ages : " + str(y))
