class Node<T: Equatable>: Equatable {
    var data: T
    var next: Node<T>?
    var prev: Node<T>?
    init(data: T) {
        self.data = data
        next = nil
        prev = nil
    }
    
    static func == (lhs: Node<T>, rhs: Node<T>) -> Bool {
        return lhs.data == rhs.data
    }
}

class Queue<T: Equatable> {
    private var head: Node<T>?
    private var tail: Node<T>?
    
    init() {
        head = nil
        tail = nil
    }
    
    func enqueue(_ element: T) -> Node<T> {
        let n = Node<T>(data: element)
        n.next = tail
        tail?.prev = n
        tail = n
        if head == nil {head = tail}
        return n
    }
    
    func dequeue() -> T? {
        guard self.head != nil else {return nil}
        let oldHead = head
        head = head?.prev
        head?.next = nil
        return oldHead!.data
    }
    
    func delete(_ data: T) {
        var n = head
        while n?.data != data {
            n = n?.next
        }
        
        if let next = n?.next {
            next.prev = n?.prev
        }
        
        if let prev = n?.prev {
            prev.next = n?.next
        }
    }
}

class Animal: Equatable {
    var name: String
    
    init(_ name: String) {
        self.name = name
    }
    
    static func == (lhs: Animal, rhs: Animal) -> Bool {
        return lhs.name == rhs.name
    }
}

class Dog: Animal {
    
}

class Cat: Animal {
    
}


class ShelterQueue {
    private var joinedQueue = Queue<Animal>()
    private var catQueue = Queue<Node<Animal>>()
    private var dogQueue = Queue<Node<Animal>>()
    
    func enqueue(_ animal: Animal) {
        let n = joinedQueue.enqueue(animal)
        if animal is Dog {
            dogQueue.enqueue(n)
        } else if animal is Cat {
            catQueue.enqueue(n)
        }
    }
    
    func dequeueAny() -> Animal? {
        let firstAnimal = joinedQueue.dequeue()
        if firstAnimal is Dog {
            dogQueue.dequeue()
        } else if firstAnimal is Cat {
            catQueue.dequeue()
        }
        return firstAnimal
    }
    
    func dequeueDog() -> Animal? {
        guard let firstDog = dogQueue.dequeue() else {return nil}
        joinedQueue.delete(firstDog.data)
        return firstDog.data
    }
    
    func dequeueCat() -> Animal? {
        guard let firstCat = catQueue.dequeue() else {return nil}
        joinedQueue.delete(firstCat.data)
        return firstCat.data
    }
}


//no testing, too large






