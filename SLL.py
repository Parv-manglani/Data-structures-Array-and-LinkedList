#implementing Node class.
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

#implementing SLL class.
class SLL:
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0

#function for returning size.
    def size(self):
        return self.__size

    def append(self,data):
        newNode=Node(data)
        if self.__size==0:
            self.__head=newNode
            self.__tail=newNode
        else:
            self.__tail.next=newNode
            self.__tail=newNode
        self.__size+=1

    def removeLast(self):
        if self.__size==0:
            raise Exception("the linked list is empty.")
        elif self.__size==1:
            trav=self.__head
            self.__head=None
            self.__tail=None
            del trav
        else:
            rem=self.__tail
            trav=self.__head
            # id=0
            while(trav.next!=self.__tail):
                # id+=1
                trav=trav.next    
            self.__tail=trav
            self.__tail.next=None
            del rem
            self.__size-=1

    def __str__(self):
        li = []
        trav = self.__head
        while trav is not None:
            li.append(str(trav.data))
            trav = trav.next
        string = " --> ".join(li)
        return string
    
    def AddAt(self,ind,data):
        newNode=Node(data)
        id=0
        trav=self.__head
        while id!=ind-1:
            id+=1
            trav=trav.next
        newNode.next=trav.next
        trav.next=newNode
        self.__size+=1

    def remove(self,value):
        if self.__head.data==value:
            self.removeFirst()
        elif self.__size==1:
            trav=self.__head
            self.__head=None
            self.__tail=None
            del trav
            self.__size-=1
        else:
            trav=self.__head
            while trav.next.data!=value:
                trav=trav.next
            temp=trav.next
            trav.next=temp.next
            del temp
            self.__size-=1

    def isEmpty(self):
        if self.size()==0:
            return True
        else:
            return False
        
    def prepend(self,value):
        newNode=Node(value)
        newNode.next=self.__head
        self.__head=newNode
        self.__size+=1   

    def removeFirst(self):
        trav=self.__head
        self.__head=trav.next
        del trav
        self.__size-=1

    def merge(self,s):
        trav=self.__head
        while trav.next is not None:
            trav=trav.next
        trav.next=s.__head
        self.__tail=s.__tail
        self.__size+=s.__size

    def reverse(self):
        prev=None
        cur=self.__head
        nex=cur.next
        while cur.next is not None:
            cur.next=prev
            prev=cur
            cur=nex
            nex=nex.next
        cur.next=prev
        self.__head=cur
        # print(cur)

    def tail(self):
        return self.__tail.data

    def rotatefromright(self,k):
        n=self.__size-k
        trav=self.__head
        id=0
        while(id==n-1):
            id+=1
            trav=trav.next
        temp=trav.next
        trav.next=None
        self.__tail.next=self.__head
        self.__head=temp
        self.__tail=trav

    def middle(self):
        slow=self.__head
        fast=self.__head
        while fast.next and fast.next.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow.data
    
    def interleave(self,s):
        if self.__size==s.__size:
            t1=self.__head
            t2=s.__head
            while t1 and t2 is not None:
                temp1=t1.next
                temp2=t2.next
                t1.next=t2
                t2.next=temp1
                t1=temp1
                t2=temp2
        self.__size+=s.__size

    def find(self,k):
        trav=self.__head
        id=0
        while trav.next is not None:
            if trav.data==k:
                return id
            trav=trav.next
            id+=1
        return -1
            





    
    







    

    



        
# s=SLL()
# k=SLL()
# s.append(1)
# s.append(2)
# s.append(3)
# s.append(4)
# k.append(5)
# k.append(6)
# k.append(7)
# k.append(8)
# s.interleave(k)
# print(s.find(9))





# print(s.tail())
# print(s.size())
# print(s.middle())



# print(s)




# s=SLL()
# s.append(1)
# s.append(2)
# s.append(3)
# s.append(4)
# s.append(5)
# s.AddAt(3,0)
# s.remove(0)
# s.addFirst(0)
# s.remove(0)
# s.removeFirst()


# print(s.isEmpty())
# print(s)
# print(s.size())

    

