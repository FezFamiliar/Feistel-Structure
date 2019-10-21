# Feistel-Structure
A basic Feistel Structure with a very insecure f-function.
Feistel structure is a basic way of designing block ciphers, common ciphers like DES, AES all use the feistel scheme. The feistel scheme works for any function f but is secure for only a set of specific f functions. It consists of 16 rounds where the halves are swapped after putting it through the f function and XOR-ing it with the other half.
