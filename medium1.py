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
        if k==1:
            self.print()
        elif k>1:
            current=self.head
            temp_current=self.head
            count=1
            while current!=None:
                if count==0:
                    temp_current=current
                    current=current.link
                    count+=1
                elif count==k:
                    current2=current
                    while True:
                        temp=temp_current
                        while temp.link!=current:
                            temp=temp.link
                        if temp==temp_current:
                            print(current.data)
                            if temp_current==self.head:
                                print(temp_current.data)
                            break
                        else:
                            print(current.data)
                            current=temp
                    
                    current=current2
                    count=0
                elif current.link==None and (count>0 and count<k):
                    temp=temp_current
                    while current!=temp_current:
                        if temp.link==current:
                            print(current.data)
                            current=temp
                            temp=temp_current
                        else:
                            temp=temp.link
                    break
                else:
                    current=current.link
                    count+=1
        else:
            print("Oops...Given number should be greater than 0...!!")

l=linkedlist()
while True:
    print("""press 1 to perform insertion
press 2 to display the list
press 3 to perform group reversal""")
    choice=int(input("Enter your choice: "))
    if choice==1:
        l.add(node(input("Enter data: ")))
    elif choice==2:
        l.print()
    elif choice==3:
        l.grp_rev(int(input("Enter group number: ")))
    else:
        print("*****************thankyou*****************")
        break