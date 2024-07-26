#check whether linkedilst is a palindrome
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

    def check_palindrome(self):
        last=self.head
        while last.link!=None:
            last=last.link
        first=self.head
        count=0
        while last!=first or last.link!=first:
            if first.data!=last.data:
                count=1
                print("Not a Plaindrome")
                break
            first=first.link
            temp=self.head
            while temp.link!=last:
                temp=temp.link
            last=temp
        if count==0:
            print("Palinedrome")

l=linkedlist()
while True:
    print("""press 1 to perform insertion
press 2 to display
press 3 to check palindrome""")
    choice=int(input("Enter your choice: "))
    if choice==1:
        l.add(node(input("Enter data: ")))

    elif choice==2:
        l.print()

    elif choice ==3:
        l.check_palindrome()

    else:
        print("*******************thanks*******************")
        break