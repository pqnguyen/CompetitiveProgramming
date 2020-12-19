#include <bits/stdc++.h>

using namespace std;

#define FastIO ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define FileIO freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout)

bool isBalanced(string s) {
    stack<char> brackets;
    for (char ch : s) {
        if (ch == '}' || ch == ']' || ch == ')') {
            if (!brackets.size()) { return false; }
            if (ch == '}' && brackets.top() != '{') { return false; }
            if (ch == ']' && brackets.top() != '[') { return false; }
            if (ch == ')' && brackets.top() != '(') { return false; }
            brackets.pop();
        } else {
            brackets.push(ch);
        }
    }
    return brackets.size() == 0;
}

int main() {
    FastIO;
    FileIO;
    int n;
    string s;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    while (n--) {
        getline(cin, s);
        if (isBalanced(s)) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}