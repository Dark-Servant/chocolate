import sys
import pathlib

# иначе не подключатся модули указанные ниже
sys.path.append(str(pathlib.Path(__file__).parent.resolve()))

from mass import *
from impurity import *

sys.path.pop()