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



print(checkForPalindrome(s: "abbca"))