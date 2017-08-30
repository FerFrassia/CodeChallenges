class Node<T> {
    var data: T
    var next: Node<T>?
    init(data: T) {
        self.data = data
        self.next = nil
    }
}

class List<T: Hashable> {
    private var head: Node<T>?
    private var size: Int
    
    init() {
        head = nil
        size = 0
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
        
        size += 1
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
    
    func kToLast(k: Int) -> Node<T>? {
        guard k < size else {return nil}
        var current = head
        var index = 0
        while index < size - 1 - k {
            current = current?.next
            index += 1
        }
        return current
    }
    
    func sizeOfList() -> Int {
        return size
    }
    
}

//test list
var l = List<Int>()
l.append(element: 5)
l.append(element: 3)
l.append(element: 8)
assert(l.toArray() == [5,3,8])

//test kth to last
l = List<Int>()
for i in 0...5 {
    l.append(element: i)
}
for i in 0...5 {
    if let ith = l.kToLast(k: i) {
        assert(ith.data == l.sizeOfList() - 1 - i)
    } else {
        assert(false)
    }
}
assert(l.kToLast(k: 6) == nil)







