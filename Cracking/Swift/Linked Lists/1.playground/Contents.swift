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
    
    func removeDuplicates() {
        var prev = head
        var current = prev?.next
        var seen = Set<T>()
        if let prev = prev {seen.insert(prev.data)}

        while current != nil {
            if seen.contains(current!.data) {
                prev?.next = current?.next
            } else {
                seen.insert(current!.data)
                prev = current
            }
            current = current?.next
        }
    }
}


//test list
var l = List<Int>()
l.append(element: 5)
l.append(element: 3)
l.append(element: 8)
assert(l.toArray() == [5,3,8])


//test remove duplicates
l = List<Int>()
var arr = [Int]()
for _ in 0...2 {
    for i in 0...9 {
        l.append(element: i)
        arr.append(i)
    }
}

assert(l.toArray() == arr)
l.removeDuplicates()
assert(l.toArray() == Array(0...9))







