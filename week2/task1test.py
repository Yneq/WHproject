def find_and_print(messages, current_station):
    if current_station not in greenLine and current_station != "Xiaobitan":
        return "No Station"

    # 设置当前站点索引
    

    min_distance = float("inf")
    nearest_friend = None

    # 创建朋友的站点索引字典
    
    for friend, friend_station in messages.items():
        if "Xiaobitan" in friend_station:
            # 特殊处理Xiaobitan站
            if current_station in ["Xindian City Hall", "Xindian"]:
                # 如果当前站点是Xindian City Hall或Xindian，则Xiaobitan索引为15.5
                station_index[friend] = 15.5
            else:
                # 其他情况Xiaobitan索引为16.5
                station_index[friend] = 16.5
        else:
            for station in greenLine:
                if station in friend_station:
                    station_index[friend] = greenLine.index(station)
                    break

    # 寻找最近的朋友
    for friend, station_idx in station_index.items():
        distance = abs(greenLine.index(current_station) - station_idx)
        # print(f"检查朋友：{friend}, 站点索引：{station_idx}, 距离：{distance}")
        
        if distance < min_distance:
            min_distance = distance
            nearest_friend = friend
            # print(f"最近的朋友是: {nearest_friend}")

    print(nearest_friend)
    return nearest_friend
# ...

# 调用 find_and_print 函数


# 测试代码



# 您的其他代码和数据...
# ...


# 您的其他代码和数据...






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
# # index_station["17.5"] = "Xiaobitan"
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





