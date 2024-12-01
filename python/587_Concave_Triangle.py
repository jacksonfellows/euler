import math

import scipy

L_section_area = (4 - math.pi)/4

def circle_y(x):
    return 1 - (2*x - x**2)**0.5

def concave_tri_area(m):
    x_int = scipy.optimize.fsolve(lambda x: circle_y(x) - m*x, 0.29)[0]
    return 0.5*x_int*circle_y(x_int) + scipy.integrate.quad(circle_y, x_int, 1)[0]

def p():
    n = 1
    while concave_tri_area(1/n) > 0.001*L_section_area: n += 1
    return n
