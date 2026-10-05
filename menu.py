opt1 = "Coke"
opt2 = "Fanta"

while True :
    CI = (input("choose 1- Coke or 2- Fanta or q to end :"))
    if CI == "1":
         print("=========Menu============")
         print(opt1)
    elif CI == "2":
         print("=========Menu============")
         print(opt2)
    elif  CI == "q":
         print("Goodbye")
         break
    else :
         print("you have not enter 1,2or q")     


