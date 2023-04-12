import numpy as np

A = [[1.0000,-0.0383,-0.2101],[-0.0383,1.0000,0.2251],[-0.2101,0.2251,1.0000]] #original correlation matrix

vol_stocks = 0.1704
vol_bonds = 0.3354
vol_inflation = 0.0296

mean_stocks = 0.0883
mean_bonds = 0.0354
mean_inflation = 0.04

U = np.linalg.cholesky(A) #creating cholesky decomposition of A
R = np.random.normal(0, 1, size=(5,3)) #normal random numbers
Rc = R @ U #Array of correlated random sequences

#turning into percentages
for i in range(len(Rc)):
    Rc[i][0] = 100 * (Rc[i][0] * vol_stocks + mean_stocks)
    Rc[i][1] = 100 * (Rc[i][1] * vol_bonds + mean_bonds)
    Rc[i][2] = 100 * (Rc[i][2] * vol_inflation + mean_inflation)

print(Rc)