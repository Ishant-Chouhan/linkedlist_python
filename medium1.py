class node:
    def __init__(self,data):
        self.data=data
        self.link=None

class linkedlist:
    def __init__(self):
        self.head=None
    
    def add(self,newnode):
        if self.head==None:
            self.head=newnode
        else:
            current=self.head
            while current.link!=None:
                current=current.link
            current.link=newnode
        
    def print(self):
        current=self.head
        while current!=None:
            print(current.data)
            current=current.link
    
    def grp_rev(self,k,m):
        current=self.head
        temp=self.head
        countk=0
        countm=0
        while countk!=k:
            pass


l=linkedlist()
while True:
    choice=int(input("Enter your choice: "))
    if choice==1:
        l.add(node(input("Enter data: ")))
    elif choice==2:
        l.print()
    elif choice==3:
        l.grp_rev(4,7)
    else:
        print("*****************thankyou*****************")
        break