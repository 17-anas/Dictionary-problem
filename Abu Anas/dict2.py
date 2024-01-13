lst=[{'item': 'item1', 'amount': 400},
{'item': 'item2', 'amount': 300},
{'item': 'item1', 'amount': 750}]
new_dic={}
for i in range(0,len(lst)):
    if (lst[i]["item"])=="item1":
        sum1=(lst[i]["amount"])+(lst[i]['amount']) 
    elif lst[i]["item"]=="item2":
        sum2=(lst[i]['amount'])
new_dic["item1"]=sum1
new_dic['item2']=sum2    
print(new_dic) 