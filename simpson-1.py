import math

# 被積分関数 f(x) 
def f(x):
    return math.sqrt(4 - x**2)

# シンプソン則による数値積分
def simpsons_rule(a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be an even number")
    
    h = (b - a) / n  # 小区間の幅
    result = f(a) + f(b)  # 両端の値を加算
    
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            result += 2 * f(x)  # 偶数項の係数は2
        else:
            result += 4 * f(x)  # 奇数項の係数は4
    
    result *= h / 3  # シンプソン則の公式
    return result

def main():
    # 真値 (円周率)
    true_value = math.pi
    
    # 積分区間
    a, b = 0, 2
    
    # 分割数 n のリスト
    partitions = [50, 100, 500, 1000, 2000, 5000, 10000, 20000]
    
    # ヘッダー
    print(f"{'Partitions (n)':<15}{'Simpson s Rule':<20}{'Error (Absolute)':<20}")
    
    # 各 n に対して計算
    for n in partitions:
        result = simpsons_rule(a, b, n)
        error = abs(true_value - result)  # 真値との絶対誤差
        print(f"{n:<15}{result:<20.8f}{error:<20.8f}")

if __name__ == "__main__":
    main()
