from fractions import Fraction

given_data = input("find Loss or gain on amount invested in bank & Stock enter 1 : "
                   "or find Q.24 enter 2 or find Q.25 enter 3 or find change in Income enter 4 : or "
                   "find change in income on service charge enter 5 ")

if  given_data == "1":
    ti = float(input("Total Investment : "))
    inrt = float(input("interest on investment by bank : "))
    fv = float(input("Face Value : "))
    invt = float(input("Cost of Each Share : "))
    dvd = float(input("Dividend % on Face Value : "))
    x = float((ti*inrt)/100)
    y = float(((dvd * fv) / 100) * (ti / invt))
    print("Bank Income : " + str(x))
    print("Total Income on Stock : " + str(y))
    if x>y:
        D = float(x-y)
        print("LOSS : " + str(D))
    else:
        D = float(y-x)
        print("Gain : " + str(D))

if  given_data == "2":
    a = int(input('total investment = '))
    b = int(input('max percentage on bond b = '))
    x = 100 * a / (b + 100)
    y = a - x
    print((x, y))
    c = int(input('percentage on bond a = '))
    d = int(input('percentage on bond b = '))
    total = (c * x / 100) + (d * y / 100)
    print("Maximum Return : " + str(total))

if  given_data == "3":
    a = Fraction(input('Stock value a = '))
    b = Fraction(input('Dividend % a = '))
    c = Fraction(input('Stock Value b = '))
    d = Fraction(input('Dividend % b = '))
    x = (a / b)
    y = c / d
    z = x / y
    print("Ratios of Investments : "+ str(z))


if  given_data == "4":
    a = float(input("1st Investment : "))
    b = float(input("one Share Value of 1st Investment : "))
    c = float(input("Annual Dividend % on one Share of A : "))
    d = float(input("One Share Value Sold at : "))
    e = float(input("New Stock Value Invested : "))
    f = float(input("Dividend % of One New Stock Value : "))
    x = (c*(a/b))
    y = (f*d*(a/b))/e
    D = (y-x)
    print("change in Income : " + str(D))

if  given_data == "5":
    a = float(input("total Shares sold at : "))
    b = float(input("Dividend % on one Share of  : "))
    c = float(input("one Share Value of 1st Investment : "))
    d = float(input("Dividend % on one New Stock Value: "))
    e = float(input("one Share Value of 2nd Investment: "))
    f = float(input("Service Charges % of Face value: "))
    # face Value = 100
    g = a/100  # no. of shares sold
    h = (c-f)*g
    i = (h)/(e+f) # no. of new shares that invested in
    x = (a * b) / 100
    y = (d*i)
    D = (y-x)
    print("change in Income : " + str(D))
