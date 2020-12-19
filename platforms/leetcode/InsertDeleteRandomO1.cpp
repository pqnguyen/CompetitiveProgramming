#include <bits/stdc++.h>

using namespace std;

#define FastIO ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define FileIO freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout)

class RandomizedSet {
public:
    map<int, int> pos;
    vector<int> eles;

    /** Initialize your data structure here. */
    RandomizedSet() {
        /* initialize random seed: */
        srand(time(NULL));
    }

    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if (pos.find(val) != pos.end()) {
            return false;
        }
        pos[val] = eles.size();
        eles.push_back(val);
        return true;
    }

    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if (pos.find(val) == pos.end()) {
            return false;
        }

        int index = pos[val];
        eles[index] = eles[eles.size() - 1];
        pos[eles[index]] = index;

        pos.erase(val);
        eles.pop_back();
        return true;
    }

    /** Get a random element from the set. */
    int getRandom() {
        if (eles.size() == 0) { return 0; }
        return eles[rand() % eles.size()];
    }
};

int main() {
    FastIO;
//    FileIO;
    RandomizedSet sol;
    cout << sol.insert(0) << endl;
    cout << sol.getRandom() << endl;
    cout << sol.remove(0) << endl;
    cout << sol.insert(0) << endl;
    return 0;
}