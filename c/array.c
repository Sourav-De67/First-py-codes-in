#include<stdio.h>
int main(){
    int i,n;
    int max,min;
    int arr[100];
    printf("Enter the array size:");
    scanf("%d",&n);
    printf("The elements are:\n");
    for(i=0;i<n;i++){
        scanf("%d",arr[i]);
    }
    max=min=arr[0];
    for(i=1;i<n;i++){
        if(arr[i]>max)
        max=arr[i];
        if(arr[i]<min)
        min=arr[i];
    }
    printf("Largest element is:%d",max);
    printf("Smallest element is:%d",min);
    return 0;
}