class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=self.next=None
        
class ListNode:
    def __init__(self):
        self.head=Node(None,None)
        self.tail=Node(None,None)
        self.Init()
        
    def Init(self):
        self.head.next=self.tail
        self.tail.prev=self.head
    
    def remove(self):
        temp=self.head.next.key
        self.head.next.next.prev=self.head
        self.head.next=self.head.next.next
        return temp
    
    def add(self,node):
        self.tail.prev.next=node
        node.prev=self.tail.prev
        node.next=self.tail
        self.tail.prev=node
    
    def change(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
        self.add(node)
    
    
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.size=capacity
        self.key_dict={}
        self.List=ListNode()
    # @return an integer
    def get(self, key):
        if key in self.key_dict:
            self.List.change(self.key_dict[key])
            return self.key_dict[key].val
        else:return -1
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.key_dict:
            self.key_dict[key].val=value
            self.List.change(self.key_dict[key])
        else:
            temp=Node(key,value)
            if self.size<=len(self.key_dict):
                x=self.List.remove()
                self.List.add(temp)
                del self.key_dict[x]
            
            else:
                self.List.add(temp)
                
            self.key_dict[key]=temp
            
                
