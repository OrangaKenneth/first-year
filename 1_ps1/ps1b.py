## 6.100A Pset 1: Part b
## Name:Kenneth Oranga
## Time Spent:10 mins 
## Collaborators:

##################################################################################################
## Get user input for annual_salary, percent_saved, total_cost_of_home, semi_annual_raise below ##
##################################################################################################
annual_salary = float(input('Enter your annual salary; '))
percent_saved = float(input('Enter the percentage of your salary to save, as a decimal: '))
total_cost_of_home = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annaul raise as a decimal: '))
#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
percentage_down_payment = 0.25
r = 0.05
down_payment= total_cost_of_home*percentage_down_payment
amount_saved = 0
months = 0
###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while amount_saved <= down_payment:
    amount_saved = amount_saved + annual_salary*percent_saved/12+ amount_saved * (r/12)  
    months += 1
    if months % 6==0:
        annual_salary += annual_salary*semi_annual_raise
print(amount_saved, down_payment)
print(f'Number of months: {months}')
