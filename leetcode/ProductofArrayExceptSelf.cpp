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

vector<int> productExceptSelf(vector<int>& nums) {
    vector<int> res(nums.size(), 1);
    int product = 1;
    for (int i = 0; i < nums.size(); i++) {
        res[i] *= product;
        product *= nums[i];
    }

    product = 1;
    for (int i = nums.size() - 1; i >= 0; i--) {
        res[i] *= product;
        product *= nums[i];
    }
    return res;
}

int main() {
    FastIO;
    FileIO;
    int a[] = {1,2,3,4};
    vector<int> v(a, a + 4);
    vector<int> res = productExceptSelf(v);
    for (int e : res) cout << e << " ";
    return 0;
}