#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a new node to a linked list
 * @head - head pointer
 * @number - input value
 * Return: address of the new node and NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node, *temp;
temp = *head;
if (!temp)
{
return (NULL);
}
new_node = malloc(sizeof(listint_t));
if (!new_node)
{
return (NULL);
}
new_node->n = number;
if (!temp || new_node->n >= number)
{
new_node->next = temp;
new_node = *head;
return (new_node);
}
return (new_node);
}
