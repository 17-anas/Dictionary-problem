lst1=["Black","Red","Maroon","Yellow"] 
lst2=["#000000", "#FF0000", "#800000","#FFFF00"]
new_list=[]
for i in range(0,len(lst1)):
    new_dic={}
    for j in range(0,i+1):
        new_dic["color_name"]=(lst1[i]) 
        new_dic["color_code"]=(lst2[j])  
    new_list.append(new_dic)
print(new_list)