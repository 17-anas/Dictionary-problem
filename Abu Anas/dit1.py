new_dic={'Math':81, 'Physics':83,'Chemistry':87}  
dic={}       
v=list(new_dic.values())

maximum_value=max(v) 
for i in new_dic.keys():
    maximum_value=max(v) 
    if new_dic[i]==maximum_value:
        dic[i]=maximum_value
        v.remove(maximum_value)
          
print(dic)    
k=list(new_dic.keys())