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

const int MAX = 1000;
const int INF = 1e4 + 100;

int leastInterval(vector<char>& tasks, int n) {
    vector<int> count(26, 0);
    for (char c : tasks) count[c - 'A']++;
    sort(count.begin(), count.end(), greater<int>());
    int index = 0;
    int res = 0;
    while (count[index]) {
        res = max(res, index + (count[index] - 1) * (n + 1));
        index++;
    }
    return max(res + 1, (int)tasks.size());
}

int main() {
    FastIO;
    FileIO;
    char a[] = {'A','B'};
    vector<char> v(a, a + 2);
    cout << leastInterval(v, 2);
    return 0;
}