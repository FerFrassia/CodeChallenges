class Node<T> {
    var data: T
    var next: Node<T>?
    init(data: T) {
        self.data = data
        self.next = nil
    }
}

class List<T: Hashable> {
    var head: Node<T>?
    
    init() {
        self.head = nil
    }
    
    func append(element: T) {
        var prev: Node<T>? = nil
        var current = head
        
        while current != nil {
            prev = current
            current = current!.next
        }
        
        let newNode = Node<T>(data: element)
        if prev != nil {
            prev?.next = newNode
        } else {
            head = newNode
        }
    }
    
    func toArray() -> [T] {
        var arr = [T]()
        var current = head
        while current != nil {
            arr.append(current!.data)
            current = current!.next
        }
        return arr
    }
    
    func giveNode(_ data: T) -> Node<T>? {
        var curr = head
        while curr != nil && curr!.data != data {
            curr = curr?.next
        }
        return curr
    }
    
    func deleteMiddle(node: Node<T>) {
        let tmp = node.data
        node.data = node.next!.data
        node.next!.data = tmp
        node.next = node.next!.next
    }
    
}


//test list
var l = List<Int>()
l.append(element: 5)
l.append(element: 3)
l.append(element: 8)
assert(l.toArray() == [5,3,8])

//test give node
var arr = [Int]()
for i in 0...9 {
    l.append(element: i)
    arr.append(i)
}
for i in 0...9 {
    if let n = l.giveNode(i) {
        assert(n.data == i)
    } else {
        assert(false)
    }
}

//test remove duplicates
l = List<Int>()
arr = [Int]()
for i in 0...9 {
    l.append(element: i)
    arr.append(i)
}
assert(l.toArray() == arr)
l.deleteMiddle(node: l.giveNode(3)!)
assert(l.toArray() == Array(0...2) + Array(4...9))
l.deleteMiddle(node: l.giveNode(6)!)
assert(l.toArray() == [0,1,2,4,5,7,8,9])
l.deleteMiddle(node: l.giveNode(7)!)
assert(l.toArray() == [0,1,2,4,5,8,9])








