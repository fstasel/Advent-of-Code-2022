#include <stdio.h>
#include <string.h>

int check(char *data, int n)
{
    int box[26];
    for (int i = 0; i < strlen(data) - n; i++)
    {
        for (int q = 0; q < 26; q++)
            box[q] = 0;
        int flag = 0;
        for (int j = 0; j < n; j++)
        {
            int z = data[i + j] - 'a';
            if (box[z])
            {
                flag = 1;
                break;
            }
            box[z] = 1;
        }
        if (!flag)
        {
            return i + n;
        }
    }
}

int main()
{
    FILE *f = fopen("input.txt", "r");
    char data[10000];
    fscanf(f, "%s", data);
    fclose(f);

    printf("%d\n%d\n", check(data, 4), check(data, 14));
    return 0;
}