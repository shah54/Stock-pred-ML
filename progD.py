from numpy import *
x = array([1,2,3,4,5,6,7,8,9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
y = array( [201.5,207.39,207.99,208.23, 208.74,209.07,207.11, 207.25,208.88,207.53,207.79,208.05,208.87,209.75,210.24,213.32,217.58,216.79,216.25,215.46,215.04,215.05])

from scipy.interpolate import *
lin = polyfit(x, y, 1)
quad = polyfit(x,y,2)
cubic polyfit(x, y, 3)
high polyfit(x,y,4)

from matplotlib.pyplot import *
plot(x, y, '0')
bf=linspace (1,25,500)
plot (bf, polyval(lin, bf), 'b-')
plot (bf, polyval (quad, bf), 'r-')
plot (bf, polyval(cubic, bf), 'b:')
plot (bf, polyval (high, bf), 'g:')

yfit = lin[0] * x + lin[1]
yresi = y-yfit
SqSumResi = sum (pow(yresi, 2))
SqSumTotal = len(y) * var(y)
rsquared = 1 - SqSumResi/SqSumTotal
print (rsquared)
