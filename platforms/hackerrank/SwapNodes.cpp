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

void dfs(Node *root, int level, map<int, vector<Node *>> &nodeByLevel) {
    if (!root) { return; }
    nodeByLevel[level].push_back(root);
    if (root->left) {
        dfs(root->left, level + 1, nodeByLevel);
    }
    if (root->right) {
        dfs(root->right, level + 1, nodeByLevel);
    }
}

void inorder(Node *root) {
    if (!root) { return; }
    inorder(root->left);
    cout << root->data << " ";
    inorder(root->right);
}

int main() {
    FastIO;
    FileIO;

    int n, t, k, left, right, depth;
    cin >> n;
    Node *nodes[n];
    map<int, vector<Node *>> nodeByLevel;

    // initialize n node
    for (int i = 0; i < n; i++) {
        nodes[i] = new Node(i + 1);
    }

    // initialize tree
    for (int i = 0; i < n; i++) {
        cin >> left >> right;
        if (left != -1) {
            nodes[i]->left = nodes[left - 1];
        }
        if (right != -1) {
            nodes[i]->right = nodes[right - 1];
        }
    }

    Node *root = nodes[0];

    // iterate over tree and group nodes by their depth
    dfs(root, 1, nodeByLevel);
    depth = nodeByLevel.size();

    cin >> t;

    while (t--) {
        cin >> k;
        int i = k;
        while (i <= depth) {
            vector<Node *> &nodesAtI = nodeByLevel[i];
            for (Node *node : nodesAtI) {
                swap(node->left, node->right);
            }
            i += k;
        }
        inorder(root);
        cout << endl;
    }

    return 0;
}