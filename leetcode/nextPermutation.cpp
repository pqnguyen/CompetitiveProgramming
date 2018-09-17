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
    void nextPermutation(vector<int> &a) {
        if (a.size() == 0) return;
        int i = a.size() - 1;
        while (i > 0 && a[i - 1] >= a[i]) i--;
        if (i != 0) {
            int j = a.size() - 1;
            while (a[j] <= a[i - 1]) j--;
            swap(a[i - 1], a[j]);
        }
        sort(a.begin() + i, a.end());
    }
};

int main() {
    FastIO;
    FileIO;
    int tmp[] = {1, 2, 3, 4};
    vector<int> a(tmp, tmp + 4);
    Solution sol;
    sol.nextPermutation(a);
    for (int e : a) cout << e << " ";
    return 0;
}











