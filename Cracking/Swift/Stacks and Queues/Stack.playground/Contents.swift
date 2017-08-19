class Node<T> {
    let data: T
    var next: Node<T>?
    init(_ withData: T) {
        data = withData
    }
}

enum ListError: Error {
    case emptyList
}

class List<T> {
    private var head: Node<T>?
    
    init() {
        head = nil
    }
    
    func getInitialElement() -> T? {
        return head?.data
    }
    
    func appendLeft(_ val: T) {
        let newHead = Node(val)
        newHead.next = head
        head = newHead
    }
    
    func dependLeft() -> T? {
        let oldHead = head
        head = oldHead?.next
        return oldHead?.data
    }
}

class Stack<T> {
    private var top: List<T>
    
    init() {
        top = List()
    }
    
    func push(_ val: T) {
        top.appendLeft(val)
    }
    
    func pop() -> T? {
        return top.dependLeft()
    }
    
    func peek() -> T? {
        return top.getInitialElement()
    }
}

let stack = Stack<Int>()
stack.push(5)
stack.push(2)
stack.push(1)

assert(stack.peek() == 1)
assert(stack.pop() == 1)
assert(stack.pop() == 2)
assert(stack.pop() == 5)
assert(stack.pop() == nil)



