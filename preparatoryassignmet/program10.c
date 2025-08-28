// Read at most 10 names of students and store them into an array of 
//char nameOfStudents[10][50]. Sort the array and display them back. Hint: 
//Use qsort() method.


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STUDENTS 10
#define MAX_NAME_LEN 50


int compareNames(const void *a, const void *b) {
    return strcmp((char *)a, (char *)b);
}

int main() {
    char nameOfStudents[MAX_STUDENTS][MAX_NAME_LEN];
    int n;

    
    printf("Enter number of students (max 10): ");
    scanf("%d", &n);
    getchar(); 

    if (n > MAX_STUDENTS || n <= 0) {
        printf("Invalid number of students.\n");
        return 1;
    }

    
    for (int i = 0; i < n; i++) {
        printf("Enter name of student %d: ", i + 1);
        fgets(nameOfStudents[i], MAX_NAME_LEN, stdin);


        size_t len = strlen(nameOfStudents[i]);
        if (len > 0 && nameOfStudents[i][len - 1] == '\n') {
            nameOfStudents[i][len - 1] = '\0';
        }
    }

    
    qsort(nameOfStudents, n, MAX_NAME_LEN, compareNames);

    
    printf("\nSorted list of student names:\n");
    for (int i = 0; i < n; i++) {
        printf("%s\n", nameOfStudents[i]);
    }

    return 0;
}