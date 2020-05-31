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

int longestIncreasingSubsequence(int a[MAX], int n) {
    vector<int> lis(n, 1);
    for(int i = 0; i < n; i++)
        for (int j = 0; j < i; j++)
            if (a[i] > a[j] && lis[i] < lis[j] + 1)
                lis[i] = lis[j] + 1;
    return *max_element(lis.begin(), lis.end());
}

int main() {
    FastIO;
    FileIO;
    int a[] = {10, 22, 9, 33, 21, 50, 41, 60};
    int n = sizeof(a) / sizeof(a[0]);
    cout << longestIncreasingSubsequence(a, n);
    return 0;
}











