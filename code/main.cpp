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

const ll MAX = 2 * 1e5 + 10;
const ll INF = 3 * 1e18 + 10;

void dfs(vector<int> graph[], bool visited[], int u, bool &isCycle) {
    visited[u] = true;
    if (graph[u].size() != 2) {
        isCycle = false;
    }
    for (int i = 0; i < graph[u].size(); i++) {
        int v = graph[u][i];
        if (!visited[v]) {
            dfs(graph, visited, v, isCycle);
        }
    }
}

int main() {
    FastIO;
    // FileIO;
    vector<int> graph[MAX];
    bool visited[MAX] = {0};
    int n, m, u, v, count = 0;

    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        cin >> u >> v;
        u--;
        v--;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    for (int i = 0; i < n; i++)
        if (!visited[i]) {
            bool isCycle = true;
            dfs(graph, visited, i, isCycle);
            if (isCycle) count++;
        }
    cout << count;
    return 0;
}