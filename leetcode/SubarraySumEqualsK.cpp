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

const int MAX = 1e9 + 10;
const int INF = 1e4 + 100;

int subarraySum(vector<int>& nums, int k) {
    map<int, int> presum;
    presum[0] = 1;
    
    int sum = 0, res = 0;
    for (int i = 0; i < nums.size(); i++) {
        sum += nums[i];
        if (presum.find(sum - k) != presum.end()) {
            res += presum[sum - k];
        }
        presum[sum] = presum[sum] + 1;
    }

    return res;
}

int main() {
    FastIO;
    FileIO;
    int a[] = {0};
    vector<int > A(a, a + 3);
    cout << subarraySum(A, 0);
    return 0;
}