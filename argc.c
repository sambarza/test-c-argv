#include <stdio.h>

int main(int argc, char *argv[]) {
    printf("Size of int: %zu bytes\n", sizeof(int));
    for (int i = 0; i < argc; i++) {
        printf("Argoument %d is %s\n", i, argv[i]);
    }

    return 0;
}