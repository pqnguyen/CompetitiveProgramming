#include <bits/stdc++.h>

using namespace std;

#define FastIO ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define FileIO freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout)

struct Node {
    Node *left;
    Node *right;
    int data;

    Node(int i) : data(i), left(nullptr), right(nullptr) {}
};

bool checkBSTUtil(Node *root, int min, int max) {
    if (!root) { return true; }
    if (root->data <= min || root->data >= max) { return false; }
    if (!checkBSTUtil(root->left, min, root->data)) {
        return false;
    }
    return checkBSTUtil(root->right, root->data, max);
}

bool checkBST(Node *root) {
    return checkBSTUtil(root, INT_MIN, INT_MAX);
}

int main() {
    FastIO;
    FileIO;
    return 0;
}