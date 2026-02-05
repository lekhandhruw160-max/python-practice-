"""sac = "lekhan dhruw "
print(sac)"""

# school marks 
chimestry = int(input("Enter your chimestry marks : "))
physics = int(input("Enter your physics  marks : "))
math = int(input("Enter your math marks : "))
biology = int(input("Enter your biology marks : "))

sum = chimestry + physics + math + biology
total = sum / 4

if total >= 85:
    print("your final grad is : A")
elif total >= 70:
    print("your final grad is : B ")
elif total >= 50:
    print(("your final grad is : c "))
else : 
    print("you are failed in exam ")

print(total ,"try next time ")