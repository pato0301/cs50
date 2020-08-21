#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>

int main(void)
{
    //get input
    string text = get_string("Text: ");
    int num_letras = 0;
    int num_palabras = 1;
    int num_sent = 0;
    //loop to get letters
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (isalpha(text[i]))
        {
            //printf("%c",text[i]);
            num_letras ++;
        }
        if (text[i] == ' ' || text[i] == '\n' || text[i] == '\t')
        {
            num_palabras++;
    	}
    	if (text[i] == '!' || text[i] == '.' || text[i] == '?')
    	{
    	    num_sent ++;
    	}
    }
    //get average letter and sentences
    float avg_let = ((float)(num_letras) / (float)num_palabras) * 100;
    float avg_sent = ((float)(num_sent) / (float)num_palabras) * 100;

    //calculate
    int index = (int)round((0.0588 * avg_let) - (0.296 * avg_sent) - 15.8);
    //print
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}