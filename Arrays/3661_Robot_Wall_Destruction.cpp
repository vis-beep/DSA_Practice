// Problem: Maximum Walls Destroyed by Robots
// Approach: DP + Binary Search
// Time Complexity: O(n log m)

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    typedef pair<int,int> P;

    vector<vector<int>> t;

    // Count walls in range [l, r]
    int countWalls(vector<int>& walls, int l, int r) {
        int left = lower_bound(walls.begin(), walls.end(), l) - walls.begin();
        int right = upper_bound(walls.begin(), walls.end(), r) - walls.begin();
        return right - left;
    }

    int solve(vector<int>& walls, vector<P>& roboDist, vector<P>& range, int i, int prevDir) {
        if (i == roboDist.size()) return 0;

        if (t[i][prevDir] != -1) return t[i][prevDir];

        int pos = roboDist[i].first;

        // LEFT
        int leftStart = range[i].first;
        if (prevDir == 1 && i > 0) {
            leftStart = max(leftStart, range[i-1].second + 1);
        }

        int leftTake = countWalls(walls, leftStart, pos) +
                       solve(walls, roboDist, range, i+1, 0);

        // RIGHT
        int rightTake = countWalls(walls, pos, range[i].second) +
                        solve(walls, roboDist, range, i+1, 1);

        return t[i][prevDir] = max(leftTake, rightTake);
    }

    int maxWalls(vector<int>& robots, vector<int>& distance, vector<int>& walls) {
        int n = robots.size();

        vector<P> roboDist(n);
        for (int i = 0; i < n; i++) {
            roboDist[i] = {robots[i], distance[i]};
        }

        sort(roboDist.begin(), roboDist.end());
        sort(walls.begin(), walls.end());

        vector<P> range(n);

        for (int i = 0; i < n; i++) {
            int pos = roboDist[i].first;
            int d = roboDist[i].second;

            int leftLimit = (i == 0) ? -1e9 : roboDist[i-1].first + 1;
            int rightLimit = (i == n-1) ? 1e9 : roboDist[i+1].first - 1;

            int L = max(pos - d, leftLimit);
            int R = min(pos + d, rightLimit);

            range[i] = {L, R};
        }

        t.assign(n, vector<int>(2, -1));

        return solve(walls, roboDist, range, 0, 0);
    }
};
