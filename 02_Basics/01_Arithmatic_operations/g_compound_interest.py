
# Initialise the Variables
#  
principal_amount = float(input("Please Enter the Loan Amount(Principal):"))
annual_interest = float(input("Please Enter the Anuual Interest Rate(in %):"))
times_compounded = float(input("Enter the number of times interest is compounded per year:"))
duration_of_loan = int(input("Enter the durtion of the loan(in year) :"))

# Compound Interest Calculation

total_loan_value  = principal_amount * (1 + annual_interest / times_compounded) ** (times_compounded * duration_of_loan)
compound_interest = total_loan_value - principal_amount

print("Principal Amount      :",principal_amount)
print("Annual Interest       :",annual_interest)
print("Number of Times Compound Interest:",times_compounded)
print("Duration of the Loan  :",duration_of_loan)

print("Compound Interest     :",round(compound_interest,2))
print("Final Amount of the loan:",round(total_loan_value,2))