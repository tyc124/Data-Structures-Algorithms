#linked list: nested dictionaries

#each node = value & pointer (to the next item)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None #remain empty first


class LinkedList:
    def __init__(self, value):
        #create new Node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 #keep track of the list


    def print_list(self):
        temp = self.head
        while temp is not None: #None = no next item
            print(temp.value)
            temp = temp.next
        else:
            return None


    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0


    def append(self, value):
        #create new Node
        #add Node to end
        new_node = Node(value)
        
        #two edge cases
        #1st empty LL
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        #2nd not empty LL
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True #not necessary usu.
    

    def pop(self):
        #pop tail item
        #need temp and pre two pointers
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp 
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp


    def prepend(self, value):
        #create new Node
        #add Node to beginning
        new_node = Node(value)

        #start with empty list
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

        return True
    
    def popfirst(self):
        #pop the first item
        if self.length == 0:
            return None
        
        else:
            temp = self.head
            self.head = self.head.next #None if only one node
            temp.next = None #remove the pointer
            self.length -= 1
            
            if self.length == 0:
                self.tail = None

        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        """
        i = 0
        while i < self.length:
            if i == index:
                return temp
            else:
                temp = temp.next
                i += 1
        """
        for _ in range(index): #if i is not used in for loop, use _ instead
            temp = temp.next

        return temp
    
    def set_value(self, index, value):
        temp = self.get(index) #get the node by index
        
        if temp is not None:
            temp.value = value
            return True
        
        else:
            return False


    def insert(self, index, value):
        #create new Node
        #insert Node

        if index < 0 or index > self.length: #outlier
            return False #False is the opposite of True
        
        if index == 0: #prepend case (front)
            return self.prepend(value) #once this method is done, this method is done
        
        elif index == self.length: #append case (end), new index = current length # (-1+1)
            return self.append(value)
        
        else:
            temp = self.get(index-1)
            new_node = Node(value)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True
        
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None #None is the opposite of returning a node
        
        if index == 0:
            return self.popfirst()
        
        elif index == self.length -1:
            return self.pop()
        
        else:
            pre = self.get(index-1)
            temp = self.get(index) #temp = pre.next would be more efficient
            pre.next = temp.next
            temp.next = None #dont forget this
            self.length -= 1
            return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        """
        for _ in range(self.length-1):
            post = temp.next
            if post.next is not None:
                post.next = temp
                temp = temp.next
        """
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            #no need to have if after is None (just let before, temp, after = None)