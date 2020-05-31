#include <bits/stdc++.h>
 
using namespace std;
 
#define FastIO ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define FileIO freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout)

string solve(const string& s) {
    int l, r, u, d;
    l = r = u = d = 0;
    for (char ch : s) {
        switch (ch) {
            case 'L': l++; break;
            case 'R': r++; break;
            case 'U': u++; break;
            case 'D': d++; break;
        }
    }
    string res = string(min(l, r), 'L') + string(min(u, d), 'U') + string(min(l, r), 'R') + string(min(u, d), 'D');
    if (res.find('L') != string::npos && res.find('U') != string::npos) {
        return res;
    } else if (res.find('L') != string::npos) {
        return "LR";
    } else if (res.find('U') != string::npos) {
        return "UD";
    }
    return "";
}

int main() {
    FastIO;
    FileIO;
    int n = 0;
    string s;
    cin >> n;
    while (n--) {
        cin >> s;
        string res = solve(s);

        cout << res.length() << endl << res;
        if (n) cout << endl;
    }
    return 0;
}