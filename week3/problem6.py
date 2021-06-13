import os
import sys
import math

"""
Notes:
- Your program converts user input to int? What limitation does this impose?
- I entered (1, 1, 1) and (2, 2, 2) and received:
Traceback (most recent call last):
  File "/Users/paulkorir/sci2pro/aishdharan/week3/week3/problem6.py", line 61, in <module>
    sys.exit(main())
  File "/Users/paulkorir/sci2pro/aishdharan/week3/week3/problem6.py", line 42, in main
    ang_a_b = math.acos(a_mul_b / mag_ab)
ValueError: math domain error

Determine the cause and fix it.
- For pt_* variables: is it better to use a tuple or a list? 
Why? Consider the key property differences between a tuple and list
 when deciding this.
"""


def main():
    # fixme: it is OK to use x0, y0, z0 as variables since
    #  they will make sense in the application domain (geometry)
    coord_x0 = 0
    coord_y0 = 0
    coord_z0 = 0
    pt_o = (coord_x0, coord_y0, coord_z0)
    print(f"Origin{pt_o}")
    coord_x1 = int(input("x1 = "))
    coord_y1 = int(input("y1 = "))
    coord_z1 = int(input("z1 = "))
    pt_a = [coord_x1, coord_y1, coord_z1]
    print(f"Coordinates of A{pt_a}")
    coord_x2 = int(input("x2 = "))
    coord_y2 = int(input("y2 = "))
    coord_z2 = int(input("z2 = "))
    pt_b = [coord_x2, coord_y2, coord_z2]
    print(f"Coordinates of B{pt_b}")
    dist_a_b = math.sqrt(((pt_a[0] - pt_b[0]) ** 2) + ((pt_a[1] - pt_b[1]) ** 2) + ((pt_a[2] - pt_b[2]) ** 2))
    dist_a_o = math.sqrt(((pt_a[0] - pt_o[0]) ** 2) + ((pt_a[1] - pt_o[1]) ** 2) + ((pt_a[2] - pt_o[2]) ** 2))
    dist_b_o = math.sqrt(((pt_b[0] - pt_o[0]) ** 2) + ((pt_b[1] - pt_o[1]) ** 2) + ((pt_b[2] - pt_o[2]) ** 2))
    print(f"The distance between points A and B in 3D space is: {dist_a_b}")
    print(f"The distance between points A and Origin in 3D space is: {dist_a_o}")
    print(f"The distance between points B and Origin in 3D space is: {dist_b_o}")
    a_mul_b = (pt_a[0] * pt_b[0] + pt_a[1] * pt_b[1] + pt_a[2] * pt_b[2])
    a_mul_o = (pt_a[0] * pt_o[0] + pt_a[1] * pt_o[1] + pt_a[2] * pt_o[2])
    b_mul_o = (pt_b[0] * pt_o[0] + pt_b[1] * pt_o[1] + pt_b[2] * pt_o[2])
    a_mag = math.sqrt((pt_a[0] ** 2) + (pt_a[1] ** 2) + (pt_a[2] ** 2))
    b_mag = math.sqrt((pt_b[0] ** 2) + (pt_b[1] ** 2) + (pt_b[2] ** 2))
    o_mag = math.sqrt((pt_o[0] ** 2) + (pt_o[1] ** 2) + (pt_o[2] ** 2))
    mag_ab = (a_mag * b_mag)
    mag_ao = (a_mag * o_mag)
    mag_bo = (b_mag * o_mag)
    ang_a_b = math.acos(a_mul_b / mag_ab)
    print(f"angle between A and B is {ang_a_b}")
    try:
        ang_a_o = math.acos(a_mul_o / mag_ao)
    except ZeroDivisionError as zde:
        print(f"Warning: {zde}; the denominator is zero")
        ang_a_o = "indefinite number"
    print(f"angle between A and Origin is {ang_a_o}")
    try:
        ang_b_o = math.acos(b_mul_o / mag_bo)
    except ZeroDivisionError as zde:
        print(f"Warning: {zde}; the denominator is zero")
        ang_b_o = "indefinite number"
    print(f"angle between B and Origin is {ang_b_o}")

    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())
