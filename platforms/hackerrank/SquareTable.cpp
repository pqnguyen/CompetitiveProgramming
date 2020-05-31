#include <bits/stdc++.h>

using namespace std;

#define FastIO ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define FileIO freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout)

// Complete the matchingStrings function below.
vector<int> matchingStrings(vector<string> strings, vector<string> queries) {
    unordered_map<string, int> freq;
    for (auto s : strings) {
        freq[s]++;
    }
    vector<int> res;
    for (auto s : queries) {
        res.push_back(freq[s]);
    }
    return res;
}

int main() {
    FastIO;
    FileIO;
    return 0;
}