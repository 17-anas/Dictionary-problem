# import another_module
# print(another_module.another_module) 
import copy
lsta=[1,[40,80],4]
lstb=copy.deepcopy(lsta)
lstb[0]=3 
print(lsta)
print(lstb)