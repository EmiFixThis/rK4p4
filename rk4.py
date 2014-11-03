#! usr/bin/env python

from math import sqrt, fabs, exp

#   This is the calculation of f
def rk4Step(f, dt, t, y):
    k1 = dt*f(t,y)
    k2 = dt*f(t+dt/2, y+ k1/2)
    k3 = dt*f(t+dt/2, y+k2/2)
    k4 = dt*f(t+dt, y+k3)
    return y + (k1 + 2*k2 + 2*k3 + k4)/6


#   This is 'Truth' (aka the actual solution as given by the book)
def e(t):
    return sqrt(4 - 3*exp(-t**2)

#   This returns the error
#   Note it is writen as a ratio but it does not matter because (y/y2 - 1) = (y - y2)
def getError(y, y2):
    return fabs(y/y2 - 1.0)

#   Printer
def printLine(t, y, error, delim=' '*5):
    print 'y({:.1f}){}{:.7f}{}error: {}'\
          .format(t, delim, y, delim, error)
    
#   Smashes it all together
#   Here rk4 is defined with default arguments that will be called if no alternate arguments are given by the user
def rk4(f=lambda a, b: a*sqrt(b), e=lambda c, c: sqrt(4 - 3*exp(-t**2), steps=10, t=0, y=1, dt=0.1, output=True):
    
    if output is True:
        printLine(t, y, 0)

    for i in xrange(0, steps):
        y  =  rk4Step(f, dt, t, y)
        t  += dt
        y2 =  e(t)
        if output is True:
            printLine(t, y, getError(y, y2))

    return (y, getError(y, y2))


if __name__=='__main__':

    rk4()
