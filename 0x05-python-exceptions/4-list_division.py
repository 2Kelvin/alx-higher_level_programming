#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    divList = []
    i = 0
    while (i < list_length):
        try:
            newVl = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            newVl = 0
        except ZeroDivisionError:
            print("division by 0")
            newVl = 0
        except IndexError:
            print("out of range")
            newVl = 0
        finally:
            divList.append(newVl)
        i += 1
    return divList
