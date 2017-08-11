enum funcExceptions: Error {
    case notFoundException
}

func findPreviousLetter(_ s: [Character], _ i: Int) throws -> Int {
    var end = i - 1
    while end >= 0 && s[end] == " " {
        end -= 1
    }

    var start = end - 1
    while start >= 0 && s[start] != " " {
        start -= 1
    }

    if start < 0 {throw funcExceptions.notFoundException}
    return end
}

func moveWord(_ s: inout [Character], _ j: inout Int, _ i: inout Int) {
    while s[j] != " " {
        s[i] = s[j]
        s[j] = " "
        j -= 1
        i -= 1
    }
}

func add20Percent(_ s: inout [Character], _ i: inout Int) {
    s[i] = "0"
    s[i-1] = "2"
    s[i-2] = "%"
    i -= 3
}

func urlify(_ s: String) -> String {
    var s = Array(s)
    var i = s.count - 1
    while i >= 0 {
        do {
            var j = try findPreviousLetter(s,i)
            moveWord(&s,&j,&i)
            add20Percent(&s,&i)
        } catch {
            return String(s)
        }
    }
    return String(s)
}

print(urlify("mr john smith    ")) //"mr%20john%20smith"


