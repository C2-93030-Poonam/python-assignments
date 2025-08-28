// Create a structure called Employee that includes three fields - a first 
//name (type String), a last name (type String) and a monthly salary (double). 
//Write functions to initialize the fields, print them and modify the values in 
//the given object. Example methods: 
// void emp_init(struct emp* e);  
// void set_salary(struct emp *e, double sal); 
// void emp_display(struct emp *e); 
//Write the test code in the main(). Create two emp objects and display each 
//object’s yearly salary. Then give each Employee a 10% raise and display 
//each Employee’s yearly salary again. '''

#include <stdio.h>
#include <string.h>

struct emp {
    char firstName[50];
    char lastName[50];
    double monthlySalary;
};

void emp_init(struct emp *e, const char *first, const char *last, double salary) {
    strncpy(e->firstName, first, sizeof(e->firstName));
    strncpy(e->lastName, last, sizeof(e->lastName));
    e->monthlySalary = (salary > 0) ? salary : 0.0;
}
void set_salary(struct emp *e, double sal) {
    if (sal > 0)
        e->monthlySalary = sal;
}

void emp_display(struct emp *e) {
    printf("Employee: %s %s\n", e->firstName, e->lastName);
    printf("Monthly Salary: %.2f\n", e->monthlySalary);
    printf("Yearly Salary : %.2f\n\n", e->monthlySalary * 12);
}


void give_raise(struct emp *e) {
    e->monthlySalary *= 1.10;
}

int main() {
    struct emp emp1, emp2;

    
    emp_init(&emp1, "Alice", "Johnson", 50000);
    emp_init(&emp2, "Bob", "Smith", 60000);

    printf("Before Raise:\n");
    emp_display(&emp1);
    emp_display(&emp2);


    give_raise(&emp1);
    give_raise(&emp2);

    printf("After 10%% Raise:\n");
    emp_display(&emp1);
    emp_display(&emp2);

    return 0;
}