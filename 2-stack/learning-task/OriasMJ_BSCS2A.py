class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Linked list class
class LinkedList:
    def __init__(self):
        self.head = None

# Append data to the linked list
    def append(self, data):

        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

# Remove the last element in the linked list
    def remove_last(self):
        
        if not self.head:
            return None
        if not self.head.next:
            data = self.head.data
            self.head = None
            return data
        current = self.head
        while current.next.next:
            current = current.next
        data = current.next.data
        current.next = None
        return data
    
# Display the linked list
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Calculate the total height represented by the linked list
    def calculate_height(self):
        current = self.head
        height = 0
        while current:
            height += current.data
            current = current.next
        return height

# Stack class using linked list as underlying storage
class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

# Push an element onto the stack
    def push(self, data):
        self.linked_list.append(data)

# Pop an element from the stack
    def pop(self):
        return self.linked_list.remove_last()

# Get the total height of the stack
    def height(self):
        return self.linked_list.calculate_height()

# Display the stack
    def display(self):
        return self.linked_list.display()
    
# Display the stack in reverse order (LIFO)
    def display_reverse(self):
        return self.linked_list.display()[::-1]

def main():
    # Create three stacks
    stack1 = Stack()
    stack2 = Stack()
    stack3 = Stack()

    # Get elements for each stack
    while True:
        try:
            elements1 = list(map(int, input("Enter elements of Stack 1: ").split()))
            break
        except ValueError:
            print("Elements must be numbers, try again")
    while True:
        try:
            elements2 = list(map(int, input("Enter elements of Stack 2: ").split()))
            break
        except ValueError:
            print("Elements must be numbers, try again")
    while True:
        try:
            elements3 = list(map(int, input("Enter elements of Stack 3: ").split()))
            break
        except ValueError:
            print("Elements must be numbers, try again")

    # Push elements to each stack
    for element in elements1:
        stack1.push(element)
    for element in elements2:
        stack2.push(element)
    for element in elements3:
        stack3.push(element)

    # Calculate and display total height of each stack
    print("----------------------------------------------")
    print("Stack 1 total height:", stack1.height())
    print("Stack 2 total height:", stack2.height())
    print("Stack 3 total height:", stack3.height())
    print("----------------------------------------------")

    # Adjust all stacks to have the same height
    stacks = [stack1, stack2, stack3]
    heights = [stack.height() for stack in stacks]
    
    # Keep reducing the tallest stack until all heights are equal or all are zero
    while len(set(heights)) != 1:
        if all(height == 0 for height in heights):
            print("Stack heights will never be equal.")
            break
        max_height_index = heights.index(max(heights))
        stacks[max_height_index].pop()
        heights[max_height_index] = stacks[max_height_index].height()

    # All stacks should now have the same height
    equal_height = heights[0]

    # Display elements of each stack up to the equal height in LIFO order
    if equal_height == 0:
        print("Stack heights will never be equal.")
    else:
        print("All stacks are equal at Height:", equal_height)
        print("Stack 1:", *stack1.display_reverse())
        print("Stack 2:", *stack2.display_reverse())
        print("Stack 3:", *stack3.display_reverse())
    print("----------------------------------------------")

    # Ask if user wants to continue
    while True:
        answer = input("Continue? Y or N: ").upper()
        if answer == "Y":
            main()
            break
        elif answer == "N":
            print("Thank you!")
            break
        else:
            print("Invalid input, please enter Y or N")

if __name__ == "__main__":
    main()