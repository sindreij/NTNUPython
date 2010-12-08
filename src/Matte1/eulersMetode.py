'''
Created on 25. nov. 2010

@author: Sindre
'''

def calculateEuler(function, x0, y0, dx, steps):
    print "**Eulers method**"
    x = x0
    y = y0
    ex = compile(function, "<string>", "eval")
    formStr = "x=%6f y=%6f"
    print formStr % (x, y)
    for i in range(steps):
        f = eval(ex)
        y = y + f*dx
        x = x + dx
        print formStr % (x, y)
    return (x, y)

def calculateImprovedEuler(function, x0, y0, dx, steps):
    print "**Eulers improved method**"
    x = x0
    y = y0
    ex = compile(function, "<string>", "eval")
    def dydx(x,y):
        return eval(ex)
    formStr = "x=%6f y=%6f"
    print formStr % (x, y)
    for i in range(steps):
        f_1 = dydx(x,y)
        z = y + f_1*dx
        x = x + dx
        f_2 = dydx(x,z)
        y = y + ((f_1+f_2)/2)*dx
        print formStr % (x, y)
    return (x, y)

def calculateBoth(function, x0, y0, dx, steps):
    calculateEuler(function, x0, y0, dx, steps)
    print
    calculateImprovedEuler(function , x0, y0, dx, steps)

def run():
    calculateBoth("1+y", 0.0, 1.0, 0.1, 10)
    