import Ex5
import numpy as np

if __name__ == '__main__':
    player_b = np.array([40, 30, 20, 10])
    player_a = np.array([10, 20, 30, 40])
    division_player_a = np.array([1, 0, 0.4, 0.7])
    division_player_b = np.array([0, 1, 0.6, 0.3])

    res = Ex5.share_minimal(player_a, player_b, division_player_a, division_player_b)
    print(res)

    res = Ex5.check_pareto_improvement(player_a, player_b, division_player_a, division_player_b)
    print(res)