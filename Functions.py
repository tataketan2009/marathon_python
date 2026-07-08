def number(r):
    area = 3.14 * r * r
    return area


a = 5


anumswer = number(a,)
print(anumswer)


def reverse_my_list(user_list):
    user_list.reverse()  
    return user_list     


user_input = input("Enter a list of items separated by spaces: ")


my_list = user_input.split()


reversed_result = reverse_my_list(my_list)


print("Reversed list:", reversed_result)