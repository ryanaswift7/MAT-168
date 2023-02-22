import cvxpy as cp


#----------------- PROBLEM 1 ------------------------------------

## Create decision variables

# Each Mi variable corresponds to the
# amount of money investested in bond i
M1 = cp.Variable()
M2 = cp.Variable()
M3 = cp.Variable()
M4 = cp.Variable()


## Define parameters

# Each xri parameter corresponds to the
# expected return percentage of bond i (in decimal)
xr1 = 0.13
xr2 = 0.07
xr3 = 0.12
xr4 = 0.14

# Each wri corresponds to the worst-case return
# percentage for bond (in decimal)
wr1 = 0.06
wr2 = 0.07
wr3 = 0.10
wr4 = 0.09

# Each di parameter corresponds to the
# duration of bond i
d1 = 3
d2 = 4
d3 = 7
d4 = 9

# Define parameters so that I don't have to keep typing
# the total investment or max investment precentage per bond
total = 1000000
bond_max_percent = 0.42


## Define objective function
obj_fxn1 = cp.Maximize(((M1*xr1) + (M2*xr2) + (M3*xr3) + (M4*xr4)))


## Define constraints

# (1) Sum of all money invested is one million dollars
# (2) The sum of all worst case returns from each bond will still yield at
#       least an 8% return on the investment
# (3) Calculate average duration usng provided formula
# (4)-(7) Set upper and lower bounds for investment in each bond
constraints1 = [(M1 + M2 + M3 + M4) == total,      # (1)
                ((M1*wr1) + (M2*wr2) + (M3*wr3) + (M4*wr4)) >= (0.08*total), #(2)
                (((M1*d1) + (M2*d2) + (M3*d3) + (M4*d4))/total) <= 6, # (3)
                M1 <= bond_max_percent*total, M1 >= 0,          # (4)
                M2 <= bond_max_percent*total, M2 >= 0,          # (5)
                M3 <= bond_max_percent*total, M3 >= 0,          # (6)
                M4 <= bond_max_percent*total, M4 >= 0]          # (7)


# Form and solve problem
prob1 = cp.Problem(obj_fxn1, constraints1)
prob1.solve()

# Display solution
print()
print("Problem 1")
print('status:', prob1.status)
ROI_total = prob1.value/total # calculate ROI
print(f'optimal expected return: {ROI_total:.2%}') # display as ROI in decimal
print("Optimal investments by bond (dollars):")
print(f'Bond 1 = {M1.value:.2f}')
print(f'Bond 2 = {M2.value:.2f}')
print(f'Bond 3 = {M3.value:.2f}')
print(f'Bond 4 = {M4.value:.2f}')



#----------------------- PROBLEM 2 -------------------------------

## Create decision variables

# Each hij corresponds to the number of hours designer i works on project j
hA1 = cp.Variable()
hA2 = cp.Variable()
hA3 = cp.Variable()
hA4 = cp.Variable()
hB1 = cp.Variable()
hB2 = cp.Variable()
hB3 = cp.Variable()
hB4 = cp.Variable()
hC1 = cp.Variable()
hC2 = cp.Variable()
hC3 = cp.Variable()
hC4 = cp.Variable()


## Define parameters

# Each cij corresponds to the capability of designer i to work on project j
cA1 = 90
cA2 = 80
cA3 = 10
cA4 = 50
cB1 = 60
cB2 = 70
cB3 = 50
cB4 = 65
cC1 = 70
cC2 = 40
cC3 = 75
cC4 = 85

# Each rj corresponds to the number of hours required to work on project j
r1 = 70
r2 = 50
r3 = 85
r4 = 35


## Define the objective function

# Compute the total capability score as the sum of product of hours worked and
# capability on each project for each designer
obj_fxn2 = cp.Maximize(hA1*cA1 + hA2*cA2 + hA3*cA3 + hA4*cA4 +
                        hB1*cB1 + hB2*cB2 + hB3*cB3 + hB4*cB4 +
                        hC1 *cC1 + hC2*cC2 + hC3*cC3 + hC4*cC4)



## Define constraints
# (1)-(3) Each designer can work up to 80 hours
# (4) A minimum of 70 hours must be worked on project 1
# (5) A minimum of 50 hours must be worked on project 2
# (6) A minimum of 85 hours must be worked on project 3
# (7) A minimum of 35 hours must be worked on project 4
# (8)-(10) All values for hours worked must be nonnegative
constraints2 = [hA1 + hA2 + hA3 + hA4 <= 80,    # (1)
                hB1 + hB2 + hB3 + hB4 <= 80,    # (2)
                hC1 + hC2 + hC3 + hC4 <= 80,    # (3)
                hA1 + hB1 + hC1 >= 70,  # (4)
                hA2 + hB2 + hC2 >= 50,  # (5)
                hA3 + hB3 + hC3 >= 85,  # (6)
                hA4 + hB4 + hC4 >= 35,  # (7)
                hA1 >= 0, hA2 >= 0, hA3 >= 0, hA4 >= 0, # (8)
                hB1 >= 0, hB2 >= 0, hB3 >= 0, hB4 >= 0, # (9)
                hC1 >= 0, hC2 >= 0, hC3 >= 0, hC4 >= 0] # (10)



## Form and solve problem
prob2 = cp.Problem(obj_fxn2, constraints2)
prob2.solve()

## Display solution
print("\n")
print("Problem 2")
print("status:", prob2.status)
print(f'optimal capability score: {prob2.value:.2f}')
print()
print("Optimal time allocations for designer A (hours):")
print(f'Project 1 = {hA1.value:.2f}')
print(f'Project 2 = {hA2.value:.2f}')
print(f'Project 3 = {hA3.value:.2f}')
print(f'Project 4 = {hA4.value:.2f}')
print()
print("Optimal time allocations for designer B (hours):")
print(f'Project 1 = {hB1.value:.2f}')
print(f'Project 2 = {hB2.value:.2f}')
print(f'Project 3 = {hB3.value:.2f}')
print(f'Project 4 = {hB4.value:.2f}')
print()
print("Optimal time allocations for designer C (hours):")
print(f'Project 1 = {hC1.value:.2f}')
print(f'Project 2 = {hC2.value:.2f}')
print(f'Project 3 = {hC3.value:.2f}')
print(f'Project 4 = {hC4.value:.2f}')
