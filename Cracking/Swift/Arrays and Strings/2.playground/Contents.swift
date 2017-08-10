import UIKit

func isPermutation(s1: String, s2: String) -> Bool {
    
    if s1.characters.count != s2.characters.count {return false}
    
    var dict = [Character:Int]()
    
    for c1 in s1.characters {
        if let c1Count = dict[c1] {
            dict[c1] = c1Count + 1
        } else {
            dict[c1] = 1
        }
    }
    
    for c2 in s2.characters {
        if let c2Count = dict[c2] {
            dict[c2] = c2Count - 1
        } else {
            return false
        }
    }
    
    for (_, charCount) in dict {
        if charCount != 0 {return false}
    }
    
    return true
}

print(isPermutation(s1: "a", s2: "b")) //false
print(isPermutation(s1: "ab", s2: "ba")) //true
print(isPermutation(s1: "abcb", s2: "abbc")) //true
print(isPermutation(s1: "abab", s2: "bbaa")) //true