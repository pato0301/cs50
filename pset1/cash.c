#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main (void)
{
    int cash;
    //get cash
    do{
        cash = round(get_float("Change owed: ")*100);
    }
    while (cash<0);
    //define coins as variables
    int quarters = 25;
    int dimes = 10;
    int nickels = 5;
    int pennies = 1;
    //initialize varible q of each coin
    int n_qrt = 0;
    int n_dim = 0;
    int n_nik = 0;
    int n_pen = 0;
    int mod_qrt = (int) (cash % quarters);
    n_qrt = cash / quarters;
    n_dim = mod_qrt / dimes;
    int mod_dim = (int) ( (int) (cash % quarters) % dimes);
    n_nik = mod_dim / nickels;
    int mod_nik = (int) round((int) round((int) round(cash % quarters) % dimes) % nickels);
    n_pen = mod_nik / pennies;
    int coins = n_qrt + n_dim + n_nik + n_pen;
    printf("%i\n",coins);
}