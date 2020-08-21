#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int h = h;

    // ask for the height of the half-pyramid until the user gives you a positive no greater than 23 number
    do
    {
        //get hegh
        h = get_int("Height: ");

    }
    while (h <= 0 || h > 8);

    //print the pyramid according to the height
    int i = 0;
    int j = h - 1;
    while (i < h)
    {
        for (int row = i + 1; row < h; row++)
        {
            printf(" ");
        }
        for (int colum = j; colum < h; colum ++)
        {
            printf("#");
        }
        printf("  ");
        for (int colum = j; colum < h; colum ++)
        {
            printf("#");
        }
        printf("\n");
        j--;
        i++;
    }
}