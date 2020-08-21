// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include<ctype.h>
#include<string.h>

#include "dictionary.h"

// Represents number of children for each node in a trie
#define N 27

// Represents a node in a trie
typedef struct node
{
    bool is_word;
    struct node *children[N];
}
node;

// Represents a trie
node *root;

int wordCount = 0;

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize trie
    root = malloc(sizeof(node));
    if (root == NULL)
    {
        return false;
    }
    root->is_word = false;
    for (int i = 0; i < N; i++)
    {
        root->children[i] = NULL;
    }

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    node* currentnode = NULL;
    currentnode = root;

    // Insert words into trie
    while (fscanf(file, "%s", word) != EOF)
    {
        // TODO
        /*int largo = strlen(word);
        for (int i = 0; i < largo; i++)
        {
            int index;

            if (isalpha(word[i]))
            {
                index = tolower(word[i]) - 'a';
            }
            else if (word[i] == '\'')
            {
                index = 26;
            }
            else
            {
                index = 27
            }
            if (index <= 27 && index >= 0)
            {
                if(currentnode->children[index] == NULL)
                {
                   node *newnode = (node*)malloc(sizeof(node));
                   if (newnode == NULL)
                    {
                        printf("Could not load dictionary");
                        unload();
                        return false;
                    }
                    currentnode->children[index]=newnode;
                }
                else
   			    {
   				    currentnode = currentnode -> children[index];
   			    }
            }
        }
        currentnode->is_word = true;
        wordCount ++;*/

        // setting current node to first node
   		currentnode = root;

   		// iterating through character and adding each
   		// letter to children until "\n"
   		//int largo = strlen(word);
   		int aAsInt = (int)'a';
        int zAsInt = (int)'z';
   		int character = 0;
   		character = fgetc(file);
   		for(; character != '\n'; character = fgetc(file))
   		{
   			// if apostrophe then store in
   			if (character == '\'')
   			{
   				character = zAsInt + 1;
   			}

   			// if the character is not in trie...create one
   			if (currentnode -> children[character - aAsInt] == NULL)
   			{
   				// malloc a new node
   				currentnode -> children[character - aAsInt] = malloc(sizeof(node));
   				currentnode = currentnode -> children[character - aAsInt];
   			}
   			// got to address in children
   			else
   			{
   				currentnode = currentnode -> children[character - aAsInt];
   			}

   		}
   		currentnode -> is_word = true;
   		wordCount++;
    }

    // Close dictionary
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    //return 0;
    return wordCount;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // TODO
    /*int length = strlen(word);
    node* currentnode = NULL;
    currentnode = root;
    for(int i = 0; i < length; i++)
    {
        if(word[i]=='\'')
        {
            if (currentnode -> is_word == true)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        int index = tolower(word[i]) - 'a';
        if(currentnode ->children[index]==NULL)
        {
            return false;
        }
        currentnode = currentnode ->children[index];
    }
    return false;*/

    //return false;
    // TODO
    // letter as int

    int aAsInt = (int)'a';
    int zAsInt = (int)'z';

    // set current node to first node
    node* currentnode = root;

    // looping through each letter in word
    int length = strlen(word);
    int i = 0;
    while(word[i] != '\0')  //for (int i = 0; i < length; i++)//while(word[i] != '\0')
    {
        char ch = word[i];


        // find is ch is apostrophe
        if (word[i] == '\'')
        {
            ch = zAsInt + 1;
        }
        // converting letter between 0 and 25
        int index = tolower(ch) - aAsInt;

        if (currentnode -> children[index] != NULL)
        {
            currentnode = currentnode -> children[index];
            i++;
        }
        else
        {
            return false;
        }

    }

        if (currentnode -> is_word == true)
        {

            return true;
        }
        else
        {
            return false;
        }
        /*
        int length = strlen(word);
        node* trav = root;
        int index;

        //for each letter in input word
        for (int i = 0; i < length; i++)
        {
            if(isalpha(word[i]) == true)
                index = tolower(word[i]) - 'a';
            else
                index = 26;

            //go to corresponding element in children
            node *next = trav->children[index];

            //check if the pointer is null or not
            if (next == NULL)
                return false;
            else
                trav = next;
        }
        if (trav->is_word == true)
            return true;
        else
            return false;*/

}

void freenode(node* rootnode)
{
    for(int i = 0; i < 27; i++)
    {
        if (rootnode -> children[i] != NULL)
        {
            freenode(rootnode -> children[i]);
        }
    }
    free(rootnode);
    return;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // TODO
    node* rootnode = root;
    freenode(rootnode);
    return true;
    //return false;
}
