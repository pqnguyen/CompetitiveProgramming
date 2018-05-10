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

const ll MAX = 2 * 1e5 + 1;
const ll INF = 1e14 + 100;

int main() {
    FastIO;
    // FileIO;
    int a[MAX], n, k;
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    sort(a, a + n);
    if (k != 0 && a[k - 1] != a[k]) 
        cout << a[k - 1];
    else if (k == 0 && a[0] > 1) cout << 1;
    else cout << -1;
    return 0;
}