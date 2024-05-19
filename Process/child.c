#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

int main() {

    printf("Child process\n");
    printf("Current PID: %d\n", getpid());
    printf("Parrent PID: %d\n", getppid());

    return 0;
    
}