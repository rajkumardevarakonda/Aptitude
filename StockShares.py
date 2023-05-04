from fractions import Fraction
def find_numberofshares():
    ti = float(input("Enter the TotalIncome : "))
    inc = float(input("Enter the Income on EachShare : "))
    brok= float(input("Enter the Brokerage : "))
    nsv = float(ti / (inc + brok))
    print("Number of ShareValues : " + str(nsv))

def find_TotalDebtre():
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


given_data = input("No of SV enter 1 or Total_Debenture enter 2 or Interest_on_faceValue enter 3 : ")
if  given_data == "1":
   find_numberofshares()
elif given_data == "2":
   find_TotalDebtre()
elif given_data == "3":
   find_interest_obtained_on_FaceValue()
else:
   print('enter a valid input')
