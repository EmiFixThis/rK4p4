# PyCode: RK4 for B&F ch. 5.4 problem 4d

# y' = -t*y + (4*t)/y
# 0 <= t <= 1
# t0 = 0
# y0 = 1
# delta = 0.1

# lambda functions: I decided to use a lambda functions to represent icky parts of my function.
# This should not be confused with Lambda calculus or functional programing. 

# Lambda functions in python are "generic" procedures that can be called just like any other function; in fact they are entirely optional. 
# But having the benefit of not needing return statements, takes arguments (even optional ones).
# Basically, lambda takes as arguments any single expression which must return a value, a generic function created by lambda implicitly returns this value. 
# You can live without it but it can make your code cleaner, and make the underlying structure a bit more apparent.



import math



def rK4(f):
    return lambda t, y, deltaT:(lambda deltaY1:(lambda deltaY2:(lambda deltaY3:(lambda deltaY4:(deltaY1+2*deltaY2+2*deltaY3+deltaY4)/6)(deltaT*f(t+deltaT, y+deltaY3))))(deltaT*f(t+deltaT/2, y+deltaY2/2)))(deltaT*f(t+deltaT/2, y+deltaY/2))(deltaT*f(t, y))


def theory(t): return -t*y+4*t/y


deltaY = rK4(lambda t, y: math.sqrt(4-3*exp((-t),2)))
t,y,deltaT = 0,1,0.1

while (t <= 10):
    if math.fabs(math.floor(t)-t) < 10**(-7):
        print "y=(%2.1f)\t=%4.6f \t error: %4.6g" % (t, y, math.fabs(y-theory(t)))
        t,y = t+ deltaT, y+deltaY(t, y, deltaT)

