# Author : Joon Son
# Date : 24/Oct/2017
# Description : Parsing String
# Allow user to enter a three word phrase.

# Check the input exactly three words, separated by spaces
# count() count(sub, start, end)
# isalpha(), find(str, beg, end))

sep = ' '  # separator space
err = -1


def get_input_string():
    in_str = input("Enter a three words phrase separated by space :")
    print(get_first_space_index(in_str))
    print(get_second_space_index(in_str))

    return in_str

# The full phrase, all in capital letters
# upper()


def my_upper(input_str):
    return input_str.upper()

# The full phrase, with each new word in the phrase capitalized
# title()


def my_title(input_str):
    return input_str.title()

# The first letter of the phrase


def first_letter(input_str):
    return input_str[0]

# The last letter of the phrase


def last_letter(input_str):
    return input_str[len(input_str)-1]

# The number of spaces in the phrase


def get_number_of_spaces(input_str):
    return input_str.count(sep, 0, len(input_str))

# The number of characters in the phrase


def get_number_of_char(input_str):
    return len(input_str) - get_number_of_spaces(input_str)


# The index location of the first space

def get_first_space_index(input_str):
    return input_str.find(sep)

# The index location of the last space


def get_second_space_index(input_str):
    first_index = get_first_space_index(input_str)
    sub_input = input_str[first_index+1:]
    second_index = sub_input.find(sep) + first_index + 1
    if second_index == first_index + 1:
        second_index = err
    return second_index

# The full first word only


def get_first_word(input_str):
    index = get_first_space_index(input_str)
    return input_str[:index]

# The full second word only


def get_second_word(input_str, index_2):
    index_1 = get_first_space_index(input_str)
    return input_str[index_1+1: index_2]

# The count of how many occurrences of the letter E are in the phrase (either upper or lower case)


def get_number_of_e(input_str):
    return input_str.lower().count('e', 0, len(input_str))

# The single character that is the max in alphabetical order


def get_max_in_alphaorder(input_str):
    input_str_lower = input_str.lower()
    max_char = 'a'

    if 'z' in input_str_lower:
        max_char = 'z'
    elif 'y' in input_str_lower:
        max_char = 'y'
    elif 'x' in input_str_lower:
        max_char = 'x'
    elif 'w' in input_str_lower:
        max_char = 'w'
    elif 'v' in input_str_lower:
        max_char = 'v'
    elif 'u' in input_str_lower:
        max_char = 'u'
    elif 't' in input_str_lower:
        max_char = 't'
    elif 's' in input_str_lower:
        max_char = 's'
    elif 'r' in input_str_lower:
        max_char = 'r'
    elif 'q' in input_str_lower:
        max_char = 'q'
    elif 'p' in input_str_lower:
        max_char = 'p'
    elif 'o' in input_str_lower:
        max_char = 'o'
    elif 'n' in input_str_lower:
        max_char = 'n'
    elif 'm' in input_str_lower:
        max_char = 'm'
    elif 'l' in input_str_lower:
        max_char = 'l'
    elif 'k' in input_str_lower:
        max_char = 'k'
    elif 'j' in input_str_lower:
        max_char = 'j'
    elif 'i' in input_str_lower:
        max_char = 'i'
    elif 'h' in input_str_lower:
        max_char = 'h'
    elif 'g' in input_str_lower:
        max_char = 'g'
    elif 'f' in input_str_lower:
        max_char = 'f'
    elif 'e' in input_str_lower:
        max_char = 'e'
    elif 'd' in input_str_lower:
        max_char = 'd'
    elif 'c' in input_str_lower:
        max_char = 'c'
    elif 'b' in input_str_lower:
        max_char = 'b'
    else:
        max_char = 'a'

    return max_char

# The full phrase, but with all spaces replaced by the underscore character( _ ).


def my_replace(input_str, new, old):
    return input_str.replace(old, new)


def input_validation(input_str):
    # when the input is consist of only characters
    # and has two separator(space)
    result = False
    if get_number_of_spaces(input_str) == 2:
        word_1 = get_first_word(input_str)
        index_2 = get_second_space_index(input_str)
        if index_2 == err:
            return result
        word_2 = get_second_word(input_str, index_2)
        word_3 = input_str[index_2+1:]

        if word_1.isalpha() and word_2.isalpha() and word_3.isalpha():
            result = True
    return result

# #########################################################################################
# start main logic
# #########################################################################################


input_string = get_input_string()

if input_validation(input_string):
    print(my_upper(input_string))
    print(my_title(input_string))
    print(first_letter(input_string))
    print(last_letter(input_string))
    print(get_number_of_spaces(input_string))
    print(get_number_of_char(input_string))
    print(get_first_space_index(input_string))
    print(get_second_space_index(input_string))
    print(get_first_word(input_string))
    print(get_second_word(input_string, get_second_space_index(input_string)))
    print(get_number_of_e(input_string))
    print(get_max_in_alphaorder(input_string))
    print(my_replace(input_string, '_', ' '))

else:
    print("validation failed!!!")
