with open("result16(1).txt", "r") as res_file:
    res = [int(val) for val in res_file.readlines()]
    
print(sum(res))