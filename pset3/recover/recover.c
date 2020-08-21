// Include library
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Check for input
    if (argc != 2)
    {
        fprintf(stderr, "Usage: recover infile\n");
        return 1;
    }

    // Pointer to file
    char *infile = argv[1];

    // Open file and set pointer
    FILE *inptr = fopen(infile, "r");
    FILE *img = NULL;

    // If NULL return 2
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // Buffer
    unsigned char buffer[512];
    int jpgtot = 0;
    char jpg_number[8];

    // Loop until end of file
    while (fread(buffer, sizeof(buffer), 1, inptr) == 1)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Find if it is the first jpg
            if (img != NULL)
            {
                fclose(img);
                img = NULL;
            }

            // Create jpeg
            sprintf(jpg_number, "%03i.jpg", jpgtot);

            // Open a new file with named as sprintf
            img = fopen(jpg_number, "w");

            // Write new jpg to img
            fwrite(&buffer, sizeof(buffer), 1, img);

            // Increment jpg number for name
            jpgtot += 1;
        }
        else
        {
            if (NULL != img)
            {
                fwrite(buffer, sizeof(buffer), 1, img);
            }
        }
    }
    // Close files
    fclose(inptr);
    fclose(img);
}
