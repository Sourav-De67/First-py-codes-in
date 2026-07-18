#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {

    int number, guess, attempts = 0, maxAttempts, difficulty;

    srand(time(0));

    printf("===== Number Guessing Game =====\n");
    printf("Choose Difficulty Level\n");
    printf("1. Easy (10 attempts)\n");
    printf("2. Medium (7 attempts)\n");
    printf("3. Hard (5 attempts)\n");

    printf("Enter choice: ");
    scanf("%d", &difficulty);

    if(difficulty == 1)
        maxAttempts = 10;
    else if(difficulty == 2)
        maxAttempts = 7;
    else
        maxAttempts = 5;

    number = rand() % 100 + 1;

    printf("\nGuess the number between 1 and 100\n");

    while(attempts < maxAttempts) {

        printf("Enter your guess: ");
        scanf("%d", &guess);

        attempts++;

        if(guess > number)
            printf("Too High!\n");
        else if(guess < number)
            printf("Too Low!\n");
        else {
            printf("🎉 Correct! You guessed it in %d attempts\n", attempts);
            return 0;
        }

        printf("Attempts left: %d\n\n", maxAttempts - attempts);
    }

    printf("❌ You lost! The number was %d\n", number);

    return 0;
}