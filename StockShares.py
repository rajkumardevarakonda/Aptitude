def find_numberofshares():
    ti = float(input("Enter the TotalIncome : "))
    inc = float(input("Enter the Income on EachShare : "))
    brok= float(input("Enter the Brokerage : "))
    nsv = float(ti / (inc + brok))
    print("Number of ShareValues : " + str(nsv))

given_data = input("No of ShareValues enter 1")
if given_data == '1':
   find_numberofshares()
else:
 print('enter a valid input')
