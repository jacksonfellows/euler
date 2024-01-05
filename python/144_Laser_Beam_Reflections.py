import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse


def angle(A, B):
    a = A/np.linalg.norm(A)
    b = B/np.linalg.norm(B)
    return np.arccos(np.dot(a,b))

def find_C(A, B):
    m = np.array([B[1], -4*B[0]])
    a1 = angle(A - B, -m)
    a2 = np.arctan2(m[1], m[0])
    a = a2 - a1
    d = np.array([np.cos(a), np.sin(a)])
    t = (-4*B[0]*d[0] - B[1]*d[1] + 2*np.sqrt(100*d[0]**2 - B[1]**2*d[0]**2 + 2*B[0]*B[1]*d[0]*d[1] + 25*d[1]**2 - B[0]**2*d[1]**2))/(4*d[0]**2 + d[1]**2)
    return B + t*d

def draw():
    fig, ax = plt.subplots()
    e = Ellipse((0,0), 10, 20, facecolor="none", edgecolor="k")
    ax.set_xlim(-7,7)
    ax.set_ylim(-12,12)
    ax.add_artist(e)
    A, B = np.array([0,10.1]), np.array([1.4,-9.6])
    for n in range(1000):
        plt.plot([A[0], B[0]], [A[1], B[1]], color="r")
        if -0.01 <= B[0] <= 0.01 and B[1] > 0:
            print(n, B)
            break
        A, B = B, find_C(A, B)
    plt.show()
