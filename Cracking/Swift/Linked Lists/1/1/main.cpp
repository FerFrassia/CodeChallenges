//
//  main.cpp
//  1
//
//  Created by Fernando N. Frassia on 8/27/17.
//  Copyright © 2017 Fernando N. Frassia. All rights reserved.
//

#include <iostream>
#include <set>

struct Node {
    int data;
    Node* next;
};

struct List {
    Node* head;
};

Node* buildList() {
    Node* head = NULL;
    
    for(int i = 5; i >= 0; --i) {
        Node* newNode = (Node*)malloc(sizeof(Node));
        newNode->data = i;
        newNode->next = head;
        head = newNode;
    }
    
    return head;
}

void removeNode(Node** dp, int searchValue) {
    while (*dp && (**dp).data != searchValue) {
        dp = &(**dp).next;
    }
    
    if (*dp != NULL) {
        Node* deletedNode = *dp;
        *dp = (**dp).next;
        free(deletedNode);
    }
}

void removeDuplicates(Node** head) {
    std::set<int> seen;
    Node** dp = head;
    while (*dp) {
        if (seen.find((**dp).data) == seen.end()) {
            seen.insert((**dp).data);
        } else {
            Node* deletedNode = *dp;
            
        }
    }
}

int main(int argc, const char * argv[]) {
    Node* list = buildList();
    removeNode(&list, 2);
    removeNode(&list, 0);
    std::cout << "Hello, World!\n";
    return 0;
}
