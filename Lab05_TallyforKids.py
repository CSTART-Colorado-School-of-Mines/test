#Lab05B TallyForKids


print("Enter values to add. Enter quit when done.")
num = 0
count = 0
total = 0
num = input("NUMBER> ")

while num != "quit":
    if num == "Quit" or num == "QUIT" or num == "QUit":
        print("Input invalid. If you want to stop enter: quit")
        num = input("NUMBER> ")
    else:
        count += 1
        num = int(num)
        total += num
        num = input("NUMBER> ")
    

    
print(f"The addition of the {count} numbers entered is:")
print("OUTPUT", count, "numbers")
print("OUTPUT", total, "total")
        

 
    


    
