"""
Purpose: Fruit store


item        price       qty                   amount
apple       12/piece    5dozen=5*12=60         12*60    
mangos      35/piece    3dozen=3*12=36         35*36
                                            -----------
                                               1944
                               discount -2%   -38.88
                               ------------------------
                                               1905.12
                                Gst     +12.5% +238.14
                                ----------------------
                                               2143.26

                                               

Algorithm:
step1:Declare the constants
step2:Get the cost of fruits into variables 
step3:Get the quantity of fruits into variables
step4:compute the end quantity by substituting doxen value.
step5:compute the selling price of each item and add them.
step6:compute the discount amount and substract from 
      the celling price, to create payable amount.
step7:Calculate GST amount and add to payable amount 
     to create billable amount.

"""


#Constants
Dozen =12
Discount = 2
GST = 12.5


#cost of fruits
cost_of_apple = 12 # per piece
cost_of_mango = 34   # per piece


#Quantity of fruits
qty_of_apple = 5*Dozen  # pieces
cost_of_mango = 3*Dozen  # pieces


#Selling price computation - PEMDAS
total_sp=cost_of_apple*qty_of_apple + cost_of_mango*cost_of_mango
print("Discount Amount :",total_sp)


#Discount calculation 
discount_amount = total_sp*Discount
print("Discount Amount :",discount_amount)


#payable amount calculation
payable_amount = total_sp-discount_amount
print("payable Amount:",payable_amount)


#GST Calculation -PEMADAS
gst_on_fruits = payable_amount*GST/100
print("GST on Fruits :",gst_on_fruits)


#Billable Amount Calculation
billable_amount = payable_amount+gst_on_fruits
print("Billable Amount :",billable_amount)


#round(num, no_of_digits)
print("Billable Amount:",round(billable_amount,2))