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

const int MAX = 1e9 + 10;
const int INF = 1e4 + 100;

int findLength(vector<int>& A, vector<int>& B) {
    vector<int> dp(A.size() + 1, 0);
    int res = 0;
    for (int i = A.size() - 1; i >= 0; i--)
        for (int j = 0; j < B.size(); j++)
            res = max(res, dp[j] = A[i] == B[j] ? 1 + dp[j + 1] : 0);

    return res;
}

int main() {
    FastIO;
    FileIO;
    int a[] = {1,2,3,2,1};
    vector<int> A(a, a + 5);
    int b[] = {3,2,1,4,7};
    vector<int> B(b, b + 5);
    cout << findLength(A, B);
    return 0;
}