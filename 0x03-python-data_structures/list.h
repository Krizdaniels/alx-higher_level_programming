#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct lsitint_s - the singly linked list
 * @i: integer
 * @next: to point to the next node
 *
 * Description: The sungly linked list node structure
 * for ALX SE Project
 */

typedef struct listint_s
{
	int i;
	struct listint_s *next;
} 
listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int i);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

#endif /* LISTS_H */
