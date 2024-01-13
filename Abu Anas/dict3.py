string='w3resource' 
new_dic={}
for i in string:
    if i in new_dic:
        new_dic[i]+=1
    else:
        new_dic[i]=1
print(new_dic) 
