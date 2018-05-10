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

const ll MAX = 200000 + 10;
const ll INF = 3 * 1e18 + 10;

int binarySearch(ll a[], int n, ll x) {
    int left, right, res;
    left = 0;
    right = n - 1;
    res = -1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (x < a[mid]) {
            right = mid - 1;
        } else {
            res = mid;
            left = mid + 1;
        }
    }
    return res;
}

int main() {
    FastIO;
    // FileIO;
    ll a[MAX], k[MAX];
    int n, q, alive, die;
    cin >> n >> q;
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < q; i++) cin >> k[i];
    for (int i = 1; i < n; i++) a[i] += a[i - 1];
    for (int i = 1; i < q; i++)
        if (k[i - 1] < a[n - 1]) {
            k[i] += k[i - 1];
        }
    for (int i = 0; i < q; i++) {
        die = binarySearch(a, n, k[i]);
        if (die != -1)
            alive = n - die - 1;
        else
            alive = n;
        if (alive == 0) cout << n << endl;
        else cout << alive << endl;
    }
    return 0;
}