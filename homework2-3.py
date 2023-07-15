def func(*data):
    middle_names = []
    full_names = []

    for name in data:
        middle_name_counts = {}
        for name1 in middle_names:
            middle_name_counts[name1] = 0
        for name1 in middle_names:
            middle_name_counts[name1]+=1 

        unique_middle_names = {}
        for name1 in middle_name_counts:
            if middle_name_counts[name1] == 1:
                unique_middle_names.append(name1)
        
        if len(unique_middle_names) > 0:
            for name1 in unique_middle_names:
                for name in full_names:
                    if name1 == name[1]:
                        print(name)
                    else:
                        print("沒有")

    func("彭⼤牆", "王明雅", "吳明") # print 彭⼤牆
    func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
    func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有