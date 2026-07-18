#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};

struct node *top = NULL;
void push(int value) {
    struct node *newNode;
    newNode = (struct node*)malloc(sizeof(struct node));

    newNode->data = value;
    newNode->next = top;
    top = newNode;

    printf("Element %d pushed into stack\n", value);
}
void pop() {
    struct node *temp;

    if(top == NULL) {
        printf("Stack Underflow\n");
    } else {
        temp = top;
        printf("Deleted element: %d\n", top->data);
        top = top->next;
        free(temp);
    }
}
void display() {
    struct node *temp;

    if(top == NULL) {
        printf("Stack is empty\n");
    } else {
        temp = top;
        printf("Stack elements are:\n");
        while(temp != NULL) {
            printf("%d\n", temp->data);
            temp = temp->next;
        }
    }
}

int main() {
    int choice, value;

    while(1) {
        printf("\n1.Push\n2.Pop\n3.Display\n4.Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
                printf("Enter value: ");
                scanf("%d", &value);
                push(value);
                break;

            case 2:
                pop();
                break;

            case 3:
                display();
                break;

            case 4:
                exit(0);

            default:
                printf("Invalid choice\n");
        }
    }
}