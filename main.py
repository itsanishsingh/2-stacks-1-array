from constants import *


def main():
    length_of_array = 10

    arr = [None] * length_of_array

    left_index = 0
    right_index = length_of_array - 1

    def push_left(val):
        nonlocal left_index, right_index
        if arr[left_index] is None:
            arr[left_index] = val
            return True
        if left_index + 1 < right_index:
            left_index += 1
            arr[left_index] = val
            return True
        if left_index + 1 == right_index and arr[right_index] == None:
            left_index += 1
            arr[left_index] = val
            return True
        print(list_full)
        return False

    def push_right(val):
        nonlocal left_index, right_index
        if arr[right_index] is None:
            arr[right_index] = val
            return True
        if right_index - 1 > left_index:
            right_index -= 1
            arr[right_index] = val
            return True
        if right_index - 1 == left_index and arr[left_index] == None:
            right_index -= 1
            arr[right_index] = val
            return True
        print(list_full)
        return False

    def pop_left():
        nonlocal left_index, right_index
        if left_index == right_index and left_index == 0:
            print(stack1_empty)
            return None
        val = arr[left_index]
        arr[left_index] = None
        left_index -= 1
        return val

    def pop_right():
        nonlocal left_index, right_index
        if left_index == right_index and right_index == length_of_array - 1:
            print(stack2_empty)
            return None
        val = arr[right_index]
        arr[right_index] = None
        right_index += 1
        return val

    while True:
        print(choices)
        try:
            user_choice = int(input(choice_string))
        except ValueError:
            print(invalid_type_string)
        else:
            match user_choice:
                case 0:
                    break
                case 1:
                    print(arr)
                case 2:
                    try:
                        val = int(input(val_string))
                    except ValueError:
                        print(invalid_type_string)
                    else:
                        status = push_left(val)
                        if status:
                            print(success)
                case 3:
                    try:
                        val = int(input(val_string))
                    except ValueError:
                        print(invalid_type_string)
                    else:
                        status = push_left(val)
                        if status:
                            print(success)
                case 4:
                    val = pop_left()
                    if val:
                        print(pop_string.format(val))
                case 5:
                    val = pop_right()
                    if val:
                        print(pop_string.format(val))
                case _:
                    print(invalid_choice)


if __name__ == "__main__":
    main()
