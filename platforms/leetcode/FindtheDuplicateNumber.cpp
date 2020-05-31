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

int findDuplicate(vector<int>& nums) {
    int fast, slow;
    fast = slow = 0;
    while (true) {
        fast = nums[nums[fast]];
        slow = nums[slow];
        if (fast == slow) break;
    }
    slow = 0;
    while (fast != slow) {
        fast = nums[fast];
        slow = nums[slow];
    }
    return fast;
}

int main() {
    FastIO;
    FileIO;
    int a[] = {1,3,4,2,2};
    vector<int> v(a, a + 5);
    cout << findDuplicate(v);
    return 0;
}