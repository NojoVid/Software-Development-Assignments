## Encrypt the two hidden email adresses

email_1 = 'rdUYjcfruqjUYrfnqAYrfnqPYhtr'
email_2 = 'otmsPYitjAYrfnqUYzxPYhtr'

def caeser_cypher(text):
    
    letters_low = list("abcdefghijklmnopqrstuvwxyz")
    result = ''

    for item in text:
        if item.islower():
            index = letters_low.index(item)
            result += letters_low[index - 5]
        else:
            if item == 'P':
                result += '.'
            elif item == 'U':
                result += '_'
            elif item == 'A':
                result += '@'
            else:
                pass

    return result

print('-' * len(email_1))
print(caeser_cypher(email_1))
print(caeser_cypher(email_2))
print('-' * len(email_1))

