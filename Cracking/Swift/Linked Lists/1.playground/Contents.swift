struct Node {
    var data: Int?
    var next: Node?
    init(data: Int?, next: Node?) {
        self.data = data
        self.next = next
    }
}

struct List {
    var head: Node?
    var length: Int
    init() {
        self.head = nil
        self.length = 0
    }
    
    func append(n: Node) {
        
    }
}
