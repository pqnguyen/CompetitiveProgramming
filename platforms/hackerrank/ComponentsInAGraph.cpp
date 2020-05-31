#include <bits/stdc++.h>

using namespace std;

#define FastIO ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define FileIO freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout)

int findParent(vector<int> &a, int u) {
    if (a[u] < 0) {
        a[u] = findParent(a, a[u]);
        return a[u];
    }
    return u;
}

void unionSet(vector<int> &a, int u, int v) {
    int parentU = findParent(a, u);
    int parentV = findParent(a, v);
    if (parentU != parentV) {
        if (a[parentU] > a[parentV]) {
            swap(parentU, parentV);
        }
        a[parentU] += a[parentV];
        a[parentV] = parentU;
    }
}

vector<int> componentsInGraph(vector<vector<int>> gb) {
    int n = gb.size();
    vector<int> a(2 * n);
    for (vector<int> &edge : gb) {
        a[edge[0]] = a[edge[1]] = -1;
    }
    for (vector<int> &edge : gb) {
        unionSet(a, edge[0], edge[1]);
    }
    int smallest = INT_MAX, largest = INT_MIN;
    for (int s : a) {
        if (s < 0) {
            smallest = min(smallest, -s);
            largest = max(largest, -s);
        }
    }
    return {smallest, largest};
}

int main() {
    FastIO;
    FileIO;
    int n, u, v;
    cin >> n;
    vector<vector<int>> edges;
    while (n--) {
        cin >> u >> v;
        edges.push_back({u, v});
    }
    vector<int> res = componentsInGraph(edges);
    cout << res[0] << " " << res[1];
    return 0;
}