#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - check if a singly list is a palindrome
 * @head: pointer to singly list head node pointer
 * Return: 1 (is a palindrome), 0 (not a palindrome)
*/

int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);
	listint_t *s = *head, *f = *head, *nxtNode;
	listint_t *prevNode, *curNode, *firstP, *lastP;

	while (f && f->next)
	{
		s = s->next;
		f = f->next->next;
	}

	prevnode = NULL;
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
