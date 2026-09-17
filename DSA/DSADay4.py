from dataclasses import dataclass

@dataclass
class Node:
    data: int
    previous: Node | None = None
    next: Node | None = None

class DoublyLinkedListStack:
    def __init__(self):
        self.top: Node | None = None  # Top of stack
        self.tail: Node | None = None  # Bottom of stack

    def push(self, data: int):
        """Add a new node to the top of the stack."""
        new_node = Node(data=data, previous=None, next=self.top)
        
        if self.top is not None:
            self.top.previous = new_node
        else:
            # If the stack was empty, this node is the tail
            self.tail = new_node
            
        self.top = new_node

    def pop(self) -> int | None:
        if self.top is None:
            return None
        
        popped_data = self.top.data
        self.top = self.top.next

        if self.top is not None:
            self.top.previous = None
        else:
            self.tail = None
            
        return popped_data

    def peek(self) -> int | None:
        if self.top is None:
            return None
        return self.top.data

    def print_forward(self):
        current = self.top
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

    def print_backward(self):
        current = self.tail
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.previous
        print(" -> ".join(elements))


def test_doubly_linked_stack():
    stack = DoublyLinkedListStack()
    
    # Test empty stack peek
    assert stack.peek() is None, "Empty stack peek should be None"
    
    # Test push and peek
    stack.push(10); stack.push(20); stack.push(30)
    assert stack.peek() == 30, "Peek should return the top element (30)"
    
    # Verify it goes in both directions
    print("Top to Bottom")
    stack.print_forward()  # Should output: 30 -> 20 -> 10
    
    print("Bottom to Top")
    stack.print_backward() # Should output: 10 -> 20 -> 30
    
    # Test pointer consistency manually
    assert stack.top.data == 30; assert stack.top.next.data == 20; assert stack.top.next.next.data == 10
    
    assert stack.tail.data == 10; assert stack.tail.previous.data == 20; assert stack.tail.previous.previous.data == 30
    
    # Test pop and LIFO order
    assert stack.pop() == 30; assert stack.pop() == 20; assert stack.peek() == 10; assert stack.pop() == 10; assert stack.peek() is None; assert stack.top is None; assert stack.tail is None
    
    print("\nPassed all unit tests!\n")

if __name__ == "__main__":
    test_doubly_linked_stack()