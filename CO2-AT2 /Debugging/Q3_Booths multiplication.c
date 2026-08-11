#include <stdio.h>

int main() {
    int M = -5;
    int Q = 4;

    int A = 0;
    int Qminus1 = 0;

    int n = 4;

    printf("===== BOOTH'S MULTIPLICATION =====\n\n");
    printf("Multiplicand (M) = %d\n", M);
    printf("Multiplier (Q) = %d\n\n", Q);

    for (int i = 0; i < n; i++) {

        int Q0 = Q & 1;

        printf("Step %d: Q0 = %d, Q-1 = %d\n", i + 1, Q0, Qminus1);

        if (Q0 == 1 && Qminus1 == 0) {
            A = A - M;
            printf("Operation: A = A - M\n");
        }
        else if (Q0 == 0 && Qminus1 == 1) {
            A = A + M;
            printf("Operation: A = A + M\n");
        }
        else {
            printf("Operation: No addition/subtraction\n");
        }

        /*
         * Arithmetic right shift of A, Q and Q-1.
         * The sign bit of A is preserved.
         */
        Qminus1 = Q & 1;

        Q = (Q >> 1) | ((A & 1) << (n - 1));

        A = A >> 1;

        printf("After arithmetic shift: A = %d, Q = %d\n\n", A, Q);
    }

    int result = (A << n) | (Q & 0x0F);

    /*
     * Convert the 8-bit two's complement result
     * to a signed value.
     */
    if (result & 0x80) {
        result = result - 256;
    }

    printf("Final Result = %d\n", result);
    printf("Expected Result = %d\n", M * 4);

    if (result == M * 4) {
        printf("Test Passed: Booth multiplication is correct.\n");
    } else {
        printf("Test Failed: Check bit-pair handling or sign extension.\n");
    }

    return 0;
}