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

int findPoisonedDuration(vector<int>& timeSeries, int duration) {
    if (!timeSeries.size()) return 0;
    int res = duration;
    for (int i = 0; i < timeSeries.size() - 1; i++) {
        res += min(timeSeries[i + 1] - timeSeries[i], duration);
    }
    return res;
}

int main() {
    FastIO;
    FileIO;
    int a[] = {1, 2}, duration = 2;
    vector<int> v(a, a + 2);
    cout << findPoisonedDuration(v, 2);
    return 0;
}