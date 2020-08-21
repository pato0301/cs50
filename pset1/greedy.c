#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main (void)
{
    // ask for change
    float w;
    do
    {
        printf("how much do i owe you?\n");
        w = GetFloat();
    }
    while (w<0.00);
    
    int m;
    m = round( w * 100);
    int c = 0;
    
    while (m >= 25)
    {
        c++;
        m-=25;                     
    }
    while (m >= 10)
    {
        c++;
        m-=10;
    }
    while (m >= 5)
    {
        c++;
        m-=5;
    }
    while (m >= 1)
    {
        c++;
        m-=1;
    }
    
    printf("%d\n", c);
}
