import numpy as np


array6409 = np.loadtxt("NACA6409.dat", skiprows=1)
array2412 = np.loadtxt("NACA2412.dat", skiprows=1)


def split_airfoil(np_arr):
    x_cord = np_arr[:,0]

    # find the index that x_cord == 0
    ref_idx = list(x_cord).index(0)

    # split airfoil into upper and lower part
    upper = np_arr[:ref_idx+1]
    lower = np_arr[ref_idx:]
    return upper, lower


def get_area(arr):
    enum = list(enumerate(arr))
    # print(enum)
    # [(0, array([1.0e+00, 9.4e-04])), (1, array([0.9928 , 0.00313])), (2, array([0.97989, 0.00699])), ... ]
    small_sum = 0
    large_sum = 0
    for index, value in enum[:-1]:
        small_sum += (value[0] - enum[index+1][1][0])*value[1]
        # multiply x-cord difference and y-cord of current item

        # print(value)
        # [1.0e+00 9.4e-04]
        # print(value[0])
        # 1.0
        # print(enum[index+1])
        # (1, array([0.9928 , 0.00313]))
        # print(enum[index+1][1])
        # [0.9928  0.00313]
        # print(enum[index+1][1][0])
        # 0.9928
        
        large_sum += (value[0] - enum[index+1][1][0])*enum[index+1][1][1] 
        # multiply x-cord difference and y-cord of next item

    return 0.5*(small_sum + large_sum)


def cross_section(np_arr):
    splited = split_airfoil(np_arr)
    area = 0
    for item in splited:
        area += get_area(item)
    return area


print(cross_section(array6409))