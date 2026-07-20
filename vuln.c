#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void) {
    char buffer[128];
    if (fgets(buffer, sizeof(buffer), stdin) != NULL) {
        // Remove newline if present
        buffer[strcspn(buffer, "\n")] = '\0';
        printf("Buffer content: %s\n", buffer);
        if (strstr(buffer, "password")) {
            printf("Access granted!\n");
            system("/bin/sh");
            exit(0);
        } else {
            printf("Access denied.\n");
        }
    }
    return 0;
}