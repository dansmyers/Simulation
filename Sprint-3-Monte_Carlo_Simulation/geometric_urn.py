# Geometric Distribution Expected Value = 1/p
# Reasonable estimates for the number of black and red balls in one turn:
# 100 * p (red) and 100 * (1 - p) (black)

e = 20
p = 1/e

print('Expected balls in Geometric Urn:')
print('Red balls: %.0f\nBlack balls: %.0f' % (100 * p, 100 * (1 - p)));