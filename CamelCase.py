'''
Question Description:
Camel Case is a naming style common in many programming languages. In Java, method and variable names typically start with a lowercase letter, with all subsequent words starting with a capital letter (example: startThread). Names of classes follow the same pattern, except that they start with a capital letter (example: BlueCar).

Your task is to write a program that creates or splits Camel Case variable, method, and class names.

- Input Format

Each line of the input file will begin with an operation (S or C) followed by a semi-colon followed by M, C, or V followed by a semi-colon followed by the words you'll need to operate on.
The operation will either be S (split) or C (combine)
M indicates method, C indicates class, and V indicates variable
In the case of a split operation, the words will be a camel case method, class or variable name that you need to split into a space-delimited list of words starting with a lowercase letter.
In the case of a combine operation, the words will be a space-delimited list of words starting with lowercase letters that you need to combine into the appropriate camel case String. Methods should end with an empty set of parentheses to differentiate them from variable names.

- Output Format

For each input line, your program should print either the space-delimited list of words (in the case of a split operation) or the appropriate camel case string (in the case of a combine operation).
'''

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
