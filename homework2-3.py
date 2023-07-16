def func(*data):
    middle_names = []
    full_names = []

    for name in data:
        middle_names.append(name[1])
        full_names.append(name)

    uniquename = False
    for i in range(len(middle_names)):
        unique_middle_names = True
        current_middle_name = middle_names[i]
        for j in range(len(middle_names)):
            if i != j:
                if middle_names[j] == current_middle_name:
                    unique_middle_names = False
                    break

        if unique_middle_names:
            uniquename = True
            print(full_names[i])

    if not uniquename:
        print("沒有")
        
func("彭⼤牆", "王明雅", "吳明") # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
