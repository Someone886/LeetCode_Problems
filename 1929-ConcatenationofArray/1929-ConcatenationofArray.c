// Last updated: 4/26/2025, 2:14:49 PM
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getConcatenation(int* nums, int numsSize, int* returnSize) {
    *returnSize = 2 * numsSize;
    int *return_arr = malloc(sizeof(int) * (*returnSize));
    int i;

    for (i = 0; i < numsSize; i++){
        return_arr[i] = nums[i];
        return_arr[i + numsSize] = nums[i];
    }

    return return_arr;
}