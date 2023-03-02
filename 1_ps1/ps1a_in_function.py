def part_a(annual_salary, percent_saved, total_cost_of_home):
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
	return months