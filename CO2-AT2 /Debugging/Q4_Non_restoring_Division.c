#include <stdio.h>

void restoringDivision(int dividend, int divisor) {
    int A = 0;
    int Q = dividend;
    int M = divisor;
    int n = 4;

    printf("\n===== RESTORING DIVISION =====\n");

    for (int i = 0; i < n; i++) {

        A = (A << 1) | ((Q >> (n - 1)) & 1);
        Q = (Q << 1) & 0x0F;

        A = A - M;

        printf("Step %d: A after subtraction = %d\n", i + 1, A);

        if (A < 0) {
            A = A + M;
            printf("Restoration performed\n");
        } else {
            Q = Q | 1;
            printf("No restoration required\n");
        }
    }

    printf("Quotient = %d\n", Q);
    printf("Remainder = %d\n", A);
}

void nonRestoringDivision(int dividend, int divisor) {
    int A = 0;
    int Q = dividend;
    int M = divisor;
    int n = 4;

    printf("\n===== NON-RESTORING DIVISION =====\n");

    for (int i = 0; i < n; i++) {

        A = (A << 1) | ((Q >> (n - 1)) & 1);
        Q = (Q << 1) & 0x0F;

        if (A >= 0) {
            A = A - M;
            printf("Step %d: A = A - M -> %d\n", i + 1, A);
        } else {
            A = A + M;
            printf("Step %d: A = A + M -> %d\n", i + 1, A);
        }

        if (A >= 0) {
            Q = Q | 1;
        }
    }

    if (A < 0) {
        A = A + M;
    }

    printf("Quotient = %d\n", Q);
    printf("Remainder = %d\n", A);
}

int main() {
    int dividend = 13;
    int divisor = 3;

    printf("===== DIVISION ALGORITHM DEBUGGING =====\n");
    printf("Dividend = %d\n", dividend);
    printf("Divisor = %d\n", divisor);

    restoringDivision(dividend, divisor);
    nonRestoringDivision(dividend, divisor);

    printf("\nOptimization: Non-Restoring Division avoids repeated restoration steps.\n");

    return 0;
}