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

void print(vector<int>& nums) {
    for (int i = 0; i < nums.size(); i++) cout << nums[i];
    cout << endl;
}

vector<int> getPermitation(vector<int> &origin, vector<int> tmp) {
    vector<int> res(origin.size());
    for (int i = 0; i < origin.size(); i++) res[i] = origin[tmp[i]];
    return res;
}

vector<vector<int> > permute(vector<int>& nums) {
    vector<vector<int> > res;
    vector<int> tmp(nums.size());
    for (int i = 0; i < tmp.size(); i++) tmp[i] = i;
    while (true) {
        res.push_back(getPermitation(nums, tmp));
        int i = tmp.size() - 2;
        while (i >= 0 && tmp[i] > tmp[i + 1]) i--;
        if (i < 0) break;
        int j = tmp.size() - 1;
        while (j > i && tmp[j] < tmp[i]) j--;
        swap(tmp[i], tmp[j]);
        sort(tmp.begin() + i + 1, tmp.end());
    }   
    return res;
}

int main() {
    FastIO;
    FileIO;
    int a[] = {0, -1, 1};    
    vector<int> ls(a, a + 3);
    vector<vector<int> > res = permute(ls);
    for (vector<int> tmp : res) print(tmp);
    return 0;
}









