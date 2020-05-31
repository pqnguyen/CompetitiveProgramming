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

int findPeakElement(vector<int>& nums) {
    int left = 0, right = nums.size() - 1;
    while (left < right) {
        int mid = (left + right) / 2;
        if (mid < nums.size() && nums[mid] < nums[mid + 1]) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return left;
}

int main() {
    FastIO;
    FileIO;
    int a[] = {1,2,3,1};
    vector<int > A(a, a + 4);

    cout << findPeakElement(A);
    return 0;
}