def find_and_print(messages, current_station):
    if current_station not in greenLine and current_station != "Xiaobitan":
        return "No Station"

    min_distance = float("inf")
    nearest_friend = None

    friend_stations = {}
    for friend, friend_station in messages.items():
        if "Xiaobitan" in friend_station:
            if current_station in ["Xindian City Hall", "Xindian"]:                
                friend_stations[friend] = 15.5
            else:
                friend_stations[friend] = 16.5 #其它情形正常作運算
        else:
            for station in greenLine:
                if station in friend_station:
                    friend_stations[friend] = greenLine.index(station)
                    break

    # 寻找最近的朋友
    for friend, station_idx in friend_stations.items():
        distance = abs(greenLine.index(current_station) - station_idx)
        if distance < min_distance:
            min_distance = distance
            nearest_friend = friend

    print(nearest_friend)
    return nearest_friend




    # location={"Leslie":"Xiaobitan","Bob":"Ximen","Mary":"Jingmei","Copper":"Taipei Arena","Vivian":"Xindian"}
greenLine=["Songshan","Nanjing Sanmin","Taipei Arena","Nanjing Fuxing","Songjiang Nanjing","Zhongshan", 
               "Beimen","Ximen","Xiaonanmen","Chiang Kai-shek Memorial Hall","Guting","Taipower Building",
                "Gongguan","Wanlong","Jingmei","Dapinglin","Qizhang","Xindian City Hall","Xindian"]

station_index = {}
index_station = {}

for i in range(len(greenLine)):
    station_index[greenLine[i]] = i
    index_station[i] = greenLine[i]

# station_index["Xiaobitan"] = "17.5"
# index_station["17.5"] = "Xiaobitan"
# branch_stations = {
#     "Qizhang": "Xiaobitan"
# }

# # 站點索引的字典，包括主線和分支
# station_index = {station: idx for idx, station in enumerate(greenLine)}
# # 添加分支站點的索引，這裡將分支站點視為與主線站點相鄰
# station_index[branch_stations["Qizhang"]] = station_index["Qizhang"] + 0.5

# # 反向索引的字典，僅限主線路，因為分支可能不在一個簡單的線性序列上
# index_station = {idx: station for idx, station in enumerate(greenLine)}



messages={
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Vivian":"I'm at Xindian station waiting for you."
}

find_and_print(messages, "Wanlong") # print Mary 
find_and_print(messages, "Songshan") # print Copper 
find_and_print(messages, "Qizhang") # print Leslie 
find_and_print(messages, "Ximen") # print Bob 
find_and_print(messages, "Xindian City Hall") # print Vivian


print("==============================")


bookings={}
def available(consultant_name, hour, duration):
    if consultant_name in bookings:
        for start, end in bookings[consultant_name]:
            if not (hour >= end or (hour+duration) <= start):
                return False
    return True
    

def book(consultants, hour, duration, criteria):
    best_consultant = None
    best_value = float("inf") if criteria == "price" else 0
    for consultant in consultants:
        if available(consultant["name"], hour, duration):
            if consultant["price"] < best_value:
                best_consultant = consultant["name"]
                best_value = consultant["price"]
            elif consultant["rate"] > best_value:
                best_consultant = consultant["name"]
                best_value = consultant["rate"]
    if best_consultant:                    
        if best_consultant not in bookings:
            bookings[best_consultant] = []
        bookings[best_consultant].append((hour, hour + duration))
        return best_consultant
    else:
        return "No Service"

consultants=[
{"name":"John", "rate":4.5, "price":1000},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800}
]

print(book(consultants, 15, 1, "price")) # Jenny 
print(book(consultants, 11, 2, "price")) # Jenny 
print(book(consultants, 10, 2, "price")) # John 
print(book(consultants, 20, 2, "rate"))# John 
print(book(consultants, 11, 1, "rate"))# Bob 
print(book(consultants, 11, 2, "rate"))# No Service 
print(book(consultants, 14, 3, "price")) # John


print("==============================")


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



print("==============================")


def get_number(index, numblist=[]):
    if not numblist:
        numblist.append(0)

    while len(numblist) <= index:
        if len(numblist) %3 == 0:
            nextnumb = numblist[-1] -1
        else: 
            nextnumb = numblist[-1] +4
        numblist.append(nextnumb)
    print(numblist[index])    
    return numblist[index]
    



get_number(1) # print 4
get_number(5) # print 15 
get_number(10) # print 25
get_number(30) # print 70




