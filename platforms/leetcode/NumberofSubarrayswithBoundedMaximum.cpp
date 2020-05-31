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

int numSubarrayBoundedMax(vector<int>& A, int L, int R) {
    int prev = -1, dp = 0, res = 0;

    for (int i = 0; i < A.size(); i++) {
        if (A[i] >= L && A[i] <= R) {
            dp = i - prev;
        }
        else if (A[i] > R) {
            dp = 0;
            prev = i;
        }
        res += dp;
    }

    return res;
}

int main() {
    FastIO;
    FileIO;
    int a[] = {2, 1, 4, 3};
    vector<int > A(a, a + 4);
    cout << numSubarrayBoundedMax(A, 2, 3);
    return 0;
}