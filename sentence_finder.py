with open(r'file-dir', 'r', encoding='utf-8') as file:
    text = file.read()
    sentences = [] #Напишите предложения, слова, которые вы хотите найти

    for i, sentences in enumerate(sentences, 1):
        if sentences.lower() in text.lower():
            print(f'{i}. Предложение найдено')
        else:
            print(f'{i}. Предложение не найдено')



