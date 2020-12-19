#include <bits/stdc++.h>

using namespace std;

#define FastIO ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define FileIO freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout)

class Solution {
public:
    bool canReach(vector<int> &arr, int start) {
        vector<bool> visited(arr.size());
        queue<int> queue;
        queue.push(start);

        while (queue.size()) {
            int index = queue.front();
            queue.pop();

            if (arr[index] == 0) { return true; }
            if (index + arr[index] < arr.size() && !visited[index + arr[index]]) {
                queue.push(index + arr[index]);
                visited[index + arr[index]] = true;
            }
            if (index - arr[index] >= 0 && !visited[index - arr[index]]) {
                queue.push(index - arr[index]);
                visited[index - arr[index]] = true;
            }
        }
        return false;
    }
};

int main() {
    FastIO;
//    FileIO;
    Solution sol;
    return 0;
}