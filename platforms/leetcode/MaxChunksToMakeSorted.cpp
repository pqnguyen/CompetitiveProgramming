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

int maxChunksToSorted(vector<int>& arr) {
    int chunks = 0;
    int rightIndex = -1;
    for (int i = 0; i < arr.size(); i++) {
        rightIndex = max(arr[i], rightIndex);
        if (i == rightIndex) {
            chunks++;
        }
    }
    return chunks;
}

int main() {
    FastIO;
    FileIO;
    int a[] = {2, 0, 1};
    vector<int> v(a, a + 3);
    cout << maxChunksToSorted(v);
    return 0;
}