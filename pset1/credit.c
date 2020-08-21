#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main (void)
{
    long credit;
    do
    {
       credit = get_long("card number: ");
    }
    while(credit <= 0);
    int count = 0;
    long credit_temp = credit;
    while (credit_temp != 0) {
        credit_temp /= 10;     // n = n/10
        ++count;
    }
    printf("Number of digits: %i\n", count);

    long FirstDigit = credit;
    long TwoDigit = credit;

  	while(FirstDigit >= 10)
  	{
  		FirstDigit = FirstDigit / 10;
	}
	while(TwoDigit >= 100)
  	{
  		TwoDigit = TwoDigit / 100;
	}

	printf(" \n The First Digit of a Given Number %ld =  %ld, %ld\n", credit, FirstDigit,TwoDigit);

	if (TwoDigit == 34 || TwoDigit == 37)
	    {
            if (count == 15){
                printf("AMEX\n");}
            else{
                printf("INVALID\n");}
	    }
    else if (TwoDigit == 51 || TwoDigit == 52 || TwoDigit == 53 || TwoDigit == 54 || TwoDigit == 55)
        {
            if (count== 16){
                printf("MASTERCARD\n");}
            else{
                printf("INVALID\n");}
        }
    else if (FirstDigit == 4)
        {
            if ((count == 13) || (count == 16)){
                printf("VISA\n");}
            else{
                printf("INVALID\n");}
        }
    else{
        printf("INVALID\n");}
}