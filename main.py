def pal_check(check_str):
    res = True
    # Сравниваем каждый символ с одинаковым порядковым номером с начала и конца. 
    # Когда найдено несовпадение изменяем res на False и прирываем цикл. Если несовпадений нет, res остаётся True
    for char in range(len(check_str)):
        if check_str[char] == check_str[-char - 1] and res == True:
            pass
        else:
            res = False
            break
        
    return res

# Строка палиндром.
ent_str = 'лепсспел'
print(ent_str, pal_check(ent_str))

# Строка не палиндром
ent_str = 'helloworld'
print(ent_str, pal_check(ent_str))