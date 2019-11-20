#include <stdio.h>
#include <stdlib.h>

struct DynamicArray
{
    int top;
    int capacity;
    int *array;
};

struct DynamicArray *createStack()
{
    struct DynamicArray *s = malloc(sizeof(struct DynamicArray));
    if (!s)
    {
        printf("Unable to allocate memory");
        return;
    }
    s->top = -1;
    s->capacity = 1;
    s->array = malloc(sizeof(int) * s->capacity);
    return s;
}

int isEmpty(struct DynamicArray *s)
{
    return s->top == -1;
}

int isFull(struct DynamicArray *s)
{
    return s->top == s->capacity - 1;
}

void reallocate_m(struct DynamicArray *s)
{
    s->capacity *= 2;
    s->array = realloc(s->array, sizeof(int) * s->capacity);
}

void push(struct DynamicArray *s, int data)
{
    // check if stack if full
    // if full reallocate memory
    if (isFull(s))
    {
        reallocate_m(s);
    }
    s->array[++s->top] = data;
}

int pop(struct DynamicArray *s)
{
    if (isEmpty(s))
    {
        printf("Stack Underflow\n");
        return;
    }
    return s->array[s->top--];
}

void print_stack(struct DynamicArray *s)
{
    for (int i = s->top; i >= 0; --i)
    {
        printf("%d ->", s->array[i]);
    }
    printf("\n");
}

int main()
{
    struct DynamicArray *s = createStack();
    int arr[10] = {1, 3, 4, 5, 6, 7, 7, 7, 5, 10};
    for (int i = 0; i < 10; i++)
    {
        push(s, arr[i]);
        print_stack(s);
    }
    pop(s);
    pop(s);
    print_stack(s);
    return 0;
}