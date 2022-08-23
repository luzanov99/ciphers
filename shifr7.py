# Функція Створення словарю символів для шифрування
def form_dict():
    d = {}
    iter = 0
    for i in range(0,127):
        d[iter] = chr(i)
        iter = iter +1
    return d
# Перетворення букв у слові на номера таблиці символів
def encode_val(word):
    list_code = []
    lent = len(word)
    d = form_dict() 

    for w in range(lent):
        for value in d:
            if word[w] == d[value]:
               list_code.append(value) 
    return list_code
# Допоміжна функція для отримання значень речення шифрування та ключа
def comparator(value, key):
    len_key = len(key)
    dic = {}
    iter = 0
    full = 0

    for i in value:
        dic[full] = [i,key[iter]]
        full = full + 1
        iter = iter +1
        if (iter >= len_key):
            iter = 0 
    return dic 
#Функція кодування слова за ключем
def full_encode(value, key):
    dic = comparator(value, key)
    lis = []
    d = form_dict()

    for v in dic:
        go = (dic[v][0]+dic[v][1]) % len(d)
        lis.append(go) 
    return lis
#Функція дешифровки закодованого речення
def decode_val(list_in):
    list_code = []
    lent = len(list_in)
    d = form_dict() 
    for i in range(lent):
        for value in d:
            if list_in[i] == value:
               list_code.append(d[value]) 
    return list_code

if __name__ == "__main__":

    word = 'Luzanov Yevgen'
    key = 'key'
    
    print ('Слово: '+ word)
    print ('Ключ: '+ key)

    key_encoded = encode_val(key)
    value_encoded = encode_val(word)
    shifre = full_encode(value_encoded, key_encoded)
    result=decode_val(shifre)
    print ('Word=',''.join(result))


