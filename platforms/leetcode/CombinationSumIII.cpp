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

const ll MAX = 100;
const ll INF = 1e14 + 100;

vector<vector<int> >res;

void utils(vector<int> a, int index, int first, int n) {
    if (index == a.size()) {
        if (n == 0) res.push_back(a);
        return;
    }
    for (int i = first; i <= 9; i++) {
        a[index] = i;
        utils(a, index + 1, i + 1, n - i);
    }
}

vector<vector<int> > combinationSum3(int k, int n) {
    vector<int> a(k, 0);
    utils(a, 0, 1, n);
    return res;
}

int main() {
    FastIO;
    FileIO;
    int a[] = {2, 0, 1};
    vector<int> v(a, a + 3);
    combinationSum3(3, 15);
    for (vector<int> arr : res) {
        for (int e : arr) cout << e << " ";
        cout << endl;
    }
    return 0;
}