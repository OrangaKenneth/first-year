## 6.100A Pset 1: Part a 
## Name: Kenneth Oranga
## Time Spent:30 mins+ 30 mins debugging
## Collaborators:

##################################################################################
## Get user input for annual_salary, percent_saved and total_cost_of_home below ##
##################################################################################
annual_salary = float(input('Enter your annual salary; '))
percent_saved = float(input('Enter the percentage of your salary to save, as a decimal: '))
total_cost_of_home = float(input('Enter the cost of your dream home: '))
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
  
print(f'Number of months: {months}')
