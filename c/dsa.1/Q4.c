#include <stdio.h>
int main()
{
    int arr[100], n, pos, i;
    printf("Enter the number of element in the array: ");
    scanf("%d", &n);
    printf("Enter %d elements: \n", n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    printf("Enter the position(index)to delete(0-%d): ", n - 1);
    scanf("%d", &pos);
    if (pos < 0 || pos >= n)
    {
        printf("Invslid position!\n");
    }
    else
    {
        for (i = pos; i < n - 1; i++)
        {
            arr[i] = arr[i + 1];
        }
        n--;
        printf("Array after deletion: \n");
        for (i = 0; i < n; i++)
        {
            printf("%d\n", arr[i]);
        }
        printf("\n");
    }
    return 0;
}