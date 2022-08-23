def shifrovka(key_word,original_text):

    key_word=key_word.lower()
    original_text = ''.join(original_text.split(' ')).lower()
    k = len(original_text) // len(key_word)
    
    shifr={}

    for index, ch in enumerate(key_word.lower()):
        if ch in shifr:
            shifr[ch] += original_text[index * k : index * k + k]
            
        else:
            shifr[ch] = original_text[index * k : index * k + k]
    list_keys = list(shifr.keys())
    list_keys.sort()
    for i in list_keys:
        print(i, ':', shifr[i])
 
shifrovka("безумство","Лузанов Евгений Олександрович")