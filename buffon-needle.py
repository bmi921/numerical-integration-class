import random
import math


def buffons_needle(num_throws=100000, needle_length=1.0, line_spacing=2.0):
    """
    ビュフォンの針を使って円周率を近似する
    :param num_throws: 針を投げる回数
    :param needle_length: 針の長さ
    :param line_spacing: 線間の間隔
    :return: 円周率の近似値
    """
    if needle_length > line_spacing:
        raise ValueError("針の長さは線間隔以下でなければなりません。")

    cross_count = 0

    for _ in range(num_throws):
        # 針の中心と線までの最短距離 (0 から line_spacing/2 の範囲で乱数生成)
        center_distance = random.uniform(0, line_spacing / 2)
        # 針がなす角度 (0 から π の範囲で乱数生成)
        angle = random.uniform(0, math.pi)

        # 針が線と交差するかの判定
        if center_distance <= (needle_length / 2) * math.sin(angle):
            cross_count += 1

    # πを近似
    if cross_count == 0:
        return None  # 交差が一度もない場合の処理
    pi_estimate = (2 * needle_length * num_throws) / \
        (cross_count * line_spacing)
    return pi_estimate


# 実行例
estimated_pi = buffons_needle(
    num_throws=100000, needle_length=1.0, line_spacing=2.0)
print(f"ビュフォンの針を用いた円周率の近似値: {estimated_pi}")
