# BASIC BANKING MANAGEMENT SYSTEM 

balance = 0
account_holder = ""

while True: 
    print("============================ WELCOME TO ABC BANK ============================")
     
    print("1. CREATE ACCOUNT")
    print("2. DEPOSIT MONEY") 
    print("3. WITHDRAW MONEY") 
    print("4. CHECK BALANCE") 
    print("5. EXIT")
    
    choice = input("ENTER YOUR CHOICE (1-5): ")
    
    if choice == "1": 
        if account_holder != "" : 
            print("ACCOUNT ALREADY EXIST.")
            
        else: 
            account_holder = input("ENTER YOUR NAME: ")
            
            if account_holder == "": 
                print("NAME CANNOT BE EMPTY.")
                
                account_holder = "" 
            else: 
                print("ACCOUNT CREATED SUCCESSFULLY!")
                print("WELCOME", account_holder)
                
    elif choice == "2":
        if account_holder == "" : 
            print("PLEASE CREATE AN ACCOUNT FIRST")
        else: 
            amount = float(input("ENTER AMOUNT TO DEPOSIT: $")) 
            if amount > 0: 
                balance += amount
                print("DEPOSIT SUCCESSFUL!")
                print(f"CURRENT BALANCE = ${balance:.2f}") 
                
            else: 
                print("ENTER A VALID POSITIVE AMOUNT")
                
                
    elif choice == "3": 
        if account_holder =="" : 
            print("PLEASE CREATE AN ACCOUNT FIRST")
        else: 
            amount = float(input("ENTER AMOUNT TO WITHDRAW: $."))
            
            if amount <= 0: 
                print("ENTER VALID POSITIVE AMOUNT.")
                
            elif amount > balance: 
                print("INSUFFICIANT BALANCE!")
            else: 
                balance -= amount
                
                print("WITHDRAWAL SUCCESSFUL!")
                
                print(f"REMAINING BALANCE : ${balance:.2f}")
    
    elif choice == "4": 
        if account_holder == "": 
            print("PLEASE CREATE AN ACCOUNT FIRST")
        else: 
            print("ACCOUNT HOLDER : ", account_holder)
            print(f"AVAILABLE BALANCE : ${balance:.2f}")
            
    
    elif choice == "5": 
        print("THANK YOU FOR USING ABC BANK!")
        
        break
    
    else: 
        print("INVALID CHOICE. PLEASE SELECT (1-5).")        