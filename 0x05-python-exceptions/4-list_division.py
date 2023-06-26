#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        divList = []
        i = 0
        while (i < list_length):
            newVl = my_list_1[i] / my_list_2[i]
            divList.append(newVl)
            i += 1
        return divList
    except TypeError:
        print("wrong type")
        divList.append(0)
    except ZeroDivisionError:
        print("division by 0")
        divList.append(0)
    except IndexError:
        print("out of range")
        divList.append(0)
    finally:
        return divList
