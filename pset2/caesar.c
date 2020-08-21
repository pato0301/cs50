#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    //checking user pass only one argument
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    // checking only pass numbers
    string clave = argv[1];
    for (int i = 0; i < strlen(clave); i++)
    {
        if (isdigit(clave[i]) == 0)
        {
            return 1;
        }
    }
    //convert string to int
    int key = atoi(clave);

    string text = get_string("plaintext:  ");

    printf("ciphertext: ");

    //cipher the text
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]))
        {
            //checking uppercase
            if (isupper(text[i]))
            {
                int letter = text[i];
                int result = ((((letter - 65) + key) % 26) + 65);
                printf("%c", result);
            }
            //checking lowercase
            else if (islower(text[i]))
            {
                int letter = text[i];
                int result = ((((letter - 97) + key) % 26) + 97);
                printf("%c", result);
            }
        }
        //else print that character
        else
        {
            printf("%c", text[i]);
        }
    }
    //return 0 if successful
    printf("\n");
    return 0;
}

