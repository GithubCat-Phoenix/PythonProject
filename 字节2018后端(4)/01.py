def team(n, k, d1, d2):
    i = 0
    while i <= n/3:
        if k == d1 + d2 and d1 + d2 != 0:
            if n-k == 2*d1 + 3*i and d1 != 0:
                return "yes"
            if n-k == 2*d2 + 3*i and d2 != 0:
                return "yes"
            else:
                return "no"
        if n - k == d1 + d2 + d2 + 3 * i:
            return "yes"
        if n - k == d1 + d2 + 3 * i:
            return "yes"
        if n - k == d1 + d1 + d2 + 3 * i:
            return "yes"
        i += 1
    else:
        return "no"


t = int(input().strip())
list_result = []
_ = 0
while _ < t:
    n, k, d1, d2 = list(map(int, input().split()))
    list_result.append(team(n, k, d1, d2))
    _ += 1
for result in list_result:
    print(result)


    # team1 - team2 = d1
    # team2 - team3 = d2
    # team1 + team2 + team3 = k