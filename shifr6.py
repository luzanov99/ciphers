def shifrovka(key,original_text):
    #Заповнення ключа до довжини шифрованого слова
    a=0
    while len(key)!=len(original_text):
        if a==0:
            key=key+key[0]
            a+=1
        if a==1:
            key=key+key[1]
            a+=1
        if a==2:
            key=key+key[2]
    key_word=list(key)

    #Заповнення таблиці шифрування номерами слів у таблиці символів
    text=list(original_text.lower())
    number=[]
    for element in text:
        number.append(ord(element))
    #Змінення позиції букви речення на відповідну довжину ключа
    for i in range(0,len(number)):
        if number[i]!=32:
            number[i]=number[i]+int(key_word[i])
    #Перетворення номерів на букви
    for j in range(0,len(number)):
        number[j]=chr(number[j])
    #Вивід результату
    result=''
    for k in range (0, len(number)):

        result+=number[k]
    print(result)
shifrovka("121","Лузанов Евгений Олександрович")