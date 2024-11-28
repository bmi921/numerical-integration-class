import random


def monte_carlo_integration_1(num_points=1000000):
    total = 0

    for _ in range(num_points):
        x = random.uniform(0, 2)  # 積分範囲 [0, 2]
        total += x**2 + x + 1  # 関数値を合計

    integral = (2 - 0) * total / num_points  # (積分範囲) × (平均値)
    return integral


# 実行例
result_1 = monte_carlo_integration_1()
print(f"定積分の結果 (1): {result_1}")
