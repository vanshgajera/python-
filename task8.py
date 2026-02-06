def odd_number(number):

    list_odd = []

    for i in number:
        if i%2 == 1:
            list_odd.append(i)
    return list_odd


list = [1,2,3,4,5,6,7,8,9,10]

list_find = odd_number(list)

print(f"Odd number list is : {list_find}")
