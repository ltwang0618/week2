def get_number(index):
    value = 0
    increment = 0

    for i in range(index+1):
        if i % 2 == 0:
            increment = 0
        else:
            increment = 2.5
        value = increment + (i / 2) * 3

    print(round(value))

get_number(1) # print 4
get_number(5) # print 10
get_number(10) # print 15