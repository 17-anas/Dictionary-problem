num = int(input())
new_dict = {}

for i in range(2, num + 1):
    if i < 2:
        prime = False
    else:
        prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                prime = False
                break

    if  prime:
        new_list = []
        power = 2
        while i**power < 100:
            if power % 2 != 0:
                new_list.append(i**power)
            power += 1

        if new_list:
            new_dict[i] = new_list

print(new_dict)