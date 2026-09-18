#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * LeetCode 1520
 * Maximum Number of Non-Overlapping Substrings
 *
 * Approach:
 * 1. Find the first and last occurrence of every character.
 * 2. Build the smallest valid interval for each character.
 * 3. Sort intervals by their ending position.
 * 4. Greedily select non-overlapping intervals.
 *
 * Time Complexity: O(n + 26^2)
 * Space Complexity: O(26)
 */

char** maxNumOfSubstrings(char* s, int* returnSize) {
    int n = strlen(s);

    int first[26];
    int last[26];

    for (int i = 0; i < 26; i++) {
        first[i] = n;
        last[i] = -1;
    }

    // Find first and last occurrence of each character
    for (int i = 0; i < n; i++) {
        int c = s[i] - 'a';

        if (first[c] == n) {
            first[c] = i;
        }

        last[c] = i;
    }

    int left[26];
    int right[26];
    int count = 0;

    // Find smallest valid interval for each character
    for (int c = 0; c < 26; c++) {
        if (last[c] == -1) {
            continue;
        }

        int l = first[c];
        int r = last[c];
        int valid = 1;

        for (int i = l; i <= r; i++) {
            int x = s[i] - 'a';

            if (first[x] < l) {
                valid = 0;
                break;
            }

            if (last[x] > r) {
                r = last[x];
            }
        }

        if (valid) {
            left[count] = l;
            right[count] = r;
            count++;
        }
    }

    // Sort intervals by ending position
    for (int i = 0; i < count - 1; i++) {
        for (int j = i + 1; j < count; j++) {
            if (right[i] > right[j]) {
                int temp = right[i];
                right[i] = right[j];
                right[j] = temp;

                temp = left[i];
                left[i] = left[j];
                left[j] = temp;
            }
        }
    }

    // Greedily select non-overlapping intervals
    char** result = (char**)malloc(26 * sizeof(char*));

    *returnSize = 0;
    int end = -1;

    for (int i = 0; i < count; i++) {
        if (left[i] > end) {
            int length = right[i] - left[i] + 1;

            result[*returnSize] =
                (char*)malloc((length + 1) * sizeof(char));

            strncpy(result[*returnSize], s + left[i], length);
            result[*returnSize][length] = '\0';

            (*returnSize)++;
            end = right[i];
        }
    }

    return result;
}
