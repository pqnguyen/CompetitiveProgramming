/**
* @author Phan Quang Nguyen
* @Email pqnguyen1996@gmail.com
* @Github https://github.com/pqnguyen
*/

#include <stdc++.h>

using namespace std;

typedef long long ll;

#define FastIO ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define FileIO freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout)

#define Rep(var, a, b) for (int var = a; var <= b; var++)
#define For(var, a, b) for (int var = a; var < b; var++)
#define Forr(var, a, b) for (int var = a; var >= b; var--)
#define Foreach(it,a) for(__typeof(a.begin()) it = a.begin(); it != a.end(); ++it)

#define db(x) { cout << #x << " = " << x << endl; }

#define pii pair<int, int>
#define pll pair<ll, ll>
#define mk(x, y) make_pair(x, y)

const int MAX = 300005;
const ll INF = 3 * 1e18 + 10;

struct Segment {
    int index, first, second;
    bool inline operator < (const Segment &rhs) const {
        return (first < rhs.first || (first == rhs.first && second >= rhs.second));
    }
};

int main() {
    FastIO;
    FileIO;
    int n, l, r;
    Segment a[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d%d", &a[i].first, &a[i].second);
        a[i].index = i + 1;
    }
    sort(a, a + n);
    for (int i = 1; i < n; i++)
        if (a[i - 1].second >= a[i].second) {
            printf("%d %d", a[i].index, a[i - 1].index);
            return 0;
        }
    printf("-1 -1");
    return 0;
}