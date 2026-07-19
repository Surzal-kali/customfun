#include <iostream>
#include <string>

int main() {
    // 1. Declare the secret passcode and variables to track attempts
    const std::string SECRET_PASSCODE = "supersecret";
    int attempts = 0;
    const int MAX_ATTEMPTS = 3;
    bool accessGranted = false;

    // 2. Start a loop that runs as long as attempts are under MAX_ATTEMPTS and access hasn't been granted
    while (attempts < MAX_ATTEMPTS && !accessGranted) {
        std::string userInput;
        std::cout << "Enter passcode: ";
        
        // C++ Safe Input: reading into std::string is safe from buffer overflows!
        std::cin >> userInput; 
        if (userInput!=SECRET_PASSCODE){
            attempts++;
            std::cout << "Incorrect passcode. Attempts left" << MAX_ATTEMPTS-attempts << "\n";
        }if (userInput==SECRET_PASSCODE) {
            accessGranted = true;
            std::cout << "Correct passcode!\n";
        }

        // TODO: Increment your attempt counter
        
        // TODO: Write an if/else check to see if userInput matches SECRET_PASSCODE
        // Hint: You can compare strings directly using == (e.g., userInput == SECRET_PASSCODE)
        
        // TODO: If correct, set accessGranted to true and print a success message
        // TODO: If incorrect, print a warning with the remaining attempts left
    }

    // 3. Check final state
    if (accessGranted) {
        std::cout << "\n[+] Welcome back, Operator.\n";
    } else {
        std::cout << "\n[!] ACCESS DENIED: Locked out!\n";
    }

    return 0;
}