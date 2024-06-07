# def my_gen(x):
#     for i in range(x):
#         yield i 
# gen=my_gen(5)
# print(next(gen))
# print(next(gen))
# print(next(gen))  

# for j in (gen):
#     print(j)

# def csv_reader(file_name):
#     file = open(file_name)
#     result = file.read().split("\n")
#     return result

# read=csv_reader("4.txt")
# print(read) 

def infinite_sequence():
    num = 0
    while True:
        num += 1
        return num
gen = infinite_sequence()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
print(gen) 
print(gen)
print(gen) 
print(gen) 
