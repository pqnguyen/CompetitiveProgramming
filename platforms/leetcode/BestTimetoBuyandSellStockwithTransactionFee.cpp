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

vector<vector<int> >res;

// sold indicate selling stock, hold indicate buying stock
// sold[i] is you can sell stock ith or not
// hold[i] is you can boy stock ith or not

int maxProfit(vector<int>& prices, int fee) {
    if (prices.size() <= 1) return 0;
    vector<int> sold(prices.size(), 0), hold = sold;
    hold[0] = -prices[0];
    for (int i = 1; i < prices.size(); i++) {
        sold[i] = max(sold[i - 1], hold[i - 1] + prices[i] - fee);
        hold[i] = max(hold[i - 1], sold[i - 1] - prices[i]);
    }
    return sold.back();
}

int main() {
    FastIO;
    FileIO;
    int a[] = {1, 3, 2, 8, 4, 9};
    vector<int> v(a, a + 6);
    cout << maxProfit(v, 2);
    return 0;
}