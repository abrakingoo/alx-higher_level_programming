#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast->next != NULL && fast->next->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	listint_t *prev = NULL;
	listint_t *next = NULL;
	listint_t *current = slow->next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	listint_t *firstHalf = *head;
	listint_t *secondHalf = prev;

	while (secondHalf != NULL)
	{
		if (firstHalf->n != secondHalf->n)
			return (0);

		firstHalf = firstHalf->next;
		secondHalf = secondHalf->next;
	}
	return (1);
}
