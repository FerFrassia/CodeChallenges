enum indexError: Error {
    case couldNotAdvanceIndex
}

func advanceIndexes(i1: inout String.Index, i2: inout String.Index, s1: String, s2: String) throws {
    if s1[s1.index(after: i1)] == s2[s2.index(after: i2)] {
        i1 = s1.index(after: i1)
        i2 = s2.index(after: i2)
    } else if s1[i1] == s2[s2.index(after: i2)] {
        i2 = s2.index(after: i2)
    } else if s1[s1.index(after: i1)] == s2[i2] {
        i1 = s1.index(after: i1)
    } else {
        throw indexError.couldNotAdvanceIndex
    }
}

func oneWay(s1: String, s2: String) -> Bool {
    guard abs(s1.count - s2.count) < 2 else {return false}
    
    var diffs = 0
    var i2 = s2.startIndex
    for var i1 in s1.indices {
        guard i2 != s2.endIndex else {return diffs + 1 < 2}
        if s1[i1] != s2[i2] {
            diffs += 1
            do {
                try advanceIndexes(i1: &i1, i2: &i2, s1: s1, s2: s2)
            } catch {
                return false
            }
        } else {
            i2 = s2.index(after: i2)
        }
    }
    return diffs < 2
}

assert(oneWay(s1: "pale", s2: "ple"), "pale | ple")
assert(oneWay(s1: "pales", s2: "pale"), "pales | pale")
assert(oneWay(s1: "pale", s2: "bale"), "pale | bale")
assert(!oneWay(s1: "pale", s2: "bake"), "pale | bake")





