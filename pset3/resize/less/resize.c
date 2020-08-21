#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>

#include "bmp.h"

int main(int argc, string argv[])
{

    // ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: copy integer infile outfile\n");
        return 1;
    }
    else if (atoi(argv[1]) < 0 || atoi(argv[1]) > 100)
    {
        printf("integer must be greater than 0 and lower than 100\n");
        return 1;
    }

    //resize integer
    //int * resizer= malloc(sizeof(int));
    //int resizer;
    int resizer = atoi(argv[1]);
    // remember filenames
    char *infile = argv[2];
    char *outfile = argv[3];

    // open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);
    BITMAPFILEHEADER bf_new;
    bf_new = bf;
    //bf_new.bfSize = bi_new.biSizeImage + sizeof(bf_new) + sizeof(bi_new);


    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);
    // resize info
    BITMAPINFOHEADER bi_new;
    bi_new = bi;
    bi_new.biWidth = bi.biWidth * resizer;
    bi_new.biHeight = bi.biHeight * resizer;
    //bi_new.biSizeImage = ((sizeof(RGBTRIPLE) * bi_new.biWidth) + padding) * abs(bi_new.biHeight);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }

    // write outfile's BITMAPFILEHEADER
    //fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    //fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // determine padding for scanlines
    int padding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    int padding_new = (4 - (bi_new.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    //new biSizeImage
    bi_new.biSizeImage = ((sizeof(RGBTRIPLE) * bi_new.biWidth) + padding_new) * abs(bi_new.biHeight);
    // new bfSize
    bf_new.bfSize = bi_new.biSizeImage + sizeof(bf_new) + sizeof(bi_new);

    // write outfile's BITMAPFILEHEADER
    fwrite(&bf_new, sizeof(BITMAPFILEHEADER), 1, outptr);
    // write outfile's BITMAPINFOHEADER
    fwrite(&bi_new, sizeof(BITMAPINFOHEADER), 1, outptr);

    // iterate over infile's scanlines
    for (int i = 0, biHeight = abs(bi.biHeight); i < biHeight; i++)
    {
        for (int m = 0; m < resizer; m++)
        {
            // iterate over pixels in scanline
            for (int j = 0; j < bi.biWidth; j++)
            {
                // temporary storage
                RGBTRIPLE triple;

                // read RGB triple from infile
                fread(&triple, sizeof(RGBTRIPLE), 1, inptr);


                // write RGB triple to outfile
                for (int k = 0; k < resizer; k++)
                {

                   fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
                }
                //fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
            }
            // skip over padding, if any
            fseek(inptr, padding, SEEK_CUR);

            // then add it back (to demonstrate how)
            for (int f = 0; f < padding_new; f++)
            {
                fputc(0x00, outptr);
            }
            fseek(inptr, -((bi.biWidth * sizeof(RGBTRIPLE)) + padding), SEEK_CUR);
        }
        fseek(inptr, (bi.biWidth * sizeof(RGBTRIPLE)) + padding, SEEK_CUR);

    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}