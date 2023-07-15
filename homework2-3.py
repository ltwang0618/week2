def func(*data):
    middlenames = []
    fullnames = []

    for name in data:
        middlenames.append(name[1])
        fullnames.append(name)

    for name1 in data:
        middlenamecounts = {}
        for name1 in middlenames:
            middlenamecounts[name1] = 0

        for name1 in middlenames:
            middlenamecounts[name1]+=1 

        uniquemiddlenames = {}
        for name1 in middle_name_counts:
            if middlenamecounts[name1] == 1:
                uniquemiddlenames.append(name1)
        
        if len(uniquemiddlenames) > 0:
            for name1 in uniquemiddlenames:
                for name in fullnames:
                    if name1 == name[1]:
                        print(name)
        else:
            print("沒有")

    func("彭⼤牆", "王明雅", "吳明") # print 彭⼤牆
    func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
    func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
