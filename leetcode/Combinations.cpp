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

int k, n;
vector<vector<int> > res;

void combine(vector<int> set, int nChoose, int prevEle) {
    if (nChoose == k) {
        res.push_back(set);
    } else {
        for (int i = prevEle + 1; i <= n - (k - nChoose - 1); i++) {
            set[nChoose] = i;
            combine(set, nChoose + 1, i);
        }
    }
}

vector<vector<int> > combine(int n, int k) {
    vector<int> set(k, 0);
    combine(set, 0, 0);
    return res;
}

int main() {
    FastIO;
    FileIO;
    n = 4;
    k = 3;
    vector<vector<int> > res = combine(n, k);
    for (vector<int> e : res) {
        for (int item : e) cout << item << " ";
        cout << endl;
    }
    return 0;
}









