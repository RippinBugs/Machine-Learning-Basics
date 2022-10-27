"""
#import a whole modult
#import file_name as something(which will work as an alias).
import pizza as p
#one can easily call the function available to this module by using the following syntax
#module_name.function_name()
#or 
#modules_alias_name.function_name()
p.make_pizza(12,'fries','tomato','spinach','pineapple')
"""

#importing specific functions from a module
#from module_name import function_name as fn
from pizza import make_pizza as mp
mp(12,'fries','tomato','spinach','pineapple')


#importing all the functions from a module
#from pizza import *