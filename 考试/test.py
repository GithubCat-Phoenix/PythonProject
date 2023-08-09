suit = ["黑桃", "红心", "方块", "梅花"]
num = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]
score_map = {}

for s in suit:
    count = 2
    for n in num:
        score_map[f"{s}{n}"] = count
        count += 1
score_map.update({"joker": 14, "Joker": 15})
print(score_map)