enum StackErrors: Error {
    case emptyStack
}

struct Stack<Element> {
    private var items = [Element]()
    
    mutating func push(_ value: Element) {
        items.append(value)
    }
    
    mutating func pop() -> Element? {
        return items.count > 0 ? items.removeLast() : nil
    }
    
    func peek() -> Element? {
        return items.count > 0 ? items[items.endIndex-1] : nil
    }
    
    func isEmpty() -> Bool {
        return items.count == 0
    }
}

func sortStack<Element: Comparable>(_ stack: inout Stack<Element>) {
    var sortedStack = Stack<Element>()
    while !stack.isEmpty() {
        let e = stack.pop()!
        if sortedStack.isEmpty() {
            sortedStack.push(e)
        } else {
            insert(element: e, from: &stack, to: &sortedStack)
        }
    }
    stack = sortedStack
}

func insert<Element: Comparable>(element e: Element, from stack: inout Stack<Element>, to sortedStack: inout Stack<Element>) {
    var poppedItems = 0
    while !sortedStack.isEmpty() && e > sortedStack.peek()! {
        stack.push(sortedStack.pop()!)
        poppedItems += 1
    }
    
    sortedStack.push(e)
    while poppedItems != 0 {
        sortedStack.push(stack.pop()!)
        poppedItems -= 1
    }
}


var s = Stack<Int>()
s.push(3)
s.push(8)
s.push(5)
s.push(1)
sortStack(&s)










