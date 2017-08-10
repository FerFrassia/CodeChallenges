//: Playground - noun: a place where people can play

import UIKit

var r = Array(repeating: Array(repeating: 0, count: 10), count: 10)
r[0][0] = 1

var i = 1
while i < r.count {
    r[i][0] = 1
    var j = 1
    while j < r[i].count {
        r[i][j] = r[i-1][j] + r[i-1][j-1]
        j += 1
    }
    i += 1
}
print("robots y tiempo: \(r) \n")


var m = Array(repeating: Array(repeating: 0, count: 10), count: 10)
var res = Array(repeating: [Int](), count: 10)

i = 0
while i < m.count {
    var j = 0
    while j < m[i].count {
        let maxAnt = i == 0 ? 0 : m[i-1].max()!
        m[i][j] = r[i][j] + maxAnt
        j += 1
    }
    
    j = 0
    while j < m.count {
        if m[i][j] == m[i].max()! {
            res[i].append(j)
        }
        j += 1
    }
    
    i += 1
}

print("robots 0 por día: \(m) \n")
print("robots 0 totales: \(m[9].max()!) \n")
print("decisiones tomadas: \(res) \n")









