class Iterator:
    def __init__(self, lst):
        self.lst = lst
        self.currentLink = lst.frontSentinel

    def hasNext(self):
        return self.currentLink.next is not self.lst.backSentinel

    def iteratorNext(self):
        self.currentLink = self.currentLink.next
        return self.currentLink.value

    def removeIter(self):
        temp = self.currentLink
        self.currentLink = self.currentLink.prev
        remove = getattr(self.lst, 'removeLink')
        remove(temp)

class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next

class DoubleList:
    def __init__(self):
        self.frontSentinel = Node(None, None, None)
        self.backSentinel = Node(None, None, None)
        self.frontSentinel.next = self.frontSentinel.prev = self.backSentinel
        self.backSentinel.next = self.backSentinel.prev = self.frontSentinel
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def addLinkAfter(self, link, value):
        newLink = Node(value, None, None)
        newLink.next = link.next
        newLink.prev = link
        link.next = newLink
        newLink.next.prev = newLink
        self.size += 1

    def removeLink(self, link):
        link.prev.next = link.next
        link.next.prev = link.prev
        self.size -= 1

    def addFront(self, value):
        self.addLinkAfter(self.frontSentinel, value)

    def addBack(self, value):
        self.addLinkAfter(self.backSentinel.prev, value)

    def getFront(self):
        if self.isEmpty() is False:
            return self.frontSentinel.next.value

    def getBack(self):
        if self.isEmpty() is False:
            return self.backSentinel.prev.value

    def removeFront(self):
        if self.isEmpty() is False:
            self.removeLink(self.frontSentinel.next)

    def removeBack(self):
        if self.isEmpty() is False:
            self.removeLink(self.backSentinel.prev)

    def print(self):
        if self.isEmpty() is False:
            current = self.frontSentinel.next
            while current is not self.backSentinel:
                print(current.value)
                current = current.next

    def reverse(self):
        if self.isEmpty() is False:
            reverse = self.frontSentinel
            forward = self.frontSentinel.next
            for i in range(1, self.size):
                reverse.next = reverse.prev
                reverse.prev == forward
                reverse = forward
                forward = forward.next

    def getNode(self, search):
        if self.isEmpty() is False:
            current = self.frontSentinel.next
            while current is not self.backSentinel:
                if current.value == search:
                    return current
                current = current.next

