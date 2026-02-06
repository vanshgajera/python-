def find_even_number(number):
    even_number = []

    for i in number:
        if i % 2 == 0:
            even_number.append(i)
    return even_number


list = [1,2,3,4,5,6,7,8,9,10]

even_list = find_even_number(list)
print(f"The even number list is : {even_list}")
