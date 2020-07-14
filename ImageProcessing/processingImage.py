from PIL import Image
from os import chdir, path, getcwd

def main():
    # Get the directory of this script.
    dirPath = path.dirname(path.realpath(__file__))
    chdir(dirPath)

    im = Image.open('lotus.png')
    im.show()

if __name__ == '__main__':
    main()