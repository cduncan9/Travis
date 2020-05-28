def is_fruit(fruit_check):
    fruit_list = ["banana", "apple", "cherry", "peach"]
    fruit_check = fruit_check.strip(" ")
    is_it_a_fruit = fruit_check in fruit_list
    return is_it_a_fruit


if __name__ == "__main__":
    print(is_fruit(" apple "))
    print(is_fruit("rocks"))
