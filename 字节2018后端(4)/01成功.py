import sys

while True:
    s = sys.stdin.readline().strip()
    if len(s) == 0: break
    for i in range(int(s)):
        [n, k, d1, d2] = [int(x) for x in input().split()]
        max_left_1, max_left_2, min_left = 2 * d1 + d2, 2 * d2 + d1, d1 + d2
        if n - k <= min_left:
            print('yes' if min_left == 0 else 'no')
        elif not (k - 2 * d2 + d1) % 3 == 0 and not (k - max_left_1) % 3 == 0 and not (k - max_left_2) % 3 == 0:
            print('no')
        else:
            print('yes' if n % 3 == 0 else 'no')
