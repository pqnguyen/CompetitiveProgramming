#include <bits/stdc++.h>

using namespace std;

#define FastIO ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define FileIO freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout)

bool isPolygon(int a[][50], int n) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (a[i][j]) {
                if (i + 1 < n && a[i + 1][j] == 0 && (j + 1) < n && a[i][j + 1] == 0) {
                    return false;
                }
            }
    return true;
}

int main() {
    FastIO;
    FileIO;
    int t, n;
    char tmp;
    cin >> t;
    while (t--) {
        cin >> n;
        int a[50][50] = {0};
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                cin >> tmp;
                a[i][j] = (tmp == '0' ? 0 : 1);
            }
        if (isPolygon(a, n)) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}