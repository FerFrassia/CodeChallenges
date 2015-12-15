#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int num;
    int sum = 0;
    int t;
    cin >> t;
    for (int i=0; i<t; ++i) {
        cin >> num;
        sum += num;
    }
    cout << sum << endl;
    return 0;
}

