import random


def monte_carlo_ellipse_area(num_points=1000000):
    inside_ellipse = 0

    for _ in range(num_points):
        x = random.uniform(0, 2)  # xの範囲は0から2
        y = random.uniform(0, 1)  # yの範囲は0から1

        if (x**2) / 4 + y**2 <= 1:  # 楕円の内側の判定
            inside_ellipse += 1

    area = (2 * 1) * inside_ellipse / num_points  # 楕円を囲む長方形の面積 * 比率
    return area


# 実行例
ellipse_area = monte_carlo_ellipse_area()
print(f"楕円の面積: {ellipse_area}")
