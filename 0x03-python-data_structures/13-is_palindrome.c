#include "lists.h"

int is_palindrome(listint_t **head)
{
    if (*head == NULL)
        return (1);

    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *next = NULL;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        next = slow->next;
        slow->next = prev;
        prev = slow;
        slow = next;
    }

    if (fast != NULL)
        slow = slow->next;

    while (prev != NULL && slow != NULL)
    {
        if (prev->n != slow->n)
            return (0);

        prev = prev->next;
        slow = slow->next;
    }

    return (1);
}

