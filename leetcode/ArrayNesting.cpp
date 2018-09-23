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

int arrayNesting(vector<int>& nums) {
    int res = 0;
    for (int i = 0; i < nums.size(); i++) {
        int k = i, len = 0;
        while (nums[k] != -1) {
            int tmp = k;
            k = nums[k];
            nums[tmp] = -1; 
            len++;
        }
        res = max(res, len);
    }   
    return res;
}

int main() {
    FastIO;
    FileIO;
    int a[] = {5,4,0,3,1,6,2};
    vector<int> v(a, a + 7);
    cout << arrayNesting(v);
    return 0;
}