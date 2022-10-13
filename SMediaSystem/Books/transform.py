def TransformToRu(incorrect_string: str) -> str:
        arr_ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я']
        arr_ru_incorrect = ['f', ',', 'd', 'u', 'l', 't', '`', ';', 'p', 'b', 'q', 'r', 'k', 'v', 'y', 'j', 'g', 'h', 'c', 'n', 'e', 'a', '[', 'w', 'x', 'i', 'o', 'm', 's', ']', "'", '.', 'z']
        also_symbols_incorrect = ['{', '}', ':', '"', '<', '>', '~']
        also_symbols = ['х', 'ъ', 'ж', 'э', 'б', 'ю', 'ё']
        incorrect_string = incorrect_string.lower()

        incorrect_string = incorrect_string.split()

        correct_string = []
        for word in incorrect_string:
                word_list = list(word)
                for i, letter in enumerate(word_list):
                        if letter in arr_ru_incorrect:
                        
                                letter_index = arr_ru_incorrect.index(letter)
                                correct_string.append(arr_ru[letter_index])
                        elif letter in also_symbols_incorrect:
                                
                                letter_index = also_symbols_incorrect.index(letter)
                                correct_string.append(also_symbols[letter_index])

                        else:
                                correct_string.append(letter)
                
        
        return ''.join(correct_string)



def TransformToEn(incorrect_string: str) -> str:
        arr_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        arr_en_incorrect = ['ф', 'и', 'с', 'в', 'у', 'а', 'п', 'р', 'ш', 'о', 'л', 'д', 'ь', 'т', 'щ', 'з', 'й', 'к', 'ы', 'е', 'г', 'м', 'ц', 'ч', 'н', 'я']

        incorrect_string.lower()

        incorrect_string.split()

        correct_string = []
        for word in incorrect_string:
                word_list = list(word)
                for i, letter in enumerate(word_list):
                        if letter in arr_en_incorrect:
                        
                                letter_index = arr_en_incorrect.index(letter)
                                
                                word_list[i] = arr_en[letter_index]
                                correct_string.append(arr_en[letter_index])

                        else:
                                correct_string.append(letter)
                
        
        return ''.join(correct_string)