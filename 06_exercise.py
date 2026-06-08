def string_value (question, min, max):
    s1 = input(question)
    size = len(s1)
    while size < min or size > max:
        s1 = input(question)
        size = len(s1)
    return s1

x = string_value('Enter a string: ', 10, 30)
print('You wrote the string:{}.\nInvalid input.\nExiting program...'.format(x))