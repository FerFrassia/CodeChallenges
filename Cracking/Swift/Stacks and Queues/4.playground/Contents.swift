struct MyQueue<Element> {
    private var pushingStack = Stack<Element>()
    private var poppingStack = Stack<Element>()
    
    mutating func push(_ value: Element) {
        pushingStack.push(value)
        poppingStack = pushingStack.invert()
    }
    
    mutating func pop() throws -> Element {
        let popped = try poppingStack.pop()
        pushingStack = poppingStack.invert()
        return popped
    }
}

enum StackErrors: Error {
    case emptyStack
}

struct Stack<Element> {
    private var items = [Element]()
    
    mutating func push(_ value: Element) {
        items.append(value)
    }
    
    mutating func pop() throws -> Element {
        guard items.count > 0 else {throw StackErrors.emptyStack}
        return items.removeLast()
    }
    
    func invert() -> Stack<Element> {
        var copy = self
        var inverted = Stack<Element>()
        var isEmpty = false
        while !isEmpty {
            do {
                let e = try copy.pop()
                inverted.push(e)
            } catch {
                isEmpty = true
            }
        }
        return inverted
    }
}

//TEST
func testPoppingWith(amountOfElements n: Int) {
    var q = MyQueue<Int>()
    for i in 0...n {
        q.push(i)
    }
    for i in 0...n {
        do {
            let firstElement = try q.pop()
            assert(firstElement == i)
        } catch {
            assert(false)
        }
    }
}

for i in 0...5 {
    testPoppingWith(amountOfElements: i)
}







