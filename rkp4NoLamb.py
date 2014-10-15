#! usr/bin/env python

import math

# rk4 problem 4 B&F No Lambda

t = 0
y = 1
dt = 0.1

def rk4(f, dt, t, y):
    k1 = dt*f(t,y)
    k2 = dt*f(t+dt/2, y+ k1/2)
    k3 = dt*f(t+dt/2, y+k2/2)
    k4 = dt*f(t+dt, y+k3)
    return y + (k1 + 2*k2 + 2*k3 + k4)/6


def rkIter(f, steps):
    prev = 1

    for i in xrange(0, steps):
        x = t+dt*i

        res = rk4(f, dt, t+dt*(i-1), prev)

        y2 = (x*x/4 + 1)**2
        print 'y(%g)\t%g\terror: %g' % (x, res, res/(y2-1))

        prev = res

if __name__=='__main__':

    def myFun(x,y):
        return x*math.sqrt(y)

    steps = int(1+(y-t)/dt)
    rkIter(myFun, steps)



