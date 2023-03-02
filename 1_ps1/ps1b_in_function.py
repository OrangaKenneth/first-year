def part_b(annual_salary, percent_saved, total_cost_of_home, semi_annual_raise):
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
	return months