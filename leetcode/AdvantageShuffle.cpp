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

bool option(pair<int , int> &a, pair<int , int> &b) {
    return a.first < b.first;
}

vector<int> advantageCount(vector<int>& A, vector<int>& B) {
    sort(A.begin(), A.end());
    vector<pair<int , int> > temp;
    for (int i = 0; i < B.size(); i++) temp.push_back(pair<int , int>(B[i], i));
    sort(temp.begin(), temp.end(), option);

    vector<int> res(A.size(), 0);
    queue<int> q;
    int j = 0;
    for (int e : A)
        if (e > temp[j].first) {
            res[temp[j].second] = e;
            j++;
        } else {
            q.push(e);
        }

    for (int i = 0; i < res.size(); i++)
        if (res[i] == 0) {
            res[i] = q.front();
            q.pop();
        }

    return res;
}

int main() {
    FastIO;
    FileIO;
    int a[] = {12,24,8,32};
    vector<int > A(a, a + 4);

    int b[] = {13,25,32,11};
    vector<int > B(b, b + 4);
    vector<int> res = advantageCount(A, B);
    for (int e : res) cout << e << " ";
    return 0;
}