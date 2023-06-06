/**
  * check_cycle - check linked list cycle
  * @list: linked list
  * Return: 0 or 1
  */
int check_cycle(listint_t *list)
{
	if (list == NULL)
		return (0);
	else if (list->next == NULL)
		return (0);
	else
		return (1);
}
