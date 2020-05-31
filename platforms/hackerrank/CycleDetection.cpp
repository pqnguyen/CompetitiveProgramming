#include <bits/stdc++.h>

using namespace std;

#define FastIO ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define FileIO freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout)

struct SinglyLinkedListNode {
    int data;
    SinglyLinkedListNode *next;
};

bool has_cycle(SinglyLinkedListNode *head) {
    if (!head || !head->next) { return false; }
    SinglyLinkedListNode *fast, *slow;
    slow = fast = head;
    while (fast and fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) { return true; }
    }
    return false;
}

int main() {
    FastIO;
    FileIO;
    return 0;
}