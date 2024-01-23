#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *reverse_list(listint_t **head);

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return (1);

    listint_t *slow = *head, *fast = *head;
    listint_t *prev_slow = NULL, *second_half = NULL;
    int is_palindrome = 1;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        second_half = slow->next;
        slow->next = NULL;
    }
    else
    {
        second_half = slow;
        slow = NULL;
    }

    prev_slow->next = reverse_list(&second_half);

    listint_t *current1 = *head;
    listint_t *current2 = second_half;

    while (current1 != NULL && current2 != NULL)
    {
        if (current1->n != current2->n)
        {
            is_palindrome = 0;
            break;
        }
        current1 = current1->next;
        current2 = current2->next;
    }

    prev_slow->next = reverse_list(&second_half);

    return is_palindrome;
}

/**
 * reverse_list - reverses a linked list
 * @head: double pointer to the head of the list
 *
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
    listint_t *prev = NULL, *current = *head, *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
    return *head;
}
