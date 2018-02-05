# list practice
# author : Joon Son
# date : 30/Oct/2017

# 1. Using a list of integers, build a function called FirstOrLast7 which returns True if a 7 appears
# as either the first or last element in the list. The list will be length 1 or more.


def FirstOrLast7(my_list):
    result = False
    if my_list[0] == 7 or my_list[len(my_list)-1] == 7:
        result = True
    return result

# 2. Given a list of 3 integers, return a new list with the elements in reverse order,
# so [1, 2, 3] becomes [3, 2, 1].


def ReverseIt(my_list):
    my_list.reverse()
    return my_list


# Given 2 lists of integers, each with a length of 3, return a new list (length of 2)
# containing their middle elements.


def MiddleElements(first_list, second_list):
    result = []
    result.append(first_list[1])
    result.append(second_list[1])

    return result

# test FirstOrLast7
sample_list = [1, 3, 7]
print(FirstOrLast7(sample_list))
sample_list = [7, 8, 2, 4]
print(FirstOrLast7(sample_list))
sample_list = [13, 7, 1, 5, 9]
print(FirstOrLast7(sample_list))

# test ReverseIt

print(ReverseIt([1, 2, 3]))
print(ReverseIt([5, 11, 9]))
print(ReverseIt([7, 0, 0]))


# test MiddleElements

print(MiddleElements([1, 2, 3], [4, 5, 6]))
print(MiddleElements ([7, 7, 7], [3, 8, 0]))
print(MiddleElements ([5, 2, 9], [1, 4, 5]))
