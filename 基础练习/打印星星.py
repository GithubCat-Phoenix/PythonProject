# 打印星星
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
row = 1
star_str = []
while row <= 9:
    print("*"*row)
    star_str.append("*"*row)
    row += 1
for star in star_str:
    print("|%s|" % star.strip().center(20))



