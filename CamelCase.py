def split_camel_case(identifier):
    words = []
    start = 0
    for i in range(1, len(identifier)):
        if identifier[i].isupper():
            words.append(identifier[start:i].lower())
            start = i
    
    last_word = identifier[start:].lower()
    if last_word.endswith('()'):
        last_word = last_word[:-2]
    words.append(last_word)
    
    return words

def combine_words(words, type):
    if type == 'M':
        return words[0].lower() + ''.join(word.capitalize() for word in words[1:]) + '()'
    elif type == 'C':
        return ''.join(word.capitalize() for word in words)
    elif type == 'V':
        return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

while True:
    try:
        line = input().strip()
        operation, type_, name = line.split(';')
        words = name.split()
        result = ""

        if operation == 'S':
            res_list = split_camel_case(words[0])

            for i in range(len(res_list[:-1])):
                result += res_list[i] + " "
            result += res_list[-1]
       
        else:
            result = combine_words(words, type_)
            
        print(result)
    except EOFError:
        break
