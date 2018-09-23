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

vector<int> findDuplicates_v1(vector<int>& nums) {
    vector<int> res;
    set<int> s;
    for (int e : nums) {
        if (s.find(e) != s.end()) {
            res.push_back(e);
        } else {
            s.insert(e);
        }
    }
    return res;
}

vector<int> findDuplicates_v2(vector<int>& nums) {
    vector<int> res;
    for (int e : nums) {
        int index = abs(e) - 1;
        if (nums[index] < 0) {
            res.push_back(abs(e));
        } else {
            nums[index] = -nums[index];
        }
    }
    return res;
}

vector<int> findDuplicates(vector<int>& nums) {
    int n = nums.size() + 1;
    vector<int> res;
    for (int e : nums) {
        int index = e % n - 1;
        nums[index] += n;
    }
    for (int i = 0; i < nums.size(); i++)
    if (nums[i] / n > 1) {
        res.push_back(i + 1);
    }
    return res;
}

int main() {
    FastIO;
    FileIO;
    int a[] = {4,3,2,7,8,2,3,1};
    vector<int> v(a, a + 8);
    vector<int> res = findDuplicates(v);
    for (int e : res) cout << e << " ";
    return 0;
}