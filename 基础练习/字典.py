dic_wym = {"name": "王永梅",
           "电话号码" : 1573,
           "地址" : 10086}
print(dic_wym)
for k in dic_wym:
    print("%s--%s" % (k ,dic_wym[k]))
# dic_wym.clear()
# print(dic_wym)
# list_wym = ["wym"]
# print(list_wym)
# list_wym.clear()
# print(list_wym)
card_list = [
    {"name": "张三",
     "电话": "110"},
    {"name": "李四",
     "电话": "10086"}
]
for card_info in card_list:
    for key in card_info:
        print("%s--%s" % (key,card_info[key]))