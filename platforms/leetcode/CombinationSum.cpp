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

vector<vector<int> > res;
vector<int> arr;

void utils(vector<int>& candidates, int target, int index) {
    if (target < 0) return;
    if (target == 0) res.push_back(arr);
    for (int i = index; i < candidates.size(); i++) {
        arr.push_back(candidates[i]);
        utils(candidates, target - candidates[i], i);
        arr.pop_back();
    }
}

vector<vector<int> > combinationSum(vector<int>& candidates, int target) {
    utils(candidates, target, 0);
    return res;
}

int main() {
    FastIO;
    FileIO;
    int a[] = {2,3,5};
    vector<int> v(a, a + 3);
    combinationSum(v, 8);
    for (auto arr : res) {
        for(int e : arr) cout << e << " ";
        cout << endl;
    }
    return 0;
}