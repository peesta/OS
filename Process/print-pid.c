#include <stdio.h>
#include <unistd.h>

int main() {
    __pid_t current_pid = getpid();
    __pid_t parrent_pid = getppid();

    printf("Current PID: %d\n", current_pid);
    printf("Parrent PID: %d\n", parrent_pid);

    return 0;
}