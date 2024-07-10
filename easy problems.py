class node:
    def __init__(self,data):
        self.data=data
        self.link=None

class linklist:
    def __init__(self):
        self.head=None
        
     #insertion elements
    def insertion(self,newnode):
        if self.head==None:
            self.head=newnode
        else:
            current=self.head
            while current.link!=None:
                current=current.link
            current.link=newnode
    
    #performing deletion
    def deletion(self):
        print("""press 1 for deletion at first
press 2 for deletion in between
press 3 for deletion at last""")
              
        choice=int(input("Enter your choice: "))
        current=self.head
        if self.head==None:
            print("Oops...it seems list is already empty")
        elif choice==1:          
            #deletion at first
            self.head=self.head.link
            print("successfully deleted...!!")
        elif choice==2:
            #deletion in between
            element=input("Enter element to be deleted: ")
            while current.link.data!=element:
                current=current.link
            current.link=current.link.link
            print("successfully deleted...!!")
        elif choice==3:
            #deletion at last
            while current.link.link!=None:
                current=current.link
            current.link=None
            print("successfully deleted...!!")
        else:
            print("Invalid Option...!!")
            
    #Searching
    def search(self,element):
        current=self.head
        while current!=None:
            if current.data==element:
                print("search successfull...!!")
                break
            current=current.link
        if current==None:
            print("search unsuccessfull...!!")
            
    #Node count
    def count(self):
        count=0
        current=self.head
        while current!=None:
            count+=1
            current=current.link
        
        return count
    
    #displaying list data
    def display(self):
        if self.head==None:
            print("list is empty..!!")
            
        current=self.head
        while current!=None:
            if current.link==None:
                print(current.data)
            else:
                print(current.data,end="->")
            current=current.link
        print()
    
    #Print the Middle of a given linked list
    def middle(self):
        c=self.count()
        global current
        if self.head==None or c==0:
            print("list is empty..!!")
        elif c==1:
            print(self.head.data)
        elif c%2==0:
            a=1
            c=(c//2)+1
            current=self.head
            while a!=c:
                a+=1
                current=current.link
        else:
            a=0
            c=c//2
            current=self.head
            while a!=c:
                current=current.link
                a+=1 
        return current.data
    
    #Reverse a Linked List
    def reverse(self):
        current=self.head
        while current.link!=None:
            current=current.link
        while True:
            temp=self.head 
            if temp==self.head and current==self.head:
                print(current.data)
                break
            else:
                print(current.data,end="->")
            while temp.link!=current:
                temp=temp.link
            current=temp
        print()
        
    #Rotate a linked list.
    def rotate(self):
        print("******************welcome to rotation******************")
        k=int(input("Enter number from which rotation to be performed: "))
        if self.head==None:
            print("List is empty...!!")
        else:
            current=self.head
            for i in range(k):
                current=current.link
            temp=current
            while temp!=None:
                print(temp.data,end="->")
                temp=temp.link
            temp=self.head
            while temp!=current:
                if temp.link==current:
                    print(temp.data)
                else:
                    print(temp.data,end="->")
                temp=temp.link
            print()
    
    #Program for Nth node from the end of a Linked List
    def pos_from_last(self):
        k=input("Enter number: ")
        current=self.head
        while current.data!=k:
            current=current.link
        count=0
        while current!=None:
            count+=1
            current=current.link
        print(count)
        
    def check_repeat(self,element):
        if self.head==None:
            print("list is empty...!!")
        else:
            current=self.head
            count=0
            while current!=None:
                if current.data==element:
                    count+=1
                current=current.link
        return count
        
    #Delete last occurrence of an item from linked list
    def last_occured(self):
        if self.head==None:
            print("list is already empty...!!")
        else:
            k=input("Enter number to be deleted: ")
            count=0
            current=self.head
            while current!=None:
                if current.data==k:
                    count+=1
                if count==self.check_repeat(k):
                    break
                current=current.link
            temp=self.head
            while temp.link!=current:
                temp=temp.link
            temp.link=temp.link.link
            print("deleted successfully...!!")
            
    #delete middle of the linkedlist
    def del_mid(self):
        if self.head==None:
            print("list is already empty...!!")
        elif self.head.link==None:
            self.head==None
            print("successfully deleted...!!")
        else:
            self.middle()
            temp=self.head
            while temp.link!=current:
                temp=temp.link
            temp.link=temp.link.link
            print("successfully deleted...!!")
        
    def unique(self):
        current=self.head
        while current!=None:
            if current.data==current.link.data:
                current.link=current.link.link
            elif current.data!=current.link.data:
                current=current.link
                
    #Delete N nodes after M nodes of a linked list
    def del_N(self,m,n):
        if self.head==None:
            print("list is empty...!!")
        else:
            count=1
            current=self.head
            while count!=m:
                if current==None:
                    break
                else:
                    print(current.data)
                    current=current.link
                    count+=1
            temp=current
            for i in range(n):
                if temp.link==None:
                    current.link=temp.link
                    break
                else:
                    temp=temp.link
            current.link=temp.link
            while current!=None:
                print(current.data)
                current=current.link
                
        
            
            
l=linklist()
while True:
    print("""press 1 to perform insertion
press 2 to perform deletion
press 3 to display
press 4 to count number of data
press 5 to perform searching
press 6 to find middle of the list
press 7 to perform reversal
press 8 to perform rotation 
press 9 to know position from last
press 10 to check number of repeatations
press 11 to delete the last occurance
press 12 to delete middle element
press 13 to remove duplicate
press 14 to delete N nodes after M nodes
press 15 to create another list
press any other key to exit""")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("******************welcome to insertion******************")
        l.insertion(node(input("Enter element: ")))
    elif choice==2:
        print("******************welcome to deletion******************")
        l.deletion()
    elif choice==3:
        print("******************Display******************")
        l.display()
    elif choice==4:
        print("number of nodes: ",l.count())
    elif choice==5:
        print("******************welcome to Searching******************")
        l.search(node(input("Enter element: ")))
    elif choice==6:
        print(l.middle())
    elif choice==7:
        l.reverse()
    elif choice==8:
        l.rotate()
    elif choice==9:
        l.pos_from_last()
    elif choice==10:
        print(l.check_repeat(input("Enter number:")))
    elif choice==11:
        l.last_occured()
    elif choice==12:
        l.del_mid()
    elif choice==13:
        l.unique()
    elif choice==14:
        l.del_N(int(input("Enter after which data to be deleted: ")),int(input("Enter upto which data to be deleted: ")))
    elif choice==15:
        print("""press 1 for insertion in list
press 2 to display
press 3 to merge it into main list""")
        option=int(input("Enter your choice: "))
        a=linklist()
        if option==1:
            a.insertion(input("Enter element: "))
        elif option==2:
            a.display()
    else:

        print("************************thank you************************")
        break
    


