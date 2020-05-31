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

int lenLongestFibSubseq(vector<int>& A) {
    unordered_set<int> set(A.begin(), A.end());
    int res = 0;
    for (int i = 0; i < A.size() - 1; i++)
        for (int j = i + 1; j < A.size(); j++) {
            int a = A[i], b = A[j], len = 0, tmp;
            while (set.find(a + b) != set.end()) {
                tmp = b;
                b = a + b;
                a = tmp;
                len++;
            }
            res = max(res, len);
        }
    
    return res > 2 ? res : 0;
}

int main() {
    FastIO;
    FileIO;
    int a[] = {1, 3, 5};
    vector<int > A(a, a + 3);
    cout << lenLongestFibSubseq(A);
    return 0;
}