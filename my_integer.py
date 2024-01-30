
def get_user_input():
    return input('Enter elements of a list separated by space:\n')

def multiples():
    user_input = get_user_input().split()
    
    try:
        user_input = [int(value) for value in user_input]
    except ValueError:
        print("Invalid input. All elements should be numeric.")
        return None

    if len(user_input) % 10 != 0:
        print("Input length should be in multiples of 10. i.e, 10, 20, 100....")
        return None

    new_list = [value for index, value in enumerate(user_input) if index % 2 != 0]
    return new_list

