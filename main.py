def pal_check(check_str):
    res = True
    check_str = list(check_str)
    for char in range(len(check_str)):
        if check_str[char] == check_str[-char - 1] and res == True:
            pass
        else:
            res = False
            break
        
    return res

ent_str = 'лепсспел'
print(pal_check(ent_str))