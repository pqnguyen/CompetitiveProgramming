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

string LongestCommonSubsequense(string x, string y) {
    int n = x.length();
    int m = y.length();
    int a[MAX][MAX] = {0};
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++) {
            if (x[i - 1] == y[j - 1] && i != j) {
                a[i][j] = a[i - 1][j - 1] + 1;
            } else {
                a[i][j] = max(a[i - 1][j], a[i][j - 1]);
            }
        }
    string res;
    int i = n;
    int j = m;
    while (i > 0 && j > 0) {
        if (a[i][j] == a[i - 1][j - 1] + 1) {
            res = x[i - 1] + res;
            i--;
            j--;
        } else if (a[i][j] == a[i - 1][j]) {
            i--;
        } else {
            j--;
        }
    }
    return res;
}

string LongestRepeatedSubsequence(string str) {
    return LongestCommonSubsequense(str, str);
}

int main() {
    FastIO;
    FileIO;
    string str = "AABEBCDD";
    cout << LongestRepeatedSubsequence(str);
    return 0;
}