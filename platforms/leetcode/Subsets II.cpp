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

void print(std::vector<int> v) {
    for (int e : v) cout << e;
    cout << endl;
}

vector<int> getSubset(const vector<int> &nums, int n) {
    vector<int> res;
    int i = 0;
    while (n > 0) {
        if ((n & 1) == 1) res.push_back(nums[i]);
        i++;
        n >>= 1;
    }
    return res;
}

string join(vector<int> &nums) {
    sort(nums.begin(), nums.end());
    string res = "";
    for (int i = 0; i < nums.size(); i++) res += to_string(nums[i]) + ",";
    return res;
}

vector<vector<int> > subsetsWithDup(vector<int>& nums) {
    map<string, bool> unique;
    vector<vector<int> > res;
    int end = pow(2, nums.size());
    for (int i = 0; i < end; i++) {
        vector<int> tmp = getSubset(nums, i);
        string str = join(tmp);
        if (unique.find(str) == unique.end()) {
            unique[str] = true;
            res.push_back(tmp);
        }
    }
    return res;
}

int main() {
    FastIO;
    FileIO;
    int a[] = {4,4,4,1,4};    
    vector<int> ls(a, a + 5);
    vector<vector<int> > res = subsetsWithDup(ls);
    for (vector<int> tmp : res) print(tmp);
    return 0;
}









