#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>

volatile int current_string_index = 0;
const char *strings[] = {
    "Hello world!\n",
    "Goodbye world...\n"
};

void handler_signal(int signal) {
    if (signal == SIGUSR1 || signal == SIGUSR2) {
        current_string_index = 1 -current_string_index;
    }
}

int main() {
    
    if (signal(SIGUSR1, handler_signal) == SIG_ERR) {
        exit(1);
    }
    if (signal(SIGUSR2, handler_signal) == SIG_ERR) {
        exit(1);
    }

    while (1) {
        printf("%s", strings[current_string_index]);
        fflush(stdout);
        sleep(1);
    }
    
    return 0;

}