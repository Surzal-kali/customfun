#include <iostream>
#include <string>
using namespace std;
// Trying to figure out a xor cipher
int main() {
   std::string plaintext;
   std::string ciphertext;
   std::string key;
   std::cout << "Enter the plaintext: ";
   std::getline(std::cin, plaintext);
   std::cout << "Enter the key: ";
   std::getline(std::cin, key);

   // Extend the key to match the length of the plaintext
   while (key.length() < plaintext.length()) {
       key += key;
   }
   key = key.substr(0, plaintext.length());

   for (size_t i = 0; i < plaintext.length(); ++i) {
       ciphertext += plaintext[i] ^ key[i];
   }
   std::cout << "Ciphertext: " << ciphertext << std::endl;
   return 0;
}