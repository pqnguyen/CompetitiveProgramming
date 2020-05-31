#include <bits/stdc++.h>

using namespace std;

#define FastIO ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define FileIO freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout)

typedef struct node {
    int freq;
    char data;
    node *left;
    node *right;
} node;

void decode_huff(node *root, string s) {
    string res;
    node *tmp = root;
    for (char ch : s) {
        if (ch == '0') {
            tmp = tmp->left;
        } else {
            tmp = tmp->right;
        }
        if (tmp->data != '\0') {
            cout << tmp->data;
            tmp = root;
        }
    }
}

int main() {
    FastIO;
    FileIO;
    return 0;
}