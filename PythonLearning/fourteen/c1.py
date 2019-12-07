
#switch

# switch (day)

##字典映射 代替switch case 语句

day = 0
switcher = {
    0:"Sunday",
    1:"Monday",
    2:"Tuesday"
}

# day_name = switcher[day]
day_name = switcher.get(day,"Unknown")  ## "Unknown"为key非法时候的返回.
print(day_name)

print(switcher.get(55,"qwer"))

def getSunday():
    return "sunday"
def getMonday():
    return "Monday"
def getTuesday():
    return "Tuesday"
def getDefault():
    return "Unknown"
switcher1 = {
    0:getSunday(),
    1:getMonday(),
    2:getTuesday()
}
day = 35
dadaa = switcher.get(day,getDefault)()  ##这样处理在getSunday里可以写很多代码和逻辑.
print(dadaa)

