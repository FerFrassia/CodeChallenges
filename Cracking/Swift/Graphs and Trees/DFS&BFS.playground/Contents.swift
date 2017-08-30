class Node<T> {
    var data: T
    var next: Node<T>?
    var prev: Node<T>?
    init(data: T) {
        self.data = data
        next = nil
        prev = nil
    }
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

class Queue<T> {
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
    
    func isEmpty() -> Bool {
        return head == nil
    }
}

struct Graph {
    
}

struct Vertex {
    var visited = false
    var marked = false
    var neighbours: [Vertex]
}

func dfsIterative(graph g: Graph, vertex v: Vertex) {
    var s = Stack<Vertex>()
    s.push(v)
    while !s.isEmpty() {
        let vertex = s.pop()!
        if !vertex.visited {
            vertex.visited
            for neighbour in vertex.neighbours {
                s.push(neighbour)
            }
        }
    }
}

func dfsRecursive(graph g: Graph, vertex v: inout Vertex) {
    v.visited = true
    for var neighbour in v.neighbours {
        if !neighbour.visited {
            dfsRecursive(graph: g, vertex: &neighbour)
        }
    }
}

func bfs(graph g: Graph, vertex v: inout Vertex) {
    let q = Queue<Vertex>()
    q.enqueue(v)
    v.marked = true
    
    while !q.isEmpty() {
        var vertex = q.dequeue()!
        vertex.visited = true
        for var neighbour in vertex.neighbours {
            if !neighbour.marked {
                neighbour.marked = true
                q.enqueue(neighbour)
            }
        }
    }
}





