#include <stdio.h>

int missingMultiple(int nums[], int n, int k) {
    int multiple = k;

    while (1) {
        int found = 0;

        for (int i = 0; i < n; i++) {
            if (nums[i] == multiple) {
                found = 1;
                break;
            }
        }

        if (!found) {
            return multiple;
        }

        multiple += k;
    }
}

int main() {
    int n, k;
    int nums[100];

    printf("Enter array size: ");
    scanf("%d", &n);

    printf("Enter array elements: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &nums[i]);
    }

    printf("Enter k: ");
    scanf("%d", &k);

    int result = missingMultiple(nums, n, k);

    printf("Smallest missing multiple: %d\n", result);

    return 0;
}
