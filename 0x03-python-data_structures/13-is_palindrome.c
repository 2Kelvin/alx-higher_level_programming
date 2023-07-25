#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - check if a singly list is a palindrome
 * @head: pointer to singly list head node pointer
 * Return: 1 (is a palindrome), 0 (not a palindrome)
*/

int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	listint_t *s = *head;
	listint_t *f = *head;
	listint_t *nxtNode;
	listint_t *prevNode;
	listint_t *curNode;
	listint_t *firstP;
	listint_t *lastP;

	while (f && f->next)
	{
		s = s->next;
		f = f->next->next;
	}

	prevNode = NULL;
	curNode = s;

	while (curNode != NULL)
	{
		nxtNode = curNode->next;
		curNode->next = prevNode;
		prevNode = curNode;
		curNode = nxtNode;
	}

	firstP = *head;
	lastP = prevNode;

	while (firstP && lastP)
	{
		if (firstP->n != lastP->n)
			return (0);
		firstP = firstP->next;
		lastP = lastP->next;
	}

	return (1);
}
