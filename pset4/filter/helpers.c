#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    //loop through height and width and gray the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int avg = (int)round((float)(image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            //average in each pixel
            image[i][j].rgbtBlue  = avg;
            image[i][j].rgbtGreen  = avg;
            image[i][j].rgbtRed  = avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    //loop through height and width and gray the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int originalRed = image[i][j].rgbtRed;
            int originalGreen = image[i][j].rgbtGreen;
            int originalBlue = image[i][j].rgbtBlue;
            //calculando sepia
            int sepiaRed = (int)round(0.393 * originalRed + 0.769 * originalGreen + 0.189 * originalBlue);
            int sepiaGreen = (int)round(0.349 * originalRed + 0.686 * originalGreen + 0.168 * originalBlue);
            int sepiaBlue = (int)round(0.272 * originalRed + 0.534 * originalGreen + 0.131 * originalBlue);
            //seting max valueof sepia
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            //replacing values
            image[i][j].rgbtBlue  = sepiaBlue;
            image[i][j].rgbtGreen  = sepiaGreen;
            image[i][j].rgbtRed  = sepiaRed;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    //is width divisible by 2
    int half_width;
    if (((width) / 2) % 2 == 0)
    {
        half_width = (width) / 2;
    }
    else
    {
        half_width = ((int)round(((float)(width)) / 2));
    }
    //loop through height and width and gray the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < half_width; j++)
        {
            //swapping values
            RGBTRIPLE temp = image[i][j];
            int reverse = j + 1;
            image[i][j] = image[i][width - reverse];
            image[i][width - reverse] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //declaring array to store average
    RGBTRIPLE temp[height][width];

    //loop through height and width and gray the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int n = 0, p = 0, q = 0; //declaring three variables for storing sum
            float count = 0.0; //variable to count how many times sum has been done
            for (int k = i - 1; k < i + 2 ; k++)
            {
                for (int l = j - 1; l < j + 2; l++)
                {
                    if ((l >= 0 && k >= 0) && (l < width && k < height))
                    {
                        //summing color from around
                        n += image[k][l].rgbtRed;
                        p += image[k][l].rgbtGreen;
                        q += image[k][l].rgbtBlue;
                        count++;
                    }

                }
            }
            //assigning value to copy
            temp[i][j].rgbtRed = (int)(round((float)n / count));
            temp[i][j].rgbtBlue = (int)(round((float)q / count));
            temp[i][j].rgbtGreen = (int)(round((float)p / count));
        }
    }
    //loop through height and width and gray the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //assigning values from temp to image
            image[i][j].rgbtRed = temp[i][j].rgbtRed;
            image[i][j].rgbtGreen = temp[i][j].rgbtGreen;
            image[i][j].rgbtBlue = temp[i][j].rgbtBlue;
        }
    }
    return;
}
