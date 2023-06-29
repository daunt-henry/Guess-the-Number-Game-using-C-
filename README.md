## Guess the Number Game

This repository contains a simple "Guess the Number" game implemented in C. The program generates a random number between 1 and 100, and the player needs to guess the correct number. The game provides feedback to the player, indicating whether the guessed number is higher or lower than the target number. Once the player guesses the correct number, the program displays the number of attempts made.

### How to Play

1. Clone the repository or download the source code file.
2. Compile the code using a C compiler.
3. Run the compiled executable.
4. The program will prompt you to enter a number between 1 and 100.
5. Enter your guess and press enter.
6. The program will provide feedback: "Lower number please!" if your guess is too high, "Higher number please!" if your guess is too low, or "You guessed it in X attempts" if you guess the correct number.
7. Continue guessing until you find the correct number.

### Prerequisites

- C compiler (e.g., GCC) installed on your system.

### Instructions

1. Open your terminal or command prompt.
2. Navigate to the directory where you have the source code file.
3. Compile the code using the following command:

   ```bash
   gcc guess_the_number.c -o guess_the_number
   ```

4. Run the compiled executable:

   - On Linux/macOS:

     ```bash
     ./guess_the_number
     ```

   - On Windows:

     ```bash
     guess_the_number.exe
     ```

5. Play the game by following the on-screen instructions.

### Example Output

```
Guess the number between 1 to 100
50
Lower number please!
Guess the number between 1 to 100
25
Lower number please!
Guess the number between 1 to 100
12
Higher number please!
Guess the number between 1 to 100
18
Lower number please!
Guess the number between 1 to 100
15
You guessed it in 5 attempts
```

Enjoy playing the "Guess the Number" game! Feel free to modify and enhance the code as per your requirements.
