import UIKit

func allUniques(s: String) -> Bool {
    guard s.characters.count >= 2 else {return true}
    
    let sortedS = s.characters.sorted()
    for i in 0...s.characters.count - 2 {
        if sortedS[i] == sortedS[i+1] {return false}
    }
    return true
}

print(allUniques(s: "abcdef"))
