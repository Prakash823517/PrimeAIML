from hello  import chai
chai("ginger Tea")


import os
print(os.getcwd())


import hello
hello.chai("mint Tea")
print(hello.chai_one)

# when some parts of data does not loard 
from importlib import reload
reload(hello)
