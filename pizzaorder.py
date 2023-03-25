size = input("What size of pizza do you want to order S,M or L")
extra_pepporini = input("do you want extra pepporini Y or N")
extra_chese = input("do you want extra chese Y or N")
bill =0
if size == "S":
    bill+=15
elif size == "M":
    bill+=20
else:
    bill+=25
if extra_pepporini == "Y":
    bill+=2
else:
    bill+=3

if extra_chese == "Y":
    bill+=1
print(f"your total bill is {bill} thank yous")
