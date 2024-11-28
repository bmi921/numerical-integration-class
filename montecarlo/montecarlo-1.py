import random


def monte_carlo_pi(num_points=1000000):
    inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(0, 1)  # 0から1の乱数
        y = random.uniform(0, 1)  # 0から1の乱数

        if x**2 + y**2 <= 1:  # 原点から半径1以内の点をカウント
            inside_circle += 1

    pi_estimate = 4 * inside_circle / num_points
    return pi_estimate


# 実行例
pi = monte_carlo_pi()
print(f"円周率の近似値: {pi}")
