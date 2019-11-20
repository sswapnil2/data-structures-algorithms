#include <iostream>
using namespace std;

struct Node
{
    int data;
    struct Node *next;
};

void push(Node **head, int data)
{
    // create new node
    // set data of node to data
    Node *newNode = new Node();
    newNode->data = data;
    newNode->next = NULL;

    if (!newNode)
    {
        cout << "Error creating node"
             << "\n";
        return;
    }
    // enter on first position
    newNode->next = *head;
    *head = newNode;
}

int pop(Node **head)
{
    int data;
    Node *temp;

    // check if any value is present in head
    if (*head == NULL)
    {
        cout << "Underflow condition"
             << "\n";
        return 0;
    }

    // first make temp point to head
    temp = *head;
    *head = (*head)->next;
    data = temp->data;
    free(temp);
    return data;
}

void printList(Node **head)
{
    Node *temp;
    // for (temp = *head; temp != NULL; temp = temp->next)
    // {
    //     cout << "hello"
    //          << " ";
    // }
    // cout << temp->data << "\n";
    // cout << temp->next->data << "\n";
    // cout << "\n";
    // cout << temp->data;
    temp = *head;
    while (temp != NULL)
    {
        cout << temp->data
             << "-->";
        temp = temp->next;
        /* code */
    }
    cout << "\n";
}

int main()
{
    Node *head = NULL;
    push(&head, 10);
    push(&head, 32);
    printList(&head);
    pop(&head);
    printList(&head);
    pop(&head);
    printList(&head);
    push(&head, 40);
    printList(&head);
    push(&head, 85);
    printList(&head);
    push(&head, 25);
    printList(&head);
    push(&head, 36);
    printList(&head);
    pop(&head);

    printList(&head);
    return 0;
}