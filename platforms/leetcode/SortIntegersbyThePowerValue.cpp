#include <bits/stdc++.h>

using namespace std;

#define FastIO ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define FileIO freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout)

class Solution {
public:
    int getKth(int lo, int hi, int k) {
        queue<pair<int, int>> queue;
        for (int i = lo; i <= hi; i++) { queue.push({i, i}); }

        int u, v;
        while (queue.size()) {
            tie(u, v) = queue.front();
            queue.pop();

            if (v == 1) {
                k--;
                if (k == 0) { return u; }
                continue;
            }

            if (v % 2 == 0) {
                queue.push({u, v / 2});
            } else {
                queue.push({u, 3 * v + 1});
            }
        }
        return 0;
    }
};

int main() {
    FastIO;
//    FileIO;
    Solution sol;
    cout << sol.getKth(1, 1000, 777);
    return 0;
}