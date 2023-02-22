import cvxpy as cp
import numpy as np
from hw3prob2data import *

b = np.array([-A, -B, 0, 0, 0, UCD, UCB, UCLA, UCSD])
b = b[np.newaxis, :]
b = b.reshape(9,1) # b column vector

# x is the vector of decision variables
# whose indices correspond to the values listed below
# x = [AC,AD,AE,BC,BD,BE,CUCD,CUCB,CUCLA,CUCSD,
#				DUCD,DUCB,DUCLA,DUCSD,EUCD,EUCB,EUCLA,EUCSD]
x = cp.Variable((18,1), nonneg=True)


# create the u vector
# u1 is the section of u corresponding to plant->tank farm
# u2 is the section of u corresponding to tank farm->school
# for simplicity, these are constructed separately and appended
u1 = np.ones(6)*pipeMax
u2 = np.ones(12)*2*pipeMax
u = np.append(u1,u2)
u = u[np.newaxis,:]
u = u.reshape(18,1)

# M is the matrix representing the network arcs
# where the arcs are the horizontal axis,
# and vectices are the vertical axis
M = np.array([[-1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
			   [0,  0,  0, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
			   [1,  0,  0,  1,  0,  0, -1, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0],			
			   [0,  1,  0,  0,  1,  0,  0,  0,  0,  0, -1, -1, -1, -1,  0,  0,  0,  0],			
			   [0,  0,  1,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1, -1],			
			   [0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0],
			   [0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0],			
			   [0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0,  1,  0],			
			   [0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0,  1]])

constraints = [x <= u, M@x >= b]
# When the comparison between Mx and b was anything other than greater than,
# the program always output an infeasible status. It makes sense to minimize,
# x components until they are tight with b, but it seems strange that I cannot
# simply use an == operator.

# initialize var to hold costs
fxn = 0

# calculate costs for the 6 pipeline routes
for i in range(6):
	fxn += x[i]*dist[i]*pipeCost

# calculate costs for the 12 truck routes
for i in range(12):
	fxn += x[i+6]*dist[i+6]*truckCost

obj = cp.Minimize(fxn)
prob = cp.Problem(obj, constraints)
prob.solve()

print("Status:", prob.status)
print(f'Minimum Cost: {prob.value:.2f}')
print("--------------------------")
print("Optimal Barrels per Route")
print(f'AC: {x[0][0].value:.2f}')
print(f'AD: {x[1][0].value:.2f}')
print(f'AE: {x[2][0].value:.2f}')
print(f'BC: {x[3][0].value:.2f}')
print(f'BD: {x[4][0].value:.2f}')
print(f'BE: {x[5][0].value:.2f}')
print(f'CUCD: {x[6][0].value:.2f}')
print(f'CUCB: {x[7][0].value:.2f}')
print(f'CUCLA: {x[8][0].value:.2f}')
print(f'CUCSD: {x[9][0].value:.2f}')
print(f'DUCD: {x[10][0].value:.2f}')
print(f'DUCB: {x[11][0].value:.2f}')
print(f'DUCLA: {x[12][0].value:.2f}')
print(f'DUCSD: {x[13][0].value:.2f}')
print(f'EUCD: {x[14][0].value:.2f}')
print(f'EUCB: {x[15][0].value:.2f}')
print(f'EUCLA: {x[16][0].value:.2f}')
print(f'EUCSD: {x[17][0].value:.2f}')