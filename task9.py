def prime_number(number):

    prime = []

    for i in number:
        if i < 2:
            print(f"NO Prime Numeber")
            continue
        
        is_prime = True
    
        for j in range(2,i):
            if i % j == 0:
                is_prime = False
                break
        
        if is_prime:
            prime.append(i)
            
    return prime


list = []
list_size = int(input("Enter the size of list: "))

for i in range(list_size):
    check = int(input("Enter the element: "))
    list.append(check)

pri = prime_number(list)

print(f"The prime number list is : {pri}")

