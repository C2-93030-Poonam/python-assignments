#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    // Check if at least one number is provided
    if (argc < 2) {
        printf("Please provide numbers as command line arguments.\n");
        return 1;
    }

    // Initialize max with the first number
    int max = atoi(argv[1]);

    // Loop through the remaining arguments
    for (int i = 2; i < argc; i++) {
        int num = atoi(argv[i]);
        if (num > max) {
            max = num;
        }
    }

    // Display the maximum number
    printf("Maximum number is: %d\n", max);

    return 0;
}