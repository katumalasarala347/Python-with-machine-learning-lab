class Node:
    def __init__(self, data):  # Fixed: Added double underscores
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):        # Fixed: Added double underscores
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print(f"Successfully inserted {data}")

    def delete(self, key):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head
        # If head node holds the key to be deleted
        if temp.data == key:
            self.head = temp.next
            print(f"Deleted {key}")
            return
        
        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next
        
        if temp is None:
            print("Value not found in list.")
        else:
            prev.next = temp.next
            print(f"Deleted {key}")

    def display(self):
        if not self.head:
            print("\nList is empty.")
            return
        print("\nCurrent List: ", end="")
        temp = self.head
        while temp:
            print(f"[{temp.data}]", end=" -> ")
            temp = temp.next
        print("None")

# --- User Interface ---
ll = LinkedList()
while True:
    print("\n1. Insert  2. Delete  3. Display  4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        val = input("Enter value to insert: ")
        ll.insert(val)
    elif choice == '2':
        val = input("Enter value to delete: ")
        ll.delete(val)
    elif choice == '3':
        ll.display()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")