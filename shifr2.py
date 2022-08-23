#Функція приймає значення тексту що потрібно зашифрувати
def shifrovka(original_text):
    original_text=original_text.replace(' ','')
    #Створюється три рядки для заповнення шифрованого слова
    first_array=[]
    second_array=[]
    third_array=[]
    a=0
    #В кожний рядок записується символ строки та працює лічильник
    for element in original_text:
        if a==0:
            first_array.append(element)
            a+=1
        elif a==1:
            second_array.append(element)
            a+=1
        else :
            third_array.append(element)
            a=0
    # Вивід шифрованого речення  
    print(first_array)
    print("")
    print(second_array)
    print("")
    print(third_array)
    print("")

shifrovka("Лузанов Евгений Олександрович")