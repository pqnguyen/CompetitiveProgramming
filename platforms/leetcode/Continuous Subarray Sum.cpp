/**
* @author Phan Quang Nguyen
* @Email pqnguyen1996@gmail.com
* @Github https://github.com/pqnguyen
*/

#include <bits/stdc++.h>
#include <cmath>

using namespace std;

typedef long long ll;

#define FastIO ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define FileIO freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout)

bool checkSubarraySum(vector<int>& nums, int k) {
    vector<int> dp(nums.size() + 1, 0);
    for (int i = 1; i < dp.size(); i++) dp[i] = nums[i - 1] + dp[i - 1];
    for (int gap = 2; gap < dp.size(); gap++)
        for (int i = 0 + gap; i < dp.size(); i++) {
            if (k == 0 && dp[i] - dp[i - gap] == 0) return true;
            else if (k != 0 && (dp[i] - dp[i - gap]) % k == 0) return true;
        }
    return false;
}

int main() {
    FastIO;
    FileIO;
    int a[] = {23, 2, 6, 4, 7};
    int k = 0;
    std::vector<int> nums(a, a + 5);
    cout << checkSubarraySum(nums, k);
    return 0;
}









