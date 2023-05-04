from fractions import Fraction
def find_numberofshares():
    ti = float(input("Enter the TotalIncome : "))
    inc = float(input("Enter the Income on EachShare : "))
    brok= float(input("Enter the Brokerage : "))
    nsv = float(ti / (inc + brok))
    print("Number of ShareValues : " + str(nsv))

def find_Total_investment_on_Debenture() :
    tin = float(input("Total Income : "))
    ei = float(input("each income on face value : "))
    x = float(input("cost of each debenture : "))
    y = float(input("Brokerage : "))
    nd = float(tin / ei)
    ced = float(x + ((y * x)/100))
    tid =(ced * nd)
    print("T.Investment on debentures : " + str(tid))

def find_interest_obtained_on_FaceValue():
    ns = float(input("No of Shares : "))
    esv = float(input("each share value : "))
    d = float(input("Discount : "))
    invt = float(ns*(esv-d))
    print("investment :" + str(invt))
    fv = float(ns*esv)
    print("Face Value :" + str(fv))
    dvdp = Fraction(input("Dividend % : "))
    dvd = Fraction((dvdp / 100)*fv)
    interestObtained = float(dvd*100)/invt
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

given_data = input("No of SV enter 1 or Total_Debenture enter 2 or Interest_on_faceValue enter 3 "
                   " or Find_X_Part_in_total_Investment enter 4  or find which Stock is Better enter a : ")
if  given_data == "1":
   find_numberofshares()
elif given_data == "2":
   find_Total_investment_on_Debenture()
elif given_data == "3":
   find_interest_obtained_on_FaceValue()
elif given_data == "4":
    find_part_Of_Amount_In_Total_Investment()
elif given_data == "a":
    find_better_investment_Stock()
else:
   print('enter a valid input')
