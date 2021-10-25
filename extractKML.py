import re


# 从所给的kml文件中提取坐标列表
# 所获数据是一个字符串数组,每一行坐标是一个元素

def extract(raw_data):
    coordinates = re.findall(r'<coordinates>[\s\S]*</coordinates>', raw_data)
    # print(str(coordinates[0]))
    return str(coordinates[0]).split("\n")[1:][:-1]


if __name__ == '__main__':
    # 从文件 in.kml 中读取
    f = open('in.kml', 'r')
    cos = extract(f.read())
    for s in cos:
        print(s)
