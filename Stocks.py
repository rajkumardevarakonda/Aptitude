



given_data = input("find Loss or gain on amount invested in bank & Stock enter 1 : "
                   "or find  ")

if  given_data == "1":
    ti = float(input("Total Investment : "))
    inrt = float(input("interest on investment by bank : "))
    fv = float(input("Face Value : "))
    invt = float(input("Cost of Each Share : "))
    dvd = float(input("Dividend on Face Value : "))
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
