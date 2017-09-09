class Node<T> {
    var data: T
    var next: Node<T>?
    var prev: Node<T>?
    init(data: T) {
        self.data = data
        self.next = nil
        self.prev = nil
    }
}

class List<T: Hashable & Comparable> {
    private var head: Node<T>?
    private var tail: Node<T>?
    
    init() {
        self.head = nil
    }
    
    func appendRight(element: T) {
        let newNode = Node<T>(data: element)
        
        tail?.next = newNode
        newNode.prev = tail
        tail = newNode
        
        if head == nil {
            head = newNode
        }
    }
    
    func appendLeft(element: T) {
        let newNode = Node<T>(data: element)
        
        head?.prev = newNode
        newNode.next = head
        head = newNode
        
        if tail == nil {
            tail = newNode
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
    
    func partition(by element: T) {
        var current = head
        let partitionList = List<T>()
        
        while current != nil {
            if current!.data < element {
                partitionList.appendLeft(element: current!.data)
            } else {
                partitionList.appendRight(element: current!.data)
            }
            current = current?.next
        }
        head = partitionList.head
    }
}






