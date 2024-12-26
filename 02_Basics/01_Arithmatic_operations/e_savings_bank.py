"""
Savings Bank Acoount

step1: Create a variable 'Balance' with initial value 0
step2: Initial deposite of min balance 1500
step3: Salary Credited of 3300
step4: Online Purchase of 33.33
step5: House rent paid of 1500
step6: Display Balace 

"""


# Declaring the Variables
initial_balance = 0
min_balance  = 1500
salary_credited =3300

print("Initial_Balance    :",initial_balance )
print("Min Balance        :",min_balance)
print("Salary Credited    : ",salary_credited)


# Total Account Balance 
total_balance  = initial_balance + min_balance + salary_credited
print("Total Account Balance:",total_balance)

# Total expences
online_purchese =33.33
house_rent= 1500
total_expences = online_purchese+house_rent
print("Total Expences       :",total_expences)

# Remaing Balance of the Account
remain_balance = total_balance - total_expences
print("Remaing Balance      :",remain_balance)