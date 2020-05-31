/**
* @author Phan Quang Nguyen
* @Email pqnguyen1996@gmail.com
* @Github https://github.com/pqnguyen
*/

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define FastIO ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define FileIO freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout)

#define Rep(var, a, b) for (int var = a; var <= b; var++)
#define For(var, a, b) for (int var = a; var < b; var++)
#define Forr(var, a, b) for (int var = a; var >= b; var--)
#define Foreach(it,a) for(__typeof(a.begin()) it = a.begin(); it != a.end(); ++it)

#define db(x) { cout << #x << " = " << x << endl; }

#define pii pair<ll, int>
#define pll pair<int, int>
#define mk(x, y) make_pair(x, y)

const ll MAX = 100;
const ll INF = 3 * 1e18 + 10;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        dfs(res, "", n, 0, 0);
        return res;
    }

    void dfs(vector<string> &res, string str, int n, int open, int close) {
        if (open == n && close == n) {
            res.push_back(str);
            return;
        } 
        if (open < n) {
            dfs(res, str + "(", n, open + 1, close);
        }
        if (close < open) {
            dfs(res, str + ")", n, open, close + 1);
        }
    }
};

int main() {
    FastIO;
    FileIO;
    Solution solution;
    vector<string> res = solution.generateParenthesis(3);
    for (string s : res)
        cout << s << endl;
    return 0;
}











