lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_dic={} 
for i in lst:
    if i%2!=0:
        new_dic[i]=i**2
print(new_dic) 