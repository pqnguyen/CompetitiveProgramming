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
const ll INF = 3 * 1e18 + 10;

class Solution {
public:
    int searchMarkPos(vector<int> &nums) {
        int l = 0;
        int r = nums.size() - 1;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (mid > 0 && nums[mid] < nums[mid - 1]) return mid;
            if (nums[mid] >= nums[0]) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return -1;
    }

    int search(vector<int>& nums, int target) {
        switch (nums.size()) {
            case 0: return -1;
            case 1: if (nums[0] == target) return 0; else return -1;
        }
        int index = searchMarkPos(nums);
        int l = 0;
        int r = nums.size() - 1;
        if (index != -1) {
            if (target >= nums[0]) r = index - 1;
            else l = index;
        }
        while (l <= r) {
            int mid = (l + r) / 2;
            if (target == nums[mid]) return mid;
            if (target < nums[mid]) r = mid - 1;
            else l = mid + 1;
        }
        return -1;
    }
};

int main() {
    FastIO;
    FileIO;
    Solution solution;
    int a[] = {3, 1};
    vector<int> arr(a, a + 2);
    cout << solution.search(arr, 1);
    return 0;
}









