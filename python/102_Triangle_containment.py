import numpy as np

tris = [np.array([int(n) for n in l.strip().split(',')]).reshape((3,2)) for l in open('../p102_triangles.txt').readlines()]

def tri_contains_origin(tri):
    m = np.vstack((tri.T, np.ones(3, dtype=tri.dtype)))
    b = np.linalg.inv(m).dot(np.array([0,0,1]))
    return (0 < b).all() and (b < 1).all()

def p102():
    return len([tri for tri in tris if tri_contains_origin(tri)])

print(p102())
