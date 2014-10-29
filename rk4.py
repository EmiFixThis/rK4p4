#! usr/bin/env python

from math import sqrt, fabs

def rk4Step(f, dt, t, y):
    k1 = dt*f(t,y)
    k2 = dt*f(t+dt/2, y+ k1/2)
    k3 = dt*f(t+dt/2, y+k2/2)
    k4 = dt*f(t+dt, y+k3)
    return y + (k1 + 2*k2 + 2*k3 + k4)/6


def getY2(t):
    return (t**2/4.0 + 1)**2


def getError(y, y2):
    return fabs(y/y2 - 1.0)


def printLine(t, y, error, delim=' '*5):
    print 'y({:.1f}){}{:.7f}{}error: {}'\
          .format(t, delim, y, delim, error)
    

def rk4(f=lambda x, y: x*sqrt(y), steps=10, t=0, y=1, dt=0.1, output=True):
    
    if output is True:
        printLine(t, y, 0)

    for i in xrange(0, steps):
        y = rk4Step(f, dt, t, y)
        t += dt
        y2 = getY2(t)
        if output is True:
            printLine(t, y, getError(y, y2))

    return y


if __name__=='__main__':

    rk4()
