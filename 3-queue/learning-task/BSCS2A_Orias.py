class Queue:
    def __init__(self):
        # Initialize an empty list to store the items in the queue
        self.queue = []

    def enqueue(self, item: int):
        # Add an item to the end of the queue
        self.queue.append(item)

    def dequeue(self):
        # Remove an item from the front of the queue and return it
        # If the queue is empty, return None
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        # Return a string of the current queue, if the queue is empty return "Empty"
        if len(self.queue) == 0:
            return "Empty"
        return " ".join(map(str, self.queue))

    def size(self):
        # Return the number of items in the queue
        return len(self.queue)

    def sum(self):
        # Return the sum of all the items in the queue
        return sum(self.queue)

    def front(self):
        # Return the front item of the queue without removing it
        if len(self.queue) < 1:
            return None
        return self.queue[0]

# Workload Queue System
def main():
    queues = [Queue(), Queue(), Queue()]

    while True:
        print("----------------------------------------------")
        print(f"Queue 1: {queues[0].display()}")
        print(f"Queue 2: {queues[1].display()}")
        print(f"Queue 3: {queues[2].display()}")
        print("----------------------------------------------")
        print("[0] Exit")
        print("[1] Enqueue Workload")
        print("[2] Dequeue Workload")
        choice = input("Choice: ")

        if choice == "0":
            print("Thank you!")
            print("----------------------------------------------")
            break
        elif choice == "1":
            print("----------------------------------------------")
            try:
                value = int(input("Input Value of Workload: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            
            # New enqueue logic
            if all(queue.size() > 0 for queue in queues):
                # If all queues have values, choose the one with the lowest sum
                target_queue = min(queues, key=lambda q: q.sum())
            else:
                # If any queue is empty, choose the one with the least items
                target_queue = min(queues, key=lambda q: q.size())
            
            target_queue.enqueue(value)
        elif choice == "2":
            print("----------------------------------------------")
            # Dequeue from the non-empty queue with the lowest front value
            non_empty_queues = [queue for queue in queues if queue.size() > 0]
            if non_empty_queues:
                target_queue = min(non_empty_queues, key=lambda q: q.front())
                dequeued_value = target_queue.dequeue()
            else:
                print("All queues are empty. Nothing to dequeue.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()