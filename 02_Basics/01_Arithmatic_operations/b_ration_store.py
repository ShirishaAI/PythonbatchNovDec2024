"""
Purpose: Ration store
--------------------------------------------------------------
item              cost              quantity       amount

wheat             25/kg              30kgs          25*30=750/-
rice              12/kg              50kgs          12*50=600/-
                                                   ----------
                                                          1350
                                    subsidy 20%           -270
                                    --------------------------
                                    Billableamount     :  1080

                                    
                                                
Algorithm: 
step 1: Get the cost of items into variables
step 2: Get the quantity of items into variables
step 3: Compute the selling price to each item, and add them.
step 4: compute the subsity amount and substract 
        from the selling price.
step 5: Display the billable amount.

"""


#cost of items
cost_of_wheat = 25
cost_of_rice = 12


#Quantity of items
qty_of_wheat = 30
qty_of_rice = 50


#Selling price computation
sp_of_wheat = cost_of_wheat * qty_of_wheat
sp_of_rice = cost_of_rice * qty_of_rice
print("Selling price of wheat:",sp_of_wheat)
print("Selling orice of rice :",sp_of_rice)


#Total selling price
total_sp = sp_of_wheat+sp_of_rice


#print(total_sp)
print("Total selling price   :",total_sp)

subsidy_amount =(total_sp*20)/100   
print("Subsidy Amount       :",subsidy_amount)

billable_amount = total_sp - subsidy_amount
print("Billable Amount      :",billable_amount)

"""
output:
Selling price of wheat: 750
Selling orice of rice : 600
Total selling price   : 1350
Subsidy Amount       : 270.0
Billable Amount      : 1080.0

"""