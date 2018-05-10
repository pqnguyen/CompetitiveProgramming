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

const ll MAX = 1000;
const ll INF = 3 * 1e18 + 10;

#define Iterator unordered_map<ll, bool>::iterator
unordered_map<ll, bool> visited;
vector<ll> res;
ll a[MAX];
int n;
bool found = false;

void printResult() {
    for (int i = 0; i < res.size(); i++)
        cout << res[i] << " ";
}

void dfs(ll u) {
    if (found) return;
    Iterator it = visited.find(u);
    if (it == visited.end()) return;
    if (it->second) return;
    it->second = true;
    res.push_back(u);
    if (res.size() == n) {
        found = true;
        printResult();
        return;
    }
    if (u % 3 == 0) dfs(u / 3);
    if (u <= INF) dfs(u * 2);
    it->second = false;
    res.pop_back();
}

int main() {
    FastIO;
    // FileIO;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        visited[a[i]] = false;
    }
    res.reserve(MAX);
    for (int i = 0; i < n; i++)
        dfs(a[i]);
    return 0;
}