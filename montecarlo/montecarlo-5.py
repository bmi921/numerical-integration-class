import random


def monte_carlo_integration_3(num_points=1000000):
    total = 0

    for _ in range(num_points):
        x = random.uniform(0, 1)  # 積分範囲 [0, 1]
        total += 4 / (1 + x**2)  # 関数値を合計

    integral = (1 - 0) * total / num_points
    return integral


# 実行例
result_3 = monte_carlo_integration_3()
print(f"定積分の結果 (3): {result_3}")
