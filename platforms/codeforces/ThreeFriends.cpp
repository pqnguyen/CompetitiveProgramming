#include <bits/stdc++.h>
 
using namespace std;
 
#define FastIO ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define FileIO freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout)

int cal_pairwise(vector<int> &pos) {
    return abs(pos[0] - pos[1]) + abs(pos[0] - pos[2]) + abs(pos[1] - pos[2]);
}

void solve(vector<int> &a, int i, vector<int> &pos, int& res) {
    if (i >= a.size()) {
        res = min(res, cal_pairwise(pos));
        return;
    }
    for (int d : {-1, 0, 1}) {
        pos.push_back(a[i] + d);
        solve(a, i + 1, pos, res);
        pos.pop_back();
    }
} 

int main() {
    FastIO;
    FileIO;
    int n, a, b, c, res;
    cin >> n;
    while (n--) {
        cin >> a >> b >> c;
        res = INT32_MAX;
        vector<int> arr = {a, b, c};
        vector<int> pos;
        solve(arr, 0, pos, res);
        cout << res << endl;
    }
    return 0;
}