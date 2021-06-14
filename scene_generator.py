import json
from pathlib import Path

thing_types = ['leave', 'characters', 'nouns', 'operators', 'properties']
thing_type_msg = '''
Choose a generate thing type
(1) characters
(2) nouns
(3) operators
(4) properties
(0) end
> '''
thing_setup_msg = '''
[x y] => create object at (x, y)
[x1 x2 y1 y2] => create object from (x1, y1) to (x2, y2)
Press Enter to stop input
'''


def get_titles():
    # input id
    id = input('Input scene setup id: ')
    while id == '':
        id = input('Input scene setup id: ')

    # input name
    name = input('Input scene setup name: ')
    while name == '':
        name = input('Input scene setup name: ')

    return id, name


def get_size():
    # input width
    width = input('Input scene setup width: ')
    while not width.isdecimal():
        width = input('Input scene setup width: ')

    # input height
    height = input('Input scene setup height: ')
    while not width.isdecimal():
        height = input('Input scene setup height: ')

    return width, height


def get_thing_name(type_index):
    if not type_index in range(1, 5):
        return None

    thing_name = input('Input object name: ')
    while not thing_name.isalpha():
        thing_name = input('Input object name: ')

    thing_name = thing_name.upper()
    if type_index != 1:
        thing_name = 'Text_' + thing_name

    return thing_name


def get_thing_setup(name, pos):
    setups = []
    if len(pos) < 2 or len(pos) > 4:
        return setups

    x1, x2, y1, y2 = 0, 0, 0, 0
    if len(pos) == 4:
        x1, x2, y1, y2 = pos[0], pos[1], pos[2], pos[3]
    elif len(pos) >= 2:
        x1, x2 = pos[0], pos[0]
        y1, y2 = pos[1], pos[1]
    elif len(pos) == 1:
        print('Input at least 2 numbers!')
        return setups
    else:
        print('Invalid input size')
        return setups

    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1

    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            setups.append({
                'defaultBlockX': x,
                'defaultBlockY': y,
                'defaultTowards': 0,
                'textureName': name
            })
    return setups


def get_ranges(thing_name, type_index, object):
    print('[ ' + thing_types[type_index] + ', ' + object + ' ]')

    thing_setup = []
    while True:
        flag = True
        pos_range = input('Input range: ')
        if pos_range == '':
            break

        pos_range = pos_range.split(' ')
        for i, x in enumerate(pos_range):
            if not x.isdecimal():
                print('Input numbers!')
                flag = False
                break
            pos_range[i] = int(x)

        if not flag:
            continue

        setups = get_thing_setup(thing_name, pos_range)
        for setup in setups:
            thing_setup.append(setup)

    return thing_setup


def main():
    show_message = True
    print('Scene Setup Generator')

    # get basic data
    id, name = get_titles()
    width, height = get_size()
    things_map = []

    # input things
    while True:
        print('\n------------------------')

        # get thing type
        type_index_str = input(thing_type_msg)
        while not type_index_str.isdigit():
            type_index_str = input(thing_type_msg)

        type_index = int(type_index_str)
        if not type_index in range(1, 5):
            break

        thing_species = thing_types[type_index]
        thing_name = get_thing_name(type_index)

        if show_message:
            print(thing_setup_msg)
            stop_showing = input('Stop showing input instructions? (y/N) ')
            if stop_showing == 'Y' or stop_showing == 'y':
                show_message = False
        thing_setup = get_ranges(thing_name, type_index, thing_name)

        thing = {
            'species': thing_species,
            'name': thing_name,
            'thingSetup': thing_setup
        }

        things_map.append(thing)

    print('\nGenerating scene setup...\n')

    setup = {
        'id': id,
        'name': name,
        'sceneWidth': width,
        'sceneHeight': height,
        'thingsMap': things_map
    }

    filePath = './setups/' + id + '.json'
    with open(filePath, 'w', encoding='utf-8') as f:
        json.dump(setup, f, ensure_ascii=False, indent=2)

    print('Scene setup file created at ' + filePath + '.')


if __name__ == '__main__':
    main()
