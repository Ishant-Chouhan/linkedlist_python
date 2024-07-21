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
    
    def grp_rev(self,k):
        current=self.head
        count=k
        while current!=None:
            if count==k:
                print(current.data)
                if current==self.head:
                    current=current.link
                    count=2
                else:
                    temp=current_temp
                    current_temp=current
                    while count!=1:
                        while temp.link!=current:
                            temp=temp.link
                        current=temp
                        print(current.data)
                        count-=1
                    current=current_temp
                    
            else:
                current=current.link
                count+=1

l=linkedlist()
while True:
    choice=int(input("Enter your choice: "))
    if choice==1:
        l.add(node(input("Enter data: ")))
    elif choice==2:
        l.print()
    elif choice==3:
        l.grp_rev(4)
    else:
        print("*****************thankyou*****************")
        break