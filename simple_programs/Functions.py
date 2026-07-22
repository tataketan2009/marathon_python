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



def add_item(lst, item):
    lst.append(item)
    return lst

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff, 'Meat'))

def remove_item(lst, item):
    lst.remove(item)
    return lst

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))



def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print(sum_of_numbers(5))  


def greet_user(name):
    return f"Hello, {name}!"

name = input("Enter your name: ")
greeting = greet_user(name)
print(greeting)


def fav_book(managment, book):
    return f"My favorite book is '{book}' and I recommend '{managment}'."

answer = fav_book("The Great Gatsby", "To Kill a Mockingbird")
print(answer)
 
def fav_game(game):
    return f"My favorite game is '{game}'."

answer = fav_game("The Legend of Zelda: Breath of the Wild")
print(answer)
