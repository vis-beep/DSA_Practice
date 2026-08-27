#include <stdio.h>
#include <string.h>

char* lexGreaterPermutation(char* s, char* target) {
    static char ans[305];
    int n = strlen(s);

    int cnt[26] = {0};

    // Count characters in s
    for (int i = 0; i < n; i++) {
        cnt[s[i] - 'a']++;
    }

    // Try to match target from left to right
    for (int i = 0; i < n; i++) {
        int c = target[i] - 'a';

        // If target[i] is available, use it
        if (cnt[c] > 0) {
            cnt[c]--;
            ans[i] = target[i];
        } 
        else {
            // Cannot match target[i].
            // Try a character greater than target[i].
            int greater = -1;

            for (int j = c + 1; j < 26; j++) {
                if (cnt[j] > 0) {
                    greater = j;
                    break;
                }
            }

            if (greater != -1) {
                ans[i] = 'a' + greater;
                cnt[greater]--;

                // Put remaining characters in sorted order
                int pos = i + 1;

                for (int j = 0; j < 26; j++) {
                    while (cnt[j] > 0) {
                        ans[pos++] = 'a' + j;
                        cnt[j]--;
                    }
                }

                ans[n] = '\0';
                return ans;
            }

            // Need to backtrack
            for (int k = i - 1; k >= 0; k--) {

                // Restore character at position k
                cnt[ans[k] - 'a']++;

                int current = ans[k] - 'a';
                int next = -1;

                // Find smallest character greater than current
                for (int j = current + 1; j < 26; j++) {
                    if (cnt[j] > 0) {
                        next = j;
                        break;
                    }
                }

                if (next != -1) {
                    ans[k] = 'a' + next;
                    cnt[next]--;

                    // Fill remaining positions with smallest characters
                    int pos = k + 1;

                    for (int j = 0; j < 26; j++) {
                        while (cnt[j] > 0) {
                            ans[pos++] = 'a' + j;
                            cnt[j]--;
                        }
                    }

                    ans[n] = '\0';
                    return ans;
                }
            }

            return "";
        }
    }

    // s == target, so we need to find the next permutation
    for (int k = n - 1; k >= 0; k--) {

        // Restore current character
        cnt[ans[k] - 'a']++;

        int current = ans[k] - 'a';
        int next = -1;

        // Find smallest greater character
        for (int j = current + 1; j < 26; j++) {
            if (cnt[j] > 0) {
                next = j;
                break;
            }
        }

        if (next != -1) {
            ans[k] = 'a' + next;
            cnt[next]--;

            int pos = k + 1;

            for (int j = 0; j < 26; j++) {
                while (cnt[j] > 0) {
                    ans[pos++] = 'a' + j;
                    cnt[j]--;
                }
            }

            ans[n] = '\0';
            return ans;
        }
    }

    return "";
}
