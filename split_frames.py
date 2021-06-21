from PIL import Image
import os

types = ['characters', 'nouns', 'operators', 'properties']


def get_name_from_file(file):
    return file.split('0')[0][:-1]


def iter_frames(img):
    try:
        i = 0
        while 1:
            img.seek(i)
            imframe = img.copy()
            if i == 0:
                palette = imframe.getpalette()
            else:
                imframe.putpalette(palette)
            yield imframe
            i += 1
    except EOFError:
        pass


def generate_frames(type):
    load_dir = './gif/' + type
    files = os.listdir(load_dir)
    for file in files:
        name = get_name_from_file(file)

        load_path = load_dir + '/' + file
        gif = Image.open(load_path)

        save_dir = './png/' + type + '/' + name

        try:
            os.mkdir(save_dir)
            for i, frame in enumerate(iter_frames(gif)):
                filename = name + '_' + str(i) + '.png'
                frame.save(save_dir + '/' + filename, **frame.info)
            print('Frames created for ' + type + ' ' + name)
        except:
            print('Ignore process for ' + type + ' ' + name)


def main():
    for type in types:
        select = input(
            'Do you want to generate split frames for ' + type + '? (Y/n) ')
        if select == 'N' or select == 'n':
            continue

        print('Generating frames of ' + type + '...')
        generate_frames(type)
        print('Frames of ' + type + ' are generated in ./png/'+type+'.')

    print('Process finished.')


if __name__ == '__main__':
    main()
