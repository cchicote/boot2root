#include <stdio.h>
#include <unistd.h>

int main()
{
    printf("%s\n", crypt("toto", "firefart"));
}
