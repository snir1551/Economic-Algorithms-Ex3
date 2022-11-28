import cmath
import math
import random

import numpy as np


def orderly_division(player_a, player_b, division_player_a, division_player_b):
    minimum, maximum = search_minimum_maximum(player_a, player_b, division_player_a, division_player_b, False)
    if minimum < maximum:
        return False

    return share_minimal(player_a, player_b, division_player_a, division_player_b)


def search_minimum_maximum(player_a, player_b, division_player_a, division_player_b, place_minimum):
    maximum = 0
    minimum = math.inf
    index_object1 = 0
    index_object2 = 0
    for i in range(len(player_a)):
        if minimum > (player_a[i] / player_b[i]) and division_player_a[i] > 0:
            minimum = (player_a[i] / player_b[i])
            index_object1 = i
        if maximum < (player_a[i] / player_b[i]) and division_player_b[i] > 0:
            maximum = player_a[i] / player_b[i]
            index_object2 = i
    if place_minimum is True:
        return index_object1, index_object2
    else:
        return minimum, maximum


def share_minimal(player_a, player_b, division_player_a, division_player_b):
    index_object1, index_object2 = search_minimum_maximum(player_a, player_b, division_player_a, division_player_b,True)
    va1 = player_a[index_object1]
    va2 = player_a[index_object2]
    vb1 = player_b[index_object1]
    vb2 = player_b[index_object2]


    while True:
        z = random.random()
        y = random.random()
        if z/y > (va1/va2) and z/y < (vb1/vb2):
            z_floor = math.floor(z * 10) / 10
            y_floor = math.floor(y * 10) / 10
            if y_floor <= division_player_a[index_object1] and z_floor <= division_player_b[index_object2] and y_floor > 0 and z_floor > 0:
                break

    temp_division_player_a = division_player_a.copy()
    temp_division_player_b = division_player_b.copy()
    temp_division_player_a[index_object1] -= y_floor
    temp_division_player_b[index_object1] += y_floor
    temp_division_player_a[index_object2] += z_floor
    temp_division_player_b[index_object2] -= z_floor

    txt = "Pareto improvement: Player A transfers {} of object {} to player B, and player B transfers {} of object {} to player A"
    print(txt.format(y_floor,index_object1,z_floor,index_object2))
    txt = "The improvement after the division: player A - {} , player B - {}"
    print(txt.format(temp_division_player_a,temp_division_player_b))
    return temp_division_player_a, temp_division_player_b


def check_pareto_improvement(player_a, player_b, division_player_a, division_player_b):
    new_division_player_a,new_division_player_b = share_minimal(player_a, player_b, division_player_a, division_player_b)
    new_sum_a = 0
    new_sum_b = 0
    old_sum_a = 0
    old_sum_b = 0
    for i in range(len(player_a)):
        old_sum_a += player_a[i] * new_division_player_a[i]
        old_sum_b += player_b[i] * new_division_player_b[i]
        new_sum_a += player_a[i] * division_player_a[i]
        new_sum_b += player_b[i] * division_player_b[i]

    if (new_sum_a > old_sum_a and new_sum_b >= old_sum_b) or (new_sum_b > old_sum_b and new_sum_a >= old_sum_a):
        txt = "old sum A = {} , new sum A = {} , old sum B = {} , new sum B {}"
        print(txt.format(old_sum_a,new_sum_a,old_sum_b,new_sum_b))
        return True
    else:
        print("problem")
        txt = "old sum A = {} , new sum A = {} , old sum B = {} , new sum B {}"
        print(txt.format(old_sum_a, new_sum_a, old_sum_b, new_sum_b))
        return False