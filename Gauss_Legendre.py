from decimal import *
import time

getcontext().prec = int(input("Set calculate precision limit. > ")) + 1

# ガウス・ルジャンドル法の反復計算部
def gauss(a, b, t, p):
    new_a = (a + b) / 2
    new_b = (a * b) ** Decimal('0.5')
    new_t = t - p * ((a - new_a) ** 2)
    new_p = 2 * p
    return (new_a, new_b, new_t, new_p)

# 与えられた数値から円周率を計算する関数
def calc(a, b, t, p):
    pi = ((a + b) ** 2) / (4 * t)
    return pi

# 計算された円周率を適当に整形して出力する関数
def print_pi(s):
    count = 0
    print("3.", end='')

    for i in s[2:]:
        count += 1
        print(i, end='')
        if count % 10 == 0:
            print(end=' ')
            if count % 50 == 0:
                print("\n  ", end='')

    print()

def main():
    # time関数で実行時間を計測
    start = time.time()
    total_time = 0

    # 初期値
    a = 1
    b = Decimal('0.5') * Decimal('2') ** Decimal('0.5')
    t = Decimal('0.25')
    p = 1

    # 値はtupleで管理
    nums = (a, b, t, p)

    # 入力待ちは時間計測を一時停止
    total_time += time.time() - start
    loop = int(input("Input number of times to calculate. > "))
    start = time.time()

    count = 0
    
    # 実際の繰り返し計算部(forループなので速度は遅い)
    for i in range(loop):
        # gauss関数の引数としてnums tupleを展開して渡す
        nums = gauss(*nums)
        count += 1
        print(count)
    
    # 結果出力部
    print("Calculating pi...")
    # *nums でtupleを展開
    pi = calc(*nums)
    pi_length = len(str(pi))
    print_pi(str(pi))
    print(str(pi_length - 1) + " Digits calculated.")

    total_time += time.time() - start

    # ファイル出力をするか否か
    mode = input("Save result?(Destination filename is \"pi.txt\") Y/N > ")
    if mode.lower() == "y":
        with open("pi.txt", "w") as f:
            f.write(str(pi))

    print("Calc time:" + str(total_time) + "[sec]")

main()
