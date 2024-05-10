def func(*data):
    middle_names = {}
    for name in data:
        if len(name) == 2:
            middle_name = name[1]
        elif len(name) == 3 or len(name) == 4:
            middle_name = name[-2]
        else:
            middle_name = name[2]

        if middle_name not in middle_names:
            middle_names[middle_name] = name
        else:
            del middle_names[middle_name]

    if middle_names:
        print(list(middle_names.values())[0])
    else:
        print("沒有")

func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安