from fractions import Fraction
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


def find_numberofshares():
    TotalIncome = float(input("Enter the TotalIncome : "))
    incone_on_each_share = float(input("Enter the Income on EachShare : "))
    brokerage= float(input("Enter the Brokerage : "))
    Number_of_ShareValues = float(TotalIncome / (incone_on_each_share + brokerage))
    print("Number of ShareValues : " + str(Number_of_ShareValues))

def find_Total_investment_on_Debenture() :
    Total_Income = float(input("Total Income : "))
    One_Share_Income = float(input("each income on single investment : "))
    x = float(input("cost of each debenture : "))
    y = float(input("Brokerage : "))
    number_of_debenture = float(Total_Income / One_Share_Income)
    cost_of_each_debenture = float(x + ((y * x)/100))
    Total_Investment_on_debentures =(cost_of_each_debenture * number_of_debenture)
    print("T.Investment on debentures : " + str(Total_Investment_on_debentures))

def find_interest_obtained_on_FaceValue():
    number_of_shares = float(input("No of Shares : "))
    each_share_value = float(input("each share value : "))
    discount = float(input("Discount : "))
    investment = float(number_of_shares*(each_share_value-discount))
    print("investment :" + str(investment))
    faceValue = float(number_of_shares*each_share_value)
    print("Face Value :" + str(faceValue))
    dividend_percentage = Fraction(input("Dividend % : "))
    dividend = Fraction((dividend_percentage / 100)*faceValue)
    interestObtained = float(dividend*100)/investment
    print("Interest Obtained :" + str(interestObtained) + "%")

def find_part_Of_Amount_In_Total_Investment():
    a = float(input("1st dividend part on market Value by 1st investment : "))
    b = float(input("first Market Value : "))
    c = float(input("2st dividend part on market Value by 2nd investment : "))
    d = float(input("Second Market Value : "))
    e = float(input("Total Investment : "))
    f = float(input("Total Income or Dividend (enter 0 to skip): "))
    if f!=0:
        x = ((b * d * f) - (c * b * e)) / ((a * d) - (c * b))
        print("1stPart invested on total Amount : " + str(x))
    else:
        y = (c * e * b * d) / ((d * a * d) + (d * c * b))
        print("1stPart invested on total Amount : " + str(y))

def find_better_investment_Stock():
    a = float(input("enter AnnualIncome on 1's share a1 : "))
    b = float(input("enter Market_value b1 : "))
    c = float(input("enter AnnualIncome on 1's share a2 : "))
    d = float(input("enter Market_value b2 : "))
    t = float(input("tax : "))
    if t==0:
        x = (a * b * d) / b
    else:
        x = ((a * b * d) / b)*t
    print("X Annual_Income 1st Case : " + str(x))
    y = (c*b*d)/d
    print("Y Annual_Income 2nd Case : " + str(y))
    if x>y:
        print(str(a) + " Stock at " + str(b) + " is better")
    else:
        print(str(c) + " Stock at " + str(d) + " is better")


def find_Loss_or_gain_on_amount_invested_in_bank_and_Stock():
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

def find_Maximum_Return():
    a = int(input('total investment = '))
    b = int(input('max percentage on bond b = '))
    x = 100 * a / (b + 100)
    y = a - x
    print((x, y))
    c = int(input('percentage on bond a = '))
    d = int(input('percentage on bond b = '))
    total = (c * x / 100) + (d * y / 100)
    print("Maximum Return : " + str(total))

def find_Ratios_of_Investments():
    a = Fraction(input('Stock value a = '))
    b = Fraction(input('Dividend % a = '))
    c = Fraction(input('Stock Value b = '))
    d = Fraction(input('Dividend % b = '))
    x = (a / b)
    y = c / d
    z = x / y
    print("Ratios of Investments : "+ str(z))


def find_change_in_Income():
    a = float(input("1st Investment : ")) # Stock value purchased
    b = float(input("one Share Value of 1st Investment : "))
    c = float(input("Annual Dividend % on one Share of A : "))
    d = float(input("One Share Value Sold at : "))
    e = float(input("New Stock Value Invested : "))
    f = float(input("Dividend % of One New Stock Value : "))
    x = (c*(a/b))
    y = (f*d*(a/b))/e
    D = (y-x)
    print("change in Income : " + str(D))

def find_change_in_income_on_service_charge():
    a = float(input("total Shares sold at : "))
    b = float(input("Dividend % on one Share of  : "))
    c = float(input("one Share Value of 1st Investment : "))
    d = float(input("Dividend % on one New Stock Value: "))
    e = float(input("one Share Value of 2nd Investment: "))
    f = float(input("Service Charges % of Face value: "))
    # face Value = 100
    g = a/100  # no. of shares sold
    h = (c-f)*g
    i = (h)/(e+f)  # no. of new shares that invested in
    x = (a * b) / 100
    y = (d*i)
    D = (y-x)
    print("change in Income : " + str(D))


given_data = input("   CostPrice enter 1 \nor Sold_ShareValue enter 2 \nor Investment enter 3 \nor Dividend enter 4 "
                   "\nor Annual_Income enter 5 \nor Income enter 6 \nor No. of numberofshares enter 7 "
                   "\nor Total_Debenture enter 8 \nor Interest_on_faceValue enter 9 \n"
                   "or Find_X_Part_in_total_Investment enter 10 \nor find which Stock is Better enter 11 \nor "
                   "find Loss or gain on amount invested in bank & Stock enter 12 : \n"
                   "or find Q.24 enter 13 \nor find Q.25 enter 14 \nor find change in Income enter 15 : \nor "
                   "find change in income on service charge enter 16 \n  = ")
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
elif given_data == "7":
 find_numberofshares()
elif given_data == "8":
 find_Total_investment_on_Debenture()
elif given_data == "9":
 find_interest_obtained_on_FaceValue()
elif given_data == "10":
 find_part_Of_Amount_In_Total_Investment()
elif given_data == "11":
 find_better_investment_Stock()
elif given_data == "12":
 find_Loss_or_gain_on_amount_invested_in_bank_and_Stock()
elif given_data == "13":
 find_Maximum_Return()
elif given_data == "14":
 find_Ratios_of_Investments()
elif given_data == "15":
 find_change_in_Income()
elif given_data == "16":
 find_change_in_income_on_service_charge()
else:
 print('enter a valid input')
