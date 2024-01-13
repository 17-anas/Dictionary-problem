sample_dict = {
"name": "Kelly",
"age": 25,
"salary": 8000,
"city": "New york"}
new_dic={}
for i in sample_dict.keys():
    if i =="name":
        new_dic["name"]=sample_dict["name"]
    elif i =="salary":
        new_dic["salary"]=sample_dict["salary"]
print(new_dic)
