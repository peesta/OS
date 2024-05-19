#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

int main() {
    __pid_t pid = fork();

    if (pid == 0) {
        printf("Child process\n");
    }
    else {
        printf("Parrent process\n");
    }

    printf("Current PID: %d\n", getpid());
    printf("Parrent PID: %d\n", getppid());

    return 0;
}