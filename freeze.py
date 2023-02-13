from flask_frozen import Freezer
from gen import app

freezer = Freezer(gen)

if __name__ == '__main__':
    freezer.freeze()
