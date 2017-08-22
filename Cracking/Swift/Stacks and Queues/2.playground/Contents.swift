class Node<T> {
    var data: T
    var next: Node<T>?
    
    init(data: T) {
        self.data = data
    }
}

enum CollectionErrors: Error {
    case emptyCollection
}

class List<T> {
    private var head: Node<T>?
    
    init() {
        head = nil
    }
    
    func appendLeft(_ value: T) {
        let n = Node<T>(data: value)
        n.next = head
        head = n
    }
    
    func deppendLeft() throws -> T {
        guard head != nil else {throw CollectionErrors.emptyCollection}
        
        let oldHead = head
        head = head!.next
        return oldHead!.data
    }
    
    func peekFirst() throws -> T {
        guard head != nil else {throw CollectionErrors.emptyCollection}
        return head!.data
    }
}

class Stack<T> {
    private var list: List<T>
    
    init() {
        list = List<T>()
    }
    
    func push(_ value: T) {
        list.appendLeft(value)
    }
    
    func pop() throws -> T {
        let popped = try list.deppendLeft()
        return popped
    }
    
    func peek() throws -> T {
        let peeked = try list.peekFirst()
        return peeked
    }
}

class MinStack<T: Comparable> {
    private var stack: Stack<T>
    private var minStack: Stack<T>
    
    init() {
        stack = Stack<T>()
        minStack = Stack<T>()
    }
    
    func push(_ value: T) {
        stack.push(value)
        
        do {
            let peeked = try minStack.peek()
            if value < peeked {
                minStack.push(value)
            }
        } catch {
            minStack.push(value)
        }
    }
    
    func pop() throws -> T {
        let top = try stack.pop()
        let minTop = try minStack.peek()
        if top == minTop {
            try minStack.pop()
        }
        return top
    }
    
    func min() throws -> T {
        let minTop = try minStack.peek()
        return minTop
    }
}


//TESTS

//empty stack
let emptyMinStack = MinStack<Int>()
do {
    try emptyMinStack.min()
    assert(false)
} catch {
    assert(true)
}

do {
    try emptyMinStack.pop()
    assert(false)
} catch {
    assert(true)
}

//1 value
let oneValMinStack = MinStack<Int>()
oneValMinStack.push(3)
do {
    let val = try oneValMinStack.min()
    assert(val == 3)
} catch {
    assert(false)
}

//3 values
let threeValMinStack = MinStack<Int>()
threeValMinStack.push(3)
threeValMinStack.push(4)
threeValMinStack.push(-2)
do {
    let min1 = try threeValMinStack.min()
    assert(min1 == -2)
    try threeValMinStack.pop()
    let min2 = try threeValMinStack.min()
    assert(min2 == 3)
    try threeValMinStack.pop()
    let min3 = try threeValMinStack.min()
    assert(min3 == 3)
} catch {
    assert(false)
}




