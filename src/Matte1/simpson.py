'''
Created on 18. okt. 2010

@author: Sindre
'''

import math

def simpson(n):
    if (n < 4) or (n % 2 != 0):
        return -1
    sum = 0.0
    a = 0.0
    b = 1.0
    h = (b-a)/n
    for j in range(n+1):
        res = math.sin(a+j*h)
        if not((j == 0) or (j ==n+1)):
            if j%2==0:
                res = res*2
            else:
                res = res*4
        sum = sum + res
    return (h/3.0)*sum
def run():
    approx = simpson(2000)
    exact = math.cos(0) - math.cos(1)
    print "Approx: %f, Exact: %f, Difference: %f" % (approx, exact, abs(approx-exact))