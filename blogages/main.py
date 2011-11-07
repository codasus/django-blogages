from os.path import abspath, dirname, join
from sys import path

# add libs to search directories
path.insert(0, join(dirname(abspath(__file__)), 'libs'))

# do djangoappengine.main stuff
from djangoappengine.main.application import main

if __name__ == '__main__':
    main()
