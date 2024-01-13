company_hr_register = {
101: {'name': 'Alice', 'age': 35,
'performance': 90, 'salary': 50000},
102: {'name': 'Bob', 'age': 58,
'performance': 98, 'salary': 70000},
103: {'name': 'Charlie', 'age': 45,
'performance': 85, 'salary': 60000},
104: {'name': 'David', 'age': 60,
'performance': 75, 'salary': 55000},
105: {'name': 'Eve', 'age': 28,
'performance': 92, 'salary': 48000},
106: {'name': 'Frank', 'age': 50,
'performance': 55, 'salary': 52000},
107: {'name': 'Grace', 'age': 62,
'performance': 97, 'salary': 75000},
}
updated_company_hr_register ={}
total_bonus_amount=0 
for key ,value in company_hr_register.items():
    if value["age"]>=55:
        total_bonus_amount+=10000
    if value["performance"]>=95:
        total_bonus_amount+=5000
    if value["performance"]>=60:
        new_dict={}
        new_dict["name"]=value["name"] 
        updated_company_hr_register[key]=new_dict 
print(len(updated_company_hr_register))
print(total_bonus_amount) 
print(updated_company_hr_register)