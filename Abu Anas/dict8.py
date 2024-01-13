original_data={
'Emma': {'name': 'Emma', 'major':
'Computer Science', 'cgpa': 3.8,
'completed_credits': 90},

'Daniel': {'name': 'Daniel', 'major':
'Electrical Engineering', 'cgpa': 3.5,
'completed_credits': 75},

'Sophia': {'name': 'Sophia', 'major':
'Mechanical Engineering', 'cgpa': 3.2,
'completed_credits': 60}
}
transformed_student_data={}
for key,value in original_data.items():
    new_dic={}
    for key1 in value.keys():
        if key1=="cgpa":
            new_dic["cgpa"]=value["cgpa"] 
        elif key1=="completed_credits":
            new_dic["completed_credits"]=value["completed_credits"]
    transformed_student_data[key]=new_dic
    print() 
print(transformed_student_data) 


