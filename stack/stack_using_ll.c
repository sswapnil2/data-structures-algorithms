#include <stdio.h>
#include <stdlib.h>

struct ListNode
{
    int data;
    struct ListNode *next;
};

void push(struct ListNode **head, int data)
{
    struct ListNode *temp = malloc(sizeof(struct ListNode));
    temp->data = data;
    temp->next = *head;
    *head = temp;
}

int pop(struct ListNode **head)
{
    struct ListNode *temp;
    if (!head)
    {
        printf("Stack Underflow\n");
    }
    else
    {
        temp = *head;
        *head = temp->next;
        int value = temp->data;
        free(temp);
        return value;
    }
}

void print_stack(struct ListNode *head)
{
    struct ListNode *temp = head;
    while (temp)
    {
        printf("%d =>", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main()
{
    struct ListNode *head = NULL;
    push(&head, 10);*head->next;
    push(&head, 20);
    print_stack(head);
    return 0;
}