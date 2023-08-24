# file contains linked list data structure



class LinkedList:

    # Nested Node class
    class Node :
        value = None
        next = None
        def __init__(self, value): 
            self.value = value
        


    # private attributes 
    __head = None 

    # methods 
    def __init__(self):
        ...
    # Return string representation of the linked list  
    def __str__(self):
        result = ""
        if (self.__head == None):
             return "[" + result + "]"
        else: 
            cursor = self.__head
            while (cursor != None) :  
                result += "["+ str( cursor.value ) + "]---"
                cursor = cursor.next 
            return result
    
    # insert new node infront of the linked list 
    def pushNode (self, value):
        if(self.__head == None):
            newNode = self.Node(value) 
            self.__head = newNode
        else: 
            # not empty
            newNode = self.Node(value)
            newNode.next = self.__head
            self.__head = newNode
            
    # Remove node from 
    def  popNode (self):
        # if empty throw an exceptino 
        if(self.__head == None):
            raise Exception("Can't remove empty list")
        else: 
            # Not empty 
            value = self.__head.value
            self.__head = self.__head.next
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
            if (cursor.value == value) :
                flag = True 
                break
        return flag 
    
    # Recursive Helper function
    def __reverseHelper(self, temp): 
        if (temp.next != None): 
            prev = self.__reverseHelper(temp.next)
            prev.next = temp
            return temp 
        else:  
            self.__head = temp
            return temp

    # Method will reverse order of the linked list 
    def reverse(self): 
         # make sure not an empty list or single element list
         if( self.getSize() > 1) :
            # get reference to first node
            temp = self.__reverseHelper(self.__head)
            temp.next = None

    # Method clears linked list
    def clear(self): 
        if(self.__head == None) :
            raise Exception("Empty list") 
        else:
            self.__head = None  
             