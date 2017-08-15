func palindromeDic(s: String) -> [Character:Int] {
    var dict = [Character:Int]()
    for c in s.characters {
        if let amount = dict[c] {
            dict[c] = amount + 1
        } else {
            dict[c] = 1
        }
    }
    return dict
}

func checkForPalindrome(s: String) -> Bool {
    let dict = palindromeDic(s: s)
    var oddCharacters = 0
    for (_, charCount) in dict {
        if charCount % 2 != 0 {oddCharacters += 1}
    }
    return oddCharacters < 2
}

enum PalindromeErrors: Error {
    case noPosiblePalindrome
}

func possiblePalindromes(s: String) throws -> [String] {
    guard checkForPalindrome(s: s) else {throw PalindromeErrors.noPosiblePalindrome}
    var m = [[String]]()
    for i in 1...s.count {

    }

    return [s]
}












assert(checkForPalindrome(s: "abbca"), "palindrome check wrong for abbca")
//print(checkForPalindrome(s: "abbca"))

