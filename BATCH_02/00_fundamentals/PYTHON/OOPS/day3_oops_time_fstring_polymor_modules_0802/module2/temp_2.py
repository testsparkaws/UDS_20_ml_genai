
## As we have imort caclutor, hello_world() in __init__.py , so we dont have to mentioned 
## the filename(calc.py)

from utils import Calulcator
from utils import hello_world

c = Calulcator()

answer_1 = c.add(1,2,3,4,5,6,7,9,10)
print(answer_1)

answer_1 = c.add(1,2,3,4,5,6,7,8,9,10)
print(answer_1)

answer_2 = c.add(1,2)
print(answer_2)

c.get_history()

hello_world()
