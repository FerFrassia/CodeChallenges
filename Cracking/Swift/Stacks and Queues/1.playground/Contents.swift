enum StackErrors: Error {
    case initialSizeError
    case maxSizeReached
    case stackEmpty
}

class threeStacks<T> {
    private var arr: [T?]
    var base0, base1, base2, top0, top1, top2: Int
    
    init(length: Int) throws {
        guard length >= 3 else {throw StackErrors.initialSizeError}
        
        arr = [T?](repeating: nil, count: length)
        
        base0 = 0
        base1 = arr.count/3
        base2 = arr.count/3 * 2
        if arr.count % 3 == 1 {base1 += 1}
        if arr.count % 3 == 2 {base2 += 1}
        
        top0 = base0 - 1
        top1 = base1 - 1
        top2 = base2 - 1
    }
    
    func pushFirst(_ val: T) throws {
        guard base1 - top0 > 1 else {throw StackErrors.maxSizeReached}
        top0 += 1
        arr[top0] = val
    }
    
    func pushSecond(_ val: T) throws {
        guard base2 - top1 > 1 else {throw StackErrors.maxSizeReached}
        top1 += 1
        arr[top1] = val
    }
    
    func pushThird(_ val: T) throws {
        guard arr.count - top2 > 1 else {throw StackErrors.maxSizeReached}
        top2 += 1
        arr[top2] = val
    }
    
    func popFirst() throws -> T {
        guard top0 >= base0 else {throw StackErrors.stackEmpty}
        let val = arr[top0]!
        top0 -= 1
        return val
    }
    
    func popSecond() throws -> T {
        guard top1 >= base1 else {throw StackErrors.stackEmpty}
        let val = arr[top1]!
        top1 -= 1
        return val
    }
    
    func popThird() throws -> T {
        guard top2 >= base2 else {throw StackErrors.stackEmpty}
        let val = arr[top2]!
        top2 -= 1
        return val
    }
    
}

do {
    let threeS =  try threeStacks<Int>(length: 6)
    try threeS.pushFirst(0)
    try threeS.pushSecond(1)
    try threeS.pushThird(2)
    
    do {
        let firstPop = try threeS.popFirst()
        assert(firstPop == 0)
    } catch {
        print("could not first pop")
    }

    do {
        let secondPop = try threeS.popSecond()
        assert(secondPop == 1)
    } catch {
        print("could not pop second")
    }
    
    
} catch {
    print("size maxed")
}










