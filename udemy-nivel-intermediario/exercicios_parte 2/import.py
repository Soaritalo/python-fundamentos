import importlib
import sys , os 
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import exercicios.ex_01_list_compreension
import sys
print(sys.platform)
platform = 'A minha'
print(platform)
for i in range(10):
    importlib.reload(exercicios.ex_01_list_compreension)
    print(i)
print('fim')