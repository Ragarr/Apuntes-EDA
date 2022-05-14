from dlist import DList, DNode

class DList2(DList):
    def __init__(self):
        super().__init__()
    
    def skipMremoveN(self,M:int,N:int):
        current=self._head
        while current:
            for i in range(M):
                current=current.next if current else current
            for i in range(N):
                if current and current.next and current.prev:
                    current.prev.next=current.next
                    current.next.prev=current.prev
                    current=current.next
                elif current and current.next:
                    current.next.prev=current.prev
                    current=current.next
                elif current and current.prev:
                    current.prev.next=current.next


                


        


l=[1,2,3,4,5,6,7,8,9,0]
dl=DList2()
for i in range(1,15):
    dl.addLast(i)
print(dl)
dl.skipMremoveN(3,11)
print(dl)