# Tip Calculator

print("Welcome to the Tip calculator")
bill = input("What was the total bill?")
tippercent = input("What percentage tip would you like to give?10,12 or 15?")
peoplesplit = input("How many people to split the bill?")
totaltip = 0.01 * int(tippercent) * float(bill)
splitperperson = round(float(bill)/int(peoplesplit) + totaltip/int(peoplesplit),2)

print(f"Each person should pay: {splitperperson}")