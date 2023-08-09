class HouseItem:
    def __init__(self, name, area):
        # 家具名字，面积
        self.name = name
        self.area = area

    def __str__(self):
        # 返回家具名字，面积
        return "%s 占地 %.2f square meter" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area

        # 剩余面积
        self.free_area = area
        # 家具列表
        self.item_list = []

    def __str__(self):
        # 返回房屋信息
        return ("户型：%s\n总面积：%.2f\n剩余面积：%.2f\n家具列表：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):
        if item.area > self.free_area:
            print("剩余面积不足，请重新选择家具")
            return
        
        self.free_area -= item.area
        self.item_list.append(item.name)
        print("添加%s" % item)


# 创建家具
bed = HouseItem("床", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("桌子", 1.5)

print(bed)
print(chest)
print(table)

# 创建房子对象
my_home = House("两室一厅", 80)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)