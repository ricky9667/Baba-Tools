import json

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
Input range in this format:
\'start_x start_y end_x end_y\'
1 3 3 5 => creates objects in square of (1,3) and (3,5)
All inputs should be numbers, input \'ok\' to finish position input
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
        return None

    start_x, start_y = pos[0], pos[1]
    end_x, end_y = pos[0], pos[1]
    if len(pos) == 4:
        end_x, end_y = pos[2], pos[3]

    for x in range(start_x, end_x+1):
        for y in range(start_y, end_y+1):
            setups.append({
                'defaultBlockX': x,
                'defaultBlockY': y,
                'defaultTowards': 0,
                'textureName': name
            })
    return setups


def main():
    print('Scene Setup Generator')

    # get basic data
    id, name = get_titles()
    width, height = get_size()
    things_map = []

    # input things
    while True:
        # get thing type
        type_index = int(input(thing_type_msg))

        if not type_index in range(1, 5):
            break
        thing_species = thing_types[type_index]
        thing_name = get_thing_name(type_index)

        thing_setup = []
        print(thing_setup_msg)

        while True:
            pos_range = input('Input range: ')
            if pos_range == 'ok':
                break
            pos_range = pos_range.split(' ')
            pos_range = [int(i) for i in pos_range]

            setups = get_thing_setup(thing_name, pos_range)
            for setup in setups:
                thing_setup.append(setup)

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

    filename = id + '.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(setup, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
