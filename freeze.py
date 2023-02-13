from flask_frozen import Freezer
from main import gen

freezer = Freezer(gen)

if __name__ == '__main__':
    freezer.freeze()