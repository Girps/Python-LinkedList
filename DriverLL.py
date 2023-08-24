from LinkedList import * 



list = LinkedList()
flag = True
while (flag):
    seq = input("1) Push Node\n2) Pop Node\n3) Display list \n4) Reverse list\n5) Clear list\n6) Search value in list\n7) List size\n8) End program ")
    match seq:
        case "1": # add node 
            value = input("Enter value to push to Linked list : ") 
            list.pushNode(value)
        case "2":
             try : 
                value = list.popNode()
                print("Popped {}".format(value))
             except Exception:
                 print("Empty list") 
        case "3":
            print(list)
        case "4":
            list.reverse()
            print(list)
        case "5":
            try : 
                list.clear()
                print("List cleared")
            except Exception:
                print("Empty list") 
        case "6":
            value = input("Value to search in Linked List : ")
            f = list.contains(value)
            print(f)
        case "7":
            print("List size {}".format(list.getSize()))
        case "8":
            flag = False
        case _:
            print("Invalid input") 
            ...
else:
    print("Terminate program")
