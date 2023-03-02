## 6.100A Pset 1: Part c
## Name: Kenneth Oranga
## Time Spent:30 mins
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input('Enter your initial deposit: '))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
house_cost = 800000
down_payment = 0.25*house_cost
amount_saved = initial_deposit
high = 1
low = 0
r = 0
steps =0

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

while abs(amount_saved - down_payment) >= 100:
    r = (high+low)/2
    amount_saved = initial_deposit*(1+r/12)**36
    if amount_saved < down_payment:
        low = r
    else:
        high = r
    
    r = (high+low)/2
    steps += 1
    if (initial_deposit*(1+1/12)**36) < down_payment:#amount saved is maximum when r=1, prevents infinte loops
        r = None
        steps = 0
        break
print(f'steps; {steps}')
print(f'rate: {r}')
