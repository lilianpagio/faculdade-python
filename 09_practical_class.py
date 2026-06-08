def val_int(question, min, max):
    x = int(input(question))
    while (x < min or x > max ):
        x = int(input(question))
    return x

def file_exists(file_name):
    try:
        a= open(file_name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def create_file (file_name):
    try:
        a = open(file_name, 'wt+')
        a.close()
    except:
        print('Error creating file.')
    else:
        print(f'File {file_name} created successfully.')

def register_game (file_name, game_name, videogame_name):
    try:
        a = open(file_name, 'at')
    except: 
        print('Error opening file.')
    else:
        a.write(f'{game_name};{videogame_name}\n')
        a.close()

def list_files (file_name):
    try:
        a = open(file_name, 'rt')
    except:
        print('Error reading file.')
    else:
        print(a.read())
    finally:
        a.close()

#main program
file = 'games.txt'
if file_exists(file):
    print('File located on computer.')
else:
    print('File not found.')
    create_file (file)  

while True:
    print('MENU')
    print('1 - Add new item')
    print('2 - View registered items')
    print('3 - Exit')

    op = val_int('Select an option: ', 1, 3)

    if op == 1: #add new item
        print('Add new item selected\n')
        game_name = input('Game name: ')
        videogame_name = input('Videogame name: ')
        register_game(file, game_name, videogame_name)

    elif op == 2: #view registered items
        print('View regitered items selected...\n')
        list_files(file)

    elif op == 3: #exit
        print('Exiting...')
        break