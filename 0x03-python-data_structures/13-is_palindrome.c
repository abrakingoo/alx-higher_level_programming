#include "lists.h"

/**
*is_palindrome - checks if a singly linked list is a palindrome.
*
*@head: pointer to pointer of first node of listint_t list
*
*Return: 0 if it is not a palindrome, 1 if it is a palindrome
*
*/

int is_palindrome(listint_t **head)
{
	size_t i, length = 0;

	if (*head == NULL)
	{
		return (1);
	}
	else
	{
		listint_t *temp = *head;

		while (temp != NULL)
		{
			length++;
			temp = temp->next;
		}
		temp = *head;

		listint_t *list1 = *head;
		listint_t *list2 = NULL;

		for (i = 0; i < (length - 1) / 2; i++)
		{
			temp = temp->next;
		}

		list2 = temp->next;
		temp->next = NULL;

		listint_t *prev = NULL;
		listint_t *current = list2;
		listint_t *next = NULL;

		while (current != NULL)
		{
			next = current->next;
			current->next = prev;
			prev = current;
			current = next;
		}
		list2 = prev;

		while (list1 != NULL && list2 != NULL)
		{
			if (list1->n != list2->n)
			{
				return (0);
			}

			list1 = list1->next;
			list2 = list2->next;
		}
		return (1);
	}
}
