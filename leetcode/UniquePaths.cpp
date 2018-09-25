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

const ll MAX = 100;
const ll INF = 1e14 + 100;

int uniquePaths(int m, int n) {
    int a[MAX][MAX] = {0};
    a[0][0] = 1;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            if (i - 1 >= 0) a[i][j] += a[i - 1][j];
            if (j - 1 >= 0) a[i][j] += a[i][j - 1];
        }       
    return a[n - 1][m - 1];
}

int main() {
    FastIO;
    FileIO;
    int a[] = {1,3,4,2,2};
    vector<int> v(a, a + 5);
    cout << uniquePaths(7, 3);
    return 0;
}