import math
import random


def monte_carlo_integration_2(num_points=1000000):
    total = 0

    for _ in range(num_points):
        x = random.uniform(0, 2)  # 積分範囲 [0, 2]
        total += math.sqrt(4 - x**2)  # 関数値を合計

    integral = (math.pi / 2 - 0) * total / num_points
    return integral


# 実行例
result_2 = monte_carlo_integration_2()
print(f"定積分の結果 (2): {result_2}")
