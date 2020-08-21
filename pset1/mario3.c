#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int h = h;
    do
    {
        //printf("give me a number\n");
        h = get_int("give me a number\n");
        printf("you picked %d \n", h);
    }
    while (h<0 || h>23);

    do
    {
        printf("##\n");
        h++;
    }
    while (h < 23);
}
