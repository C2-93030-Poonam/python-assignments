//Declare an Array of type char* and initialize it with a few strings (hard
//coded). Display the strings which are duplicated in that array. (Hint: use 
//strcmp())

#include <stdio.h>
#include <string.h>

int main() {
    char *nameOfStudents[] = {
        "Alice", "Bob", "Charlie", "Alice", "David", "Bob", "Eve"
    };
    int n = sizeof(nameOfStudents) / sizeof(nameOfStudents[0]);

    printf("Duplicate names in the array:\n");


    for (int i = 0; i < n; i++) {
        int isDuplicate = 0;


        for (int k = 0; k < i; k++) {
            if (strcmp(nameOfStudents[i], nameOfStudents[k]) == 0) {
                isDuplicate = 1;
                break;
            }
        }

       
        if (!isDuplicate) {
            for (int j = i + 1; j < n; j++) {
                if (strcmp(nameOfStudents[i], nameOfStudents[j]) == 0) {
                    printf("%s\n", nameOfStudents[i]);
                    break;
                }
            }
        }
    }

    return 0;
}