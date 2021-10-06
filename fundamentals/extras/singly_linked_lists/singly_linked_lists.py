class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None
        self.length = 1

    def add_to_front(self, value):
        new_node = SLNode(value)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        self.length += 1
        return self
    
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        self.length += 1
        return self

    def remove_from_front(self):
        if self.head == None:
            print("empty list")
            return self
        print(f"Removing first node with value: {self.head.value}")
        self.head = self.head.next
        self.length -= 1
        return self

    def remove_from_back(self):
        if self.head == None:
            print("empty list")
            return self
        runner = self.head
        temp = self.length - 2
        while (temp > 0):
            runner = runner.next
            temp -= 1
        print(f"Removing last entry with value: {runner.next.value}")
        runner.next = None
        self.length -= 1
        return self
        
    def remove_val(self, val):
        runner = self.head
        if runner == None:
            print("empty list")
            return self
        if runner.value == val:
            self.remove_from_front()
            print(f"removing {val} from front of list")
            self.length -= 1
            return self
        while (runner.next != None):
            prev_runner = runner
            runner = runner.next
            print(f"checking whether {runner.value} matches {val}")
            if runner.value == val:
                prev_runner.next = runner.next
                print(f"removing {val} from middle or end of list")
                self.length -= 1
                return self
        print(f"{val} not found in list")
        return self

    def insert_at(self, val, n):
        if n == 0:
            self.add_to_front(val)
            self.length += 1
            return self
        if n == self.length:
            self.add_to_back(val)
            self.length += 1
            return self
        runner = self.head
        count = n
        while (count > 0):
            runner = runner.next
            print(runner)
            count -= 1
        prev_node = runner
        next_node = runner.next
        new_node = SLNode(val)
        prev_node.next = new_node
        new_node.next = next_node
        self.length += 1
        print(f"added node with value {val} at position {n}")
        return self


# my_list = SList()
# my_list.add_to_front("are").add_to_front("linked lists").add_to_back("fun!").print_values()
# my_list.remove_from_front().print_values()

# test_list = SList()
# test_list.add_to_front("2").add_to_front("3").add_to_back("1").print_values()
# test_list.remove_from_back().print_values()

remove_test = SList()
remove_test.add_to_front("5").add_to_front("4").add_to_front("3").add_to_front("2").add_to_front("1").print_values()
remove_test.remove_val("3").remove_val("5").remove_val("1").print_values()
print(remove_test.length)

remove_test.insert_at(1, 0).insert_at(3, 2).insert_at(5, 3).print_values()