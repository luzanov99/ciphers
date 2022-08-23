def shifrovka(key_word,original_text):
  #Переклад слова до нижнього регістру
    key_word=key_word.lower()
 # Вилучення пробілів 
    original_text = ''.join(original_text.split(' ')).lower()
    # Визначення оптимальної довжини стовбчика 
    k = len(original_text) // len(key_word)
    #Створення першого масиву шифрувального слова
    shifr={}
    #Заповнення масиву вхідним реченням
    for index, ch in enumerate(key_word.lower()):
        if ch in shifr:
            shifr[ch] += original_text[index * k : index * k + k]
            
        else:
            shifr[ch] = original_text[index * k : index * k + k]
    
    list_keys1 = list(shifr.keys())
    list_keys1.sort()
 
   #Створення другого масиву для перетворень шифрування
    shifr2={}
    list_keys2_1=[]
    #шифрую масив за соруванням стовбчиків
    for a in list_keys1:
        shifr2[a]=list(shifr[a])
    #Перший стовбчик записую до одномірного масиву для обробки інших стовбчиків відповідно до першого
    keys2 = list(shifr2.keys())
    for g in shifr2[keys2[0]]:
        list_keys2_1.append(g)


    #В залежності від номеру букви першого стовбчика у абетці перетворення інших стовбчиків
    if  (list_keys2_1[0]< list_keys2_1[1])&(list_keys2_1[1]< list_keys2_1[2]):
        print(list_keys2_1[0])
    elif (list_keys2_1[0]> list_keys2_1[1])&(list_keys2_1[0]< list_keys2_1[2]):
        for key_one in list_keys1:
            tmp=shifr2[key_one][0]
            shifr2[key_one][0]=shifr2[key_one][1]
            shifr2[key_one][1]=tmp   
    elif (list_keys2_1[1]< list_keys2_1[0])&(list_keys2_1[1]<list_keys2_1[2]):
        for key_one in list_keys1:
            tmp=shifr2[key_one][0]
            shifr2[key_one][0]=shifr2[key_one][1]
            shifr2[key_one][1]=shifr2[key_one][2]
            shifr2[key_one][2]=tmp
    elif (list_keys2_1[2]< list_keys2_1[0])&(list_keys2_1[1]< list_keys2_1[0]):
        for key_one in list_keys1:
            tmp=shifr2[key_one][0]
            shifr2[key_one][0]=shifr2[key_one][2]
            shifr2[key_one][2]=tmp
    elif (list_keys2_1[2]< list_keys2_1[0])&(list_keys2_1[0]< list_keys2_1[1]):
        for key_one in list_keys1:
            tmp=shifr2[key_one][0]
            shifr2[key_one][0]=shifr2[key_one][2]
            shifr2[key_one][2]=shifr2[key_one][1]
            shifr2[key_one][1]=tmp
    #Вивід шифру
    
   
    for keys3 in shifr2.keys():
        print('Для ключа {} значення {}'.format(keys3, shifr2[keys3]))
        
 
shifrovka("безумство","Лузанов Евгений Олександрович")