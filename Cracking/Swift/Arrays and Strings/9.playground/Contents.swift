func isSubString(s1: String, s2: String) -> Bool {
    for i in s2.indices {
        let sub = String(s2[i..<s2.endIndex])
        if sub.hasPrefix(s1) {return true}
    }
    return false
}

func isRotation(s1: String, s2: String) -> Bool {
    guard s1.count == s2.count else {return false}
    let s2Composed = s2 + s2
    return isSubString(s1: s1, s2: s2Composed)
}

assert(isRotation(s1: "waterbottle", s2: "erbottlewat"))
assert(!isRotation(s1: "waterbottle", s2: "erbottleswat"))

