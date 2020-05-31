#include <bits/stdc++.h>

using namespace std;

#define FastIO ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define FileIO freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout)

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode() : val(0), left(nullptr), right(nullptr) {}

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}

    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<double> averageOfLevels(TreeNode *root) {
        vector<double> res;
        vector<TreeNode *> &parents = *(new vector<TreeNode *>);

        if (root == nullptr) { return res; }
        parents.push_back(root);
        while (parents.size()) {
            double sum = 0;
            for (auto parent : parents) { sum += parent->val; }
            res.push_back(sum / parents.size());

            vector<TreeNode *> children;
            for (auto parent : parents) {
                if (parent->left) { children.push_back(parent->left); }
                if (parent->right) { children.push_back(parent->right); }
            }
            parents = children;
        }
        return res;
    }
};

int main() {
    FastIO;
    FileIO;
    Solution sol;
    return 0;
}