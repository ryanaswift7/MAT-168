import numpy as np

# distances from start of arc to end of arc
# [AC,AD,AE,BC,BD,BE,CUCD,CUCB,CUCLA,CUCSD,
# DUCD,DUCB,DUCLA,DUCSD,EUCD,EUCB,EUCLA,EUCSD]
dist = np.array([25.1, 128, 228, 272, 159, 68.4, 51.6, 19.6, 364,
				477, 149, 130, 252, 365, 236, 230, 172, 285])

truckCost = 0.85 # transport cost per barrel per mile
pipeCost = 0.7 # transport cost per barrel per mile
pipeMax = 811	# max barrels per pipeline

# Supply parameters
A = 700
B = 1200

# Demand parameters
UCD = 180
UCB = 270
UCLA = 135
UCSD = 90

# For reference, s0 = 9, s1 = 1