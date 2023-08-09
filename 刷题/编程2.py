gifts = input().split()

for money in gifts:
    if gifts.count(money) > len(gifts)/2:
        print(money)
    else:
        print("0")
    