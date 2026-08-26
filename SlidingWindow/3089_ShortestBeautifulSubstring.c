#include <stdio.h>
#include <string.h>

char* shortestBeautifulSubstring(char* s, int k) {
    static char ans[101];
    int n = strlen(s);
    int minLen = n + 1;

    ans[0] = '\0';

    for (int i = 0; i < n; i++) {
        int ones = 0;

        for (int j = i; j < n; j++) {
            if (s[j] == '1')
                ones++;

            if (ones == k) {
                int len = j - i + 1;

                if (len < minLen) {
                    minLen = len;

                    strncpy(ans, s + i, len);
                    ans[len] = '\0';
                }
                else if (len == minLen) {
                    char temp[101];

                    strncpy(temp, s + i, len);
                    temp[len] = '\0';

                    if (strcmp(temp, ans) < 0) {
                        strcpy(ans, temp);
                    }
                }

                break;
            }
        }
    }

    return ans;
}
