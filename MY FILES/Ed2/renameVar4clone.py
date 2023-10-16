class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def addTwoIntegers(self, node1: Node, node2: Node) -> Node:
        car = 0
        solve = Node()
        curry = sol
        car = 0
        while node1 or node2 or car:
            answer = 0
            if node1:
                answer += node1.val
                node1 = node1.next
            if node2:
                answer += node2.val
                node2 = node2.next
            if car:
                answer += car
                
            val = answer % 10
            car = answer // 10
            curry.next = Node(val)
            curry = curry.next
                
        return solve.next