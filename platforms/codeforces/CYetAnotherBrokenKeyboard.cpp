#include <bits/stdc++.h>
 
using namespace std;
 
#define FastIO ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define FileIO freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout)

int main() {
    FastIO;
    FileIO;
    int n, k;
    string s;
    cin >> n >> k >> s;
    char key;
    unordered_set<char> keys;
    while (k--) {
        cin >> key;
        keys.insert(key);
    }

    long long res = 0;
    for (int i = 0, j = 0; i <= s.length(); i++) {
        if (i == s.length() || keys.find(s[i]) == keys.end()) {
            n = i - j;
            res += (long long)n * (n + 1) / 2;
            j = i + 1;
        }
    }
    cout << res;
    return 0;
}