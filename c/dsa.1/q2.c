#include<stdio.h>
int main(){
    int arr[]={2,3,4,5,6};
    int i;
    printf("The original array elements are: \n");
    for(i=0;i<5;i++){
        printf("%d\n",arr[i]);
    }
    printf("Using for loop :\n");
    for(i=0;i<5;i++){
        arr[i]=arr[i]+10;
        printf("%d\n",arr[i]);
    }
    printf("Using while loop :\n");
    i=0;
    while(i<5){
        arr[i]=arr[i]+5;
        printf("%d\n",arr[i]);
        i++;
    }
    return 0;
}