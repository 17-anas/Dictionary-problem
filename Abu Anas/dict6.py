sam_input="the quick brown fox jumps over the lazy dog the lazy dog barks"
lst=list(sam_input.split(" "))
new_dic={} 
for i in lst:
    if i in new_dic:
        new_dic[i]+=1
    else:
        new_dic[i]=1  
print(new_dic) 
