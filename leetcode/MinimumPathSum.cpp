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

#define db(x) { cout << #x << " = " << x << endl; }

#define pii pair<int , int>
#define pll pair<ll, ll>
#define mk(x, y) make_pair(x, y)

const int MAX = 1000;
const int INF = 1e4 + 100;

void initialize(int a[][MAX], int n, int m) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            a[i][j] = INF;
}

int minPathSum(vector<vector<int>>& grid) {
    int n = grid.size();
    int m = grid.front().size();
    int dp[MAX][MAX];
    initialize(dp, n, m);
    dp[0][0] = grid[0][0];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            if (i - 1 >= 0) dp[i][j] = min(dp[i][j], dp[i - 1][j] + grid[i][j]);
            if (j - 1 >= 0) dp[i][j] = min(dp[i][j], dp[i][j - 1] + grid[i][j]);
        }
    return dp[n - 1][m - 1];
}

int main() {
    FastIO;
    FileIO;
    return 0;
}