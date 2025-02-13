# Welcome to the tip Calculator

bill = float(input("what is the total bill? Rs."))
tip = float(input("how much % you want to give tip"))
tip = tip/100 * bill
total_bill=bill+tip

split= int(input("how many person you want to split the bill"))
each_bill= round(total_bill/split,2)
print(f"you total bill is = {total_bill}")
print(f" each person should pay = {each_bill}")


