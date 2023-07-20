from random import randint

class Node:
    def __init__ (self,value = None):
        self.value = value
        self.next = None
#--------------------------------
class LinkedList:
    def __init__(self):
        self.head = None
# ----- Добавление элемента -------------------------------
    def add(self, value):
        newnode = Node(value)
        if self.head is None:
          self.head = newnode
          return
        lastnode = self.head
        while (lastnode.next):
            lastnode = lastnode.next
        lastnode.next = newnode
# ----- Вставка элемента -------------------------------
    def insert(self,newdata,value):
        new_list=LinkedList()
        lastnode = self.head
        while (lastnode):
            if lastnode.value == value:
                new_list.add(value)
                new_list.add(newdata)
                lastnode = lastnode.next
            else:
                new_list.add(lastnode.value)
                lastnode = lastnode.next
        return new_list
# ----- Печать списка -------------------------------
    def print_list (self):
        lastnode = self.head
        while (lastnode):
            print (lastnode.value,end=" ")  
            lastnode = lastnode.next
# ----- Разворот списка -------------------------------
    def reverse (self):
        tmp=[]
        lastnode = self.head
        while (lastnode):
            tmp.append(lastnode.value)  
            lastnode = lastnode.next
        tmp.reverse()
        self.head=None
        for i in range(len(tmp)):
            self.add(tmp[i])
        return      
#------ Удаление элемента ---------------------------
    def remove(self,dvalue):
        headnode = self.head
        if headnode is not None:
            if headnode.value==dvalue:
                self.head = headnode.next
                headnode = None
                return
        while headnode is not None:
            if headnode.value==dvalue:
                break
            lastnode = headnode
            headnode = headnode.next
        if headnode == None:
            return
        lastnode.next = headnode.next
        headnode = None

#-------------------------------
print("Введите кол-во элементов для формирования списка")
n=int(input())
ll=LinkedList()
for i in range(n):
    ll.add(randint(1,100))

print("Односвязный список создан")
ll.print_list()
command=""
while command!="stop":
    print("\n\nВведите команду (stop для выхода)")
    print("d - удаление элемента")
    print("i - вставка элемента ")
    print("r - развернуть список в обратном порядке")
    command=input()
    if command=="d":
        print("Какой элемент нужно удалить?")
        ll.remove(int(input()))
        ll.print_list()
    elif command=="r":
        ll.reverse()
        ll.print_list()
    elif command=="i":
        print("Введите значение нового элемента и после какого. Через пробел")
        new,val=map(int,input().split())
        ll=ll.insert(new,val)
        ll.print_list()


        
