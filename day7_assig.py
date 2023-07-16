# WAP to display only the odd numbers from 0 to 20 using range()

odd_num = range(20)

for i in odd_num:
    if i%2 != 0:
        print(i)


# WAP to display only the even numbers from 0 to 20 using range()

even_num = range(21)

for i in even_num:
    if i%2 == 0:
        print(i)


#WAP to display the numbers from 10 to 1 in descending order using range()

for i in reversed(range(1,11)):
    print(i)