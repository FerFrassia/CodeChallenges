func repetitions(i: String.Index, s: String) -> Int {
    var j = i
    var count = 0
    while j != s.endIndex && s[j] == s[i] {
        count += 1
        j = s.index(after: j)
    }
    return count
}

func compress(_ s: String) -> String {
    var compressed = ""
    var i = s.startIndex
    while i != s.endIndex {
        let count = repetitions(i: i, s: s)
        compressed += "\(s[i])\(count)"
        i = s.index(i, offsetBy: count)
    }
    return compressed.count <= s.count ? compressed : s
}

assert(compress("aabcccccaaa") == "a2b1c5a3")
assert(compress("a") == "a")
assert(compress("") == "")
assert(compress("aa") == "a2")
assert(compress("aabbbbd") == "a2b4d1")
