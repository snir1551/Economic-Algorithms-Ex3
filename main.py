import Orderly_Division_Or_Pareto_Improvement
import numpy as np

if __name__ == '__main__':
    player_b = np.array([40, 30, 20, 10])
    player_a = np.array([10, 20, 30, 40])

    division_player_a = np.array([0.1, 0, 0.4, 0.9])
    division_player_b = np.array([0.9, 1, 0.6, 0.1])

    # Player A transfers 0.1 of object 0 to player B, and player B transfers 0.1 of object 3 to player A
    #res = Ex5.orderly_division(player_a, player_b, division_player_a, division_player_b)


    #print(res)


    division_player_a1 = np.array([0, 0, 0.1, 0])
    division_player_b1 = np.array([1, 1, 0.9, 1])
    res = Orderly_Division_Or_Pareto_Improvement.orderly_division(player_a, player_b, division_player_a1, division_player_b1)


    print(res)

    division_player_a2 = np.array([0, 0, 0, 0.1])
    division_player_b2 = np.array([1, 1, 1, 0.9])
    res = Orderly_Division_Or_Pareto_Improvement.orderly_division(player_a, player_b, division_player_a2, division_player_b2)

    print(res)


    player_b = np.array([40,30])
    player_a = np.array([10,10])
    division_player_a2 = np.array([0.5, 0])
    division_player_b2 = np.array([0.5, 1])

    res = Orderly_Division_Or_Pareto_Improvement.orderly_division(player_a, player_b, division_player_a2,
                                                                  division_player_b2)
    print(res)

    player_b = np.array([40, 30])
    player_a = np.array([10, 10])
    division_player_a2 = np.array([0.5, 1])
    division_player_b2 = np.array([0.5, 0])

    res = Orderly_Division_Or_Pareto_Improvement.orderly_division(player_a, player_b, division_player_a2,
                                                                  division_player_b2)
    print(res)

    player_b = np.array([10, 20])
    player_a = np.array([10, 20])
    division_player_a2 = np.array([0.5, 0])
    division_player_b2 = np.array([0.5, 1])

    res = Orderly_Division_Or_Pareto_Improvement.orderly_division(player_a, player_b, division_player_a2,
                                                                  division_player_b2)
    print(res)