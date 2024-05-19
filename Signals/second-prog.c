#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>

int main(int argc, char *argv[]) {
    __pid_t pid = atoi(argv[1]);
    int signal_number = atoi(argv[2]);
    int signal;

    if (signal_number == 1) {
        signal = SIGUSR1;
    } else if (signal_number == 2){
        signal = SIGUSR2;
    } else {
        exit(1);
    }

    if (kill(pid, signal) == -1) {
        exit(1);
    }

    return 0;
}