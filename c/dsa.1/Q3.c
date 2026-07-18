#include <stdio.h>
int main()
{
    int arr[] = {10, 20, 30, 40, 50};
    int n = 5;
    int i, pos, value;
    printf("Original array :\n");
    for (i = 0; i < 5; i++)
    {
        printf("%d\n", arr[i]);
    }
    printf("Enter the position to insert(0-%d): \n", n);
    scanf("%d", &pos);
    printf("Enter the value to insert: ");
    scanf("%d", &value);
    for (i = n; i > pos; i--)
    {
        arr[i] = arr[i - 1];
    }
    arr[pos] = value;
    n++;
    printf("Array after insertion: \n");
    for (i = 0; i < n; i++)
    {
        printf("%d\n", arr[i]);
    }
    return 0;
}