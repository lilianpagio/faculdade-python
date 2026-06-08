def border(s1):
    size = len(s1)
    if size:
        print('+', '-' * size, '+')
        print('|', s1, '|')
        print('+', '-' * size, '+')

border('Hello, world!')
border('Progamming Logic')