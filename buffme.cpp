#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
//so this is definitely a buffer overflow vulnerability im so happy!!! THANK YOU POOKIE. I always wondered, how do you exploit this? (well, my first thought is file upload vulnerability, you look for exec. or compile as a "png!" or "exe" and upload it to the server)
int main(vuln) {
    char buffer[128];
    read(STDIN_FILENO, buffer, 512);
    printf("Buffer content: %s\n", buffer);
    if (strstr(buffer, "password")) { // Check if the buffer contains "password"
        printf("Access granted!\n");
        system("/bin/sh");
        exit(0);
    } else {
        printf("Access denied.\n");
    }
}
