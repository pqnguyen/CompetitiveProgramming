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

int hashFunc(int a, int b, int c) {
    return a * 999999664 + b * 49 + c * 1000000000;  
}

vector<vector<int> > threeSum(vector<int>& nums) {
    vector< vector<int> > res;
    if (nums.size() < 2) return res;
    map<int, vector<int> > hash;
    sort(nums.begin(), nums.end());
    for (int i = 0; i < nums.size() - 2; i++) {
        int l = i + 1;
        int r = nums.size() - 1;
        while (l < r) {
           if (nums[i] + nums[l] + nums[r] < 0) l++;
           else if (nums[i] + nums[l] + nums[r] > 0) r--;
           else {
            vector<int> tmp;
            tmp.push_back(nums[i]);
            tmp.push_back(nums[l]);
            tmp.push_back(nums[r]);
            hash[hashFunc(nums[i], nums[l], nums[r])] = tmp;
            l++;
            r--;
           }
        }
    }
    for (map<int, vector<int> >::iterator it = hash.begin(); it != hash.end(); it++) {
        res.push_back(it->second);
    }
    return res;
}

int main() {
    FastIO;
    FileIO;
    int a[] = {};
    vector<int> data(a, a + 0);
    vector< vector<int> > res = threeSum(data);
    for (vector<int> item : res) {
        for (int e : item) cout << e << " ";
        cout << endl;
    }
    return 0;
}









