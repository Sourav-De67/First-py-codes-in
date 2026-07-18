#include<stdio.h>
int main(){
    int arr[5]={10,20,30,40,50};
    int index;
    printf("Enter the index between o and 4 to access the array element: ");
    scanf("%d",&index);
    if(index>=0&&index<5){
        printf("Element at index %d:%d\n",index,arr[index]);
    }else{
        printf("Invalid index!Please enter a number between 0 and 4\n");
    }
    return 0;
}