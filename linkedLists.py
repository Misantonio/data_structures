class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self, node=None):
        self.__head = node

    def add_last_node(self, node):
        if not self.__head:
            self.__head = node
        else:
            last = self.find_final_node()
            last.next = node            
    
    def add_head_node(self, node):
        if not self.__head:
            self.__head = node
        else:
            old_head = self.__head
            node.next = old_head
            self.__head = node

    def find_final_node(self):
        current = self.__head
        while True:
            if current.next == None:
                break
            current = current.next
        
        return current
    
    def count_nodes(self):
        current = self.__head
        count = 1
        while True:
            if current.next == None:
                break
            current = current.next
            count += 1
        
        return count
    
    def get_head_node(self):
        return self.__head


if __name__ == "__main__":
    nodeA = Node(6)
    nodeB = Node(5)
    nodeC = Node(4)
    nodeA.next = nodeB
    nodeB.next = nodeC
    link = LinkedList(nodeA)
    print(link.count_nodes()) 
    link.add_last_node(Node(9))
    print(link.count_nodes()) 