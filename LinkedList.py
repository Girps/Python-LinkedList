# file contains linked list data structure



class LinkedList:

    # Nested Node class
    class Node :
        __value = None
        __next = None
        def __init__(self, value): 
            self.__value = value



    # private attributes 
    __head = None 

    # methods 
    def __init__(self):
        ...
    
    # insert new node infront of the linked list 
    def pushNode (self, newNode):
        if(self.__head == None):
            self.__head = newNode
        else: 
            # not empty
            temp = newNode
            newNode.__next = self._head
            self.__head = temp
            temp = None 
            
    # Remove node from 
    def  popNode (self):
        # if empty throw an exceptino 
        if(self.__head == None):
            raise Exception("Can't remove empty list")
        else: 
            # Not empty 
            value = self.head.__value
            self.__head = self.__head.__next
            return value     

    # Get size of the linked list      
    def getSize(self): 
        size = 0
        cursor = self.__head
        # iterate the list and count number of elements 
        while (cursor != None):
            cursor = cursor.next
            size += 1
        return size 
    
    # Method checks if value is in the linked list return bool  
    def contains(self,value): 
        flag = False
        cursor = self.__head
        while (cursor != None) : 
            if (cursor.__value == value) :
                flag = True 
                break
        return flag 
    
    # Recursive Helper function
    def __reverseHelper(self, temp): 
        if (temp != None): 
            prev = self.__reverseHelper(temp)
            prev.__next = temp
            return temp 
        else:  
            self.__head = temp
            return temp

    # Method will reverse order of the linked list 
    def reverse(self): 
         # make sure not an empty list or single element list
         if( self.getSize() > 1) :
            # get reference to first node
            temp = self.__head
            self.__reverseHelper(temp) 
            tail = self.__head
            tail.__next = None
             