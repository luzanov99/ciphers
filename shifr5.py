def shifrovka(original_text):
    #Функція приймає текст шифрування 
    text=list(original_text.lower())
    number=[]
    #Кожна буква перетворюється на номер у таблиці символів
    for element in text:
        number.append(ord(element))
  
    #До номеру букви додається +2, щоб виконати переміщення до іншої букві у абетці
    for i in range(0,len(number)):
        if number[i]!=32:
            number[i]=number[i]+2
    #Номера перетворюється на значення букв у таблиці за цими номерами
    for j in range(0,len(number)):
        number[j]=chr(number[j])
    #Вивід результату
    result=''
    for k in range (0, len(number)):

        result+=number[k]
    print(result)
 

shifrovka("Лузанов Евгений Олександрович")