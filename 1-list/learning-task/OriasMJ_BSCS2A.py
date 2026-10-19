# insert a value at the start of the list
def insert_at_start(list, value):
    list.insert(0, value) 

# insert a value at the end of the list
def insert_at_end(list, value):
    list.append(value) 

# insert a value at a specific position in the list
def insert_at_position(list, index, value):
    list.insert(index, value)

# delete the value at the start of the list
def delete_at_start(list):
    if len(list) == 0:
        print("List is empty, cannot delete")
    else:
        list.pop(0)

# delete the value at the end of the list
def delete_at_end(list):
    if len(list) == 0:
        print("List is empty, cannot delete")
    else:
        list.pop()

# delete the value at a specific position in the list
# it checks if the list is empty or if the index is out of range, and prints an error message if so. 
# otherwise, it removes the element at the specified index using the pop method.
def delete_at_position(list, index):
    if len(list) == 0:
        print("List is empty, cannot delete")
    elif index < 0 or index >= len(list):
        print("Invalid position, cannot delete")
    else:
        list.pop(index)

# delete the first occurrence of a number in the list
def delete_number(list, num):
    if num in list:
        list.remove(num)
        print(f"{num} has been successfully deleted.")
    else:
        print(f"{num} is not on the list and cannot be deleted.")

# search for a number in the list and return its position
def search_number(list, num):
    if num in list:
        print(f"Value {num} found at position {list.index(num)}")
    else:
        print(f"Value {num} not found")

# display the number at a specific position in the list
# if the index is less than 0 or greater than or equal to the length of the list, it prints "Invalid position". 
# otherwise, it prints the number at the specified position in the list.
def display_number_at_position(list, index):
    if index < 0 or index >= len(list): 
        print("Invalid position")
    else:
        print(f"Number at position {index} is {list[index]}") 

# display the entire list
def display_list(list):
    print(*list)

# main program
# this is a loop that runs until the user chooses to exit
# this is also incorporated with an error handling mechanism using the try-except block to ensure that the user enters a valid choice

def main():
    list = [] # create an empty list
    while True:
        print("\nMenu:")
        print("[0] Exit")
        print("[1] Insert At Start")
        print("[2] Insert At End")
        print("[3] Insert At Position")
        print("[4] Delete At Start")
        print("[5] Delete At End")
        print("[6] Delete At Position")
        print("[7] Delete Number")
        print("[8] Search Number")
        print("[9] Display Number At Position")
        print("[10] Display List")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue
        if choice == 0:
            confirm = input("Are you sure you want to exit? (y/n): ")
            if confirm.lower() == "y":
                print("Thank you!")
                break
        elif choice == 1:
            try:
                value = int(input("Enter the value to insert: "))
            except ValueError:
                print("Invalid value. Please enter a number.")
                continue
            insert_at_start(list, value)
            print(f"{value} has been successfully inserted at the start.")
        elif choice == 2:
            try:
                value = int(input("Enter the value to insert: "))
            except ValueError:
                print("Invalid value. Please enter a number.")
                continue
            insert_at_end(list, value)
            print(f"{value} has been successfully inserted at the end.")
        elif choice == 3:
            try:
                index = int(input("Enter the position to insert: "))
                value = int(input("Enter the value to insert: "))
            except ValueError:
                print("Invalid value. Please enter a number.")
                continue
            insert_at_position(list, index, value)
            print(f"{value} has been successfully inserted at position {index}.")
        elif choice == 4:
            delete_at_start(list)
            print(f"The value at the start has been successfully deleted.")
        elif choice == 5:
            delete_at_end(list)
            print(f"The value at the end has been successfully deleted.")
        elif choice == 6:
            try:
                index = int(input("Enter the position to delete: "))
            except ValueError:
                print("Invalid position. Please enter a number.")
                continue
            delete_at_position(list, index)
            print(f"The value at position {index} has been successfully deleted.")
        elif choice == 7:
            try:
                num = int(input("Enter the number to delete: "))
            except ValueError:
                print("Invalid number. Please enter a number.")
                continue
            delete_number(list, num)
        elif choice == 8:
            try:
                num = int(input("Enter the number to search: "))
            except ValueError:
                print("Invalid number. Please enter a number.")
                continue
            search_number(list, num)
        elif choice == 9:
            try:
                index = int(input("Enter the position to display: "))
            except ValueError:
                print("Invalid position. Please enter a number.")
                continue
            display_number_at_position(list, index)
        elif choice == 10:
            if len(list) == 0:
                print("There are no numbers in the list.")
            else:
                display_list(list)
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()


