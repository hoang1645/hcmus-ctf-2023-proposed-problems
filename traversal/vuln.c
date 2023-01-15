#include <stdio.h>
#include <string.h>
#include <unistd.h>

char FLAG[40];

void read_flag()
{
    FILE* f = fopen("flag.txt", "r");
    fread(FLAG, 1, 40, f);
    fclose(f);
}

int main()
{
    read_flag();
    printf("Here is your gift: %x\n", FLAG);
    printf("Do you want to say anything else?\n");
    char buf[550];
    fgets(buf, 550, stdin);
    printf(buf);
    printf("Goodbye!");
    return 0;
}
