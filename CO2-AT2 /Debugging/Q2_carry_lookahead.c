#include <stdio.h>

void rippleCarryAdder(int a[], int b[], int sum[], int n) {
    int carry = 0;

    printf("Ripple Carry Adder:\n");

    for (int i = 0; i < n; i++) {
        sum[i] = a[i] ^ b[i] ^ carry;
        carry = (a[i] & b[i]) | (a[i] & carry) | (b[i] & carry);

        printf("Bit %d -> Carry = %d\n", i, carry);
    }
}

void carryLookAheadAdder(int a[], int b[], int sum[], int n) {
    int p[4], g[4], c[5];

    c[0] = 0;

    for (int i = 0; i < n; i++) {
        p[i] = a[i] ^ b[i];
        g[i] = a[i] & b[i];
    }

    c[1] = g[0] | (p[0] & c[0]);
    c[2] = g[1] | (p[1] & g[0]) |
           (p[1] & p[0] & c[0]);

    c[3] = g[2] | (p[2] & g[1]) |
           (p[2] & p[1] & g[0]) |
           (p[2] & p[1] & p[0] & c[0]);

    c[4] = g[3] | (p[3] & g[2]) |
           (p[3] & p[2] & g[1]) |
           (p[3] & p[2] & p[1] & g[0]) |
           (p[3] & p[2] & p[1] & p[0] & c[0]);

    for (int i = 0; i < n; i++) {
        sum[i] = p[i] ^ c[i];
    }

    printf("\nCarry Look-Ahead Adder:\n");

    for (int i = 0; i < n; i++) {
        printf("Bit %d -> Carry = %d\n", i, c[i + 1]);
    }
}

void printResult(int sum[], int n) {
    printf("Result = ");

    for (int i = n - 1; i >= 0; i--) {
        printf("%d", sum[i]);
    }

    printf("\n");
}

int main() {
    int a[4] = {1, 0, 1, 1};
    int b[4] = {0, 1, 1, 0};

    int rippleSum[4];
    int claSum[4];

    printf("===== CARRY ADDER DEBUGGING =====\n\n");

    printf("A = 1101\n");
    printf("B = 0110\n\n");

    rippleCarryAdder(a, b, rippleSum, 4);
    printResult(rippleSum, 4);

    carryLookAheadAdder(a, b, claSum, 4);
    printResult(claSum, 4);

    printf("\nOptimization: Carry Look-Ahead reduces carry propagation delay.\n");

    return 0;
}