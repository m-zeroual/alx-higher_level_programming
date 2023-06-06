#include "lists.h"

/**
 * check_cycle - checks list has cycle
 * @list: pointer to list
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *lst, *check;

	if (list == NULL || list->next == NULL)
		return (0);
	lst = list;
	check = lst->next;
	while (lst != NULL && check->next != NULL
		&& check->next->next != NULL)
	{
		if (lst == check)
			return (1);
		lst = lst->next;
		check = check->next->next;
	}
	return (0);
}
