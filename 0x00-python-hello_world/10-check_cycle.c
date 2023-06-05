#include "lists.h"

/**
*check_cycle - checks if a singly linked list has a cycle in it
*
*@list: pointer to the singly list head
*
*Return: 1 if cycle present or 0 if no cycle found
*
*/

int check_cycle(listint_t *list)
{

	listint_t *top = list->next;
	listint_t *normal = list;


	while (top != NULL && top->next != NULL && normal != NULL)
	{
		if (!list)
		{
			return (0);
		}

		if (top == normal)
		{

			return (1);
		}

		top = top->next->next;
		normal = normal->next;
	}

	return (0);
}
