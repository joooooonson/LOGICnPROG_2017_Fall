# Author : Joon Son
# Date : 6/Nov/2017
# Loops & Lists Exercises


def loop_list_ex1(num):
    # 1
    # Write a while loop that prints
    # - All squares less than n. For example, if n is 100, print 0 1 4 9 16 25 36 49 64 81.
    # - All positive numbers that are divisible by 10 and less than n. For example, if n is 100, print 10 20
    # 30 40 50 60 70 80 90
    # - All powers of two less than n. For example, if n is 100, print 1 2 4 8 16 32 64.
    squares = []
    po_numbers = []
    powers = []
    for i in range(num):
        if i*i < num:
            squares.append(i*i)

        if i % 10 == 0:
            po_numbers.append(i)

        if 2**i < num:
            powers.append(2**i)
    print(squares)
    print(po_numbers)
    print(powers)


def loop_list_ex2(num_a, num_b, digits):
    # 2
    # Write a loop that computes
    # - The sum of all even numbers between 2 and 100 (inclusive).
    # - The sum of all squares between 1 and 100 (inclusive).
    # - The sum of all odd numbers between a and b (inclusive).
    # - The sum of all odd digits of n. (For example, if n is 32677, the sum would be 3 + 7 + 7 = 17.)
    even_numbers = []
    squares = []
    odd_numbers = []
    odd_digits = []

    for i in range(1, 101, 1):
        if i % 2 == 0:
            even_numbers.append(i)
        if i**2 <= 100:
            squares.append(i**2)
    for i in range(num_a, num_b+1, 1):
        if i % 2 != 0:
            odd_numbers.append(i)
    while digits == 0:              # 32677 3267 326 32 3 0
        num = digits % 10           # 7 7 6 2 3
        if num % 2 != 0:
            odd_digits.append(num)
        digits = int(digits/10)     # 3267 326 32 3 0

    print(sum(even_numbers))
    print(sum(squares))
    print(sum(odd_numbers))
    print(sum(odd_digits))


def loop_list_ex3():
    # 3
    # Rewrite the following for loop as a while loop.
    # s = 0
    # for i in range(1, 10) : s = s + i
    count = 1
    total = 0
    while count < 10:
        total += count
    print(total)


def loop_list_ex4():
    #  Write programs that read a sequence of integer inputs and print
    # - The smallest and largest of the inputs.
    # - The number of even and odd inputs.
    # - Cumulative totals. For example, if the input is 1 7 2 9, the program should print 1 8 10 19.
    # - All adjacent duplicates. For example, if the input is 1 3 3 4 5 5 6 6 6 2, the program should print 3 5 6.
    input_str = input("Please input a sequence of integers (quit to 'quit') :")
    int_inputs = []
    cumulative_tot = []
    duplicates = []
    while input_str.lower() != 'quit':
        try:
            input_int = int(input_str)
        except TypeError:
            print("**Error:please enter a integer value**")
        else:
            int_inputs.append(input_int)
        finally:
            input_str = input("Please input a sequence of integers (quit to 'quit') :")
    smallest = min(int_inputs)
    largest = max(int_inputs)
    even_cnt = 0
    odd_cnt = 0
    is_first = True
    prev = 0
    for int_input in int_inputs:
        if int_input % 2 == 0:
            even_cnt += 1
        else:
            odd_cnt += 1

        if is_first:
            is_first = False
        else:
            if int_input == prev and int_input not in duplicates:
                duplicates.append(int_input)
        prev = int_input

    print("\nThe smallest input : {}".format(smallest))
    print("The largest input : {}".format(largest))
    print("Cumulative Total : ", end="")
    for num in cumulative_tot:
        print(num, end=" ")
    print('\n')
    print("All adjacent duplicates : ", end="")
    for num in duplicates:
        print(num, end=" ")
    print('\n')

# run!!!
# 1
loop_list_ex1(100)
# 2
loop_list_ex2(3, 91, 32677)
# 3
loop_list_ex3()
# 4
loop_list_ex4()

