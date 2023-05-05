def find_cost_price():
    fv = float(input("Enter the FaceValue : "))
    dis = float(input("Enter the Discount : "))
    brok= float(input("Enter the Brokerage : "))
    cp = float(fv - dis + brok)
    print("costPrice : " + str(cp))


def find_stock_value():
    sp = float(input("Enter the SellingPrice : "))
    brok = float(input("Enter the Brokerage : "))
    sv = float(sp - brok)
    print("stockValue : " + str(sv))


def find_investment():
    ic1 = float(input("Income1 or Earn1 or obtain1 :"))
    iv1 = float(input("Investment1 or Stock1: "))
    ic2 = float(input("Income2 or Earn2 or obtain2 : "))
    iv2 = float((iv1 / ic1) * ic2)
    print("Investment2 or Stock2 :" + str(iv2))


def find_dividend():
    i1 = float(input("Investment1 : "))
    inc1 = float(input("Income1 : "))
    i2 = float(input("Investment2 : "))
    inc2 = float((inc1 / i1) * i2)
    print("Income2 : " + str(inc2))
    print("Dividend :" + str(inc2) + "%")


def find_annual_income():
    ti = float(input("Total Investment : "))
    inv1 = float(input("Investment in 1'share : "))
    fc1 = float(input("FaceValue of 1'Share : "))
    dvd = float(input("Dividend : "))
    ai = float((dvd /100 ) * ((ti / inv1) * fc1))
    print("Annual_Income : " + str(ai))


def find_income():
    ivt1 = float(input("Investment1 :"))
    income1 = float(input("Income1: "))
    ivt2 = float(input("Investment2 : "))
    income2 = float((income1 / ivt1) * ivt2)
    print("Income2 :" + str(income2))

given_data = input("CostPrice enter 1. or Sold_SV enter 2. or INV enter 3. or DVD enter 4. or A.I enter 5."
                   " or INC enter 6.")
if given_data == '1':
  find_cost_price()
elif given_data == '2':
  find_stock_value()
elif given_data == '3':
  find_investment()
elif given_data == '4':
 find_dividend()
elif given_data == '5':
 find_annual_income()
elif given_data == '6':
 find_income()
else:
 print('enter a valid input')
