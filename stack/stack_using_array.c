#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 10

struct Stack
{
    int capacity;
    int top;
    int *array;
};

int isEmpty(struct Stack *s)
{
    return s->top == -1;
}

int isFull(struct Stack *s)
{
    return s->top == MAX_SIZE - 1;
}

void push(struct Stack *s, int data)
{
    if (isFull(s))
    {
        printf("stack overflow \n");
    }
    else
    {
        s->array[++s->top] = data;
    }
}

int pop(struct Stack *s)
{
    if (isEmpty(s))
    {
        printf("Stack Underflow \n");
    }
    else
    {
        return s->array[s->top--];
    }
}

void print_stack(struct Stack *s)
{
    for (int i = s->top; i >= 0; --i)
    {
        printf("%d ->", s->array[i]);
    }
    printf("\n");
}

int main()
{
    struct Stack *s = malloc(sizeof(struct Stack));
    s->top = -1;
    s->capacity = MAX_SIZE;
    s->array = (int *)malloc(sizeof(int) * s->capacity);
    push(s, 10);
    push(s, 20);
    print_stack(s);
    pop(s);
    print_stack(s);
    return 0;
}