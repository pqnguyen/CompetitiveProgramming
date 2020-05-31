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
const ll INF = 1e14 + 100;

int main() {
    FastIO;
    // FileIO;
    int n;
    string str;
    cin >> n;
    cin.ignore();
    cin >> str;
    map<string, int> cnt;
    map<string, int>::iterator it;

    int m = 0;
    string res;
    for (int i = 0; i < n - 1; i++) {
        string twoGrams = str.substr(i, 2);
        it = cnt.find(twoGrams);
        if (it == cnt.end()) {
            cnt[twoGrams] = 1;
        } else {
            it->second++;
        }
        if (cnt[twoGrams] > m) {
            m = cnt[twoGrams];
            res = twoGrams;
        }
    }
    cout << res;

    return 0;
}