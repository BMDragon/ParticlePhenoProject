import numpy as np

# Data taken from 
# Assumes 3 neutrino mixing, normal ordering, no CP-violation, without SK-atm
theta12 = 33.82 * np.pi / 180
theta13 = 8.61 * np.pi / 180
theta23 = 48.3 * np.pi / 180

s12 = np.sin(theta12); c12 = np.cos(theta12)
s13 = np.sin(theta13); c13 = np.cos(theta13)
s23 = np.sin(theta23); c23 = np.cos(theta23)

# Data taken from NuFIT 6.0 (2024) http://www.nu-fit.org/?q=node/294
PMNSbounded = np.array([[[0.801, 0.842], [0.519, 0.580], [0.142, 0.155]],
                        [[0.248, 0.505], [0.473, 0.682], [0.649, 0.764]],
                        [[0.270, 0.521], [0.483, 0.690], [0.628, 0.746]]])

def getElems(mean, upper, lower):
    ret = mean
    if mean < 0:
        mean = -mean
    low = (mean - lower)/3
    high = (upper - mean)/3
    unc = max(low, high)
    return ret, unc

PMNS = np.array([[getElems(c12*c13, PMNSbounded[0,0,1], PMNSbounded[0,0,0]), 
                  getElems(s12*c13, PMNSbounded[0,1,1], PMNSbounded[0,1,0]), 
                  getElems(s13, PMNSbounded[0,2,1], PMNSbounded[0,2,0])],
                 [getElems(-s12*c23 - c12*s23*s13, PMNSbounded[1,0,1], PMNSbounded[1,0,0]), 
                  getElems(c12*c23 - s12*s23*s13, PMNSbounded[1,1,1], PMNSbounded[1,1,0]), 
                  getElems(s23*c13, PMNSbounded[1,2,1], PMNSbounded[1,2,0])],
                 [getElems(s12*s23 - c12*c23*s13, PMNSbounded[2,0,1], PMNSbounded[2,0,0]), 
                  getElems(-c12*s23 - s12*c23*s13, PMNSbounded[2,1,1], PMNSbounded[2,1,0]), 
                  getElems(c23*c13, PMNSbounded[2,2,1], PMNSbounded[2,2,0])]])

print(PMNS)

np.save('PMNS.npy', PMNS)