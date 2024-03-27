from math import sqrt

def cosine_x_radians(x):
    global n
    global term
    global cos
    n = 0
    term = 1
    cos = 1
    for i in range(0, 9):
        n += 2
        term = (-1 * term) * ((x * x) / ((n - 1) * n))
        cos += term

def calculate_pi():
    global x
    global pi
    x = 1
    for i in range(0, 4):
        cosine_x_radians(x)
        x += cos / sqrt(1 - cos ** 2)
    pi = x * 2
    print(pi)

calculate_pi()