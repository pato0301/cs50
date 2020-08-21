// Implements a dictionary's functionality

#include <stdbool.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>
#include "dictionary.h"


// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
// Const unsigned int N = 1;
const unsigned int N = 26;

unsigned long q_words = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // Get index word
    int index = hash(word);
    node *cursor = NULL;

    // Get tables's index
    cursor = table[index];

    // Check hash table until end
    while (cursor != NULL)
    {
        int value = strcasecmp(cursor -> word, word);
        if (value == 0)
        {
            return true;
        }
        else
        {
            // Point to next
            cursor = cursor -> next;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // Assign the last position to the apostrophe
    if (word[0] == '\'')
    {
        return N;
    }
    return tolower(word[0]) - 'a';
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Open file and Set Pointer to file
    FILE *file = fopen(dictionary, "r");
    if (!file)
    {
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];
    int index;

    // Load until end of text
    while (fscanf(file, "%s", word) != EOF)
    {
        // Alloc new memory
        node *new_word = malloc(sizeof(node));

        // If pointer NuLL return false
        if (new_word == NULL)
        {
            return false;
        }

        // Copy string to new pointer
        strcpy(new_word -> word, word);
        new_word -> next = NULL;

        // Get index word
        index = hash(word);

        // Check if exist in hash table
        if (table[index] == NULL)
        {
            table[index] = new_word;
        }
        else
        {
            // Keep track of the previous value
            node *predptr = table[index];

            // Loop until we find the end
            while (true)
            {
                // Check if end of list
                if (predptr -> next == NULL)
                {
                    // Add new node to end of list
                    predptr -> next = new_word;

                    // Break out while loop
                    break;
                }

                // Update pointer
                predptr = predptr -> next;
            }
        }
        // Add word counter
        q_words ++;
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary
unsigned int size(void)
{
    // Return number of words in Dic
    return q_words;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // If it truly load
    if (&load)
    {
        // Set pointers cursor and tmp
        node *cursor = NULL;
        node *tmp = NULL;
        int index;

        // Go through each value and set to NULL
        for (int i = 0; i < N; i++)
        {
            index = i;
            cursor = table[index];
            tmp = table[index];

            // Set cursor to next, free tmp and set tmp
            // To point to same value as cursor
            while (cursor != NULL)
            {
                cursor = cursor -> next;
                free(tmp);
                tmp = cursor;
            }
        }
        // If success return True
        return true;
    }
    // If success return False
    return false;
}
