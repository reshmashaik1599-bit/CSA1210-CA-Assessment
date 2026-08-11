#include <stdio.h>
#include <stdint.h>
#include <string.h>

void printFloatBits(float value) {
    uint32_t bits;

    memcpy(&bits, &value, sizeof(bits));

    printf("IEEE 754 bits: ");

    for (int i = 31; i >= 0; i--) {
        printf("%d", (bits >> i) & 1);

        if (i == 31 || i == 23) {
            printf(" ");
        }
    }

    printf("\n");
}

int main() {
    float largeFloat = 100000000.0f;
    float smallFloat = 1.0f;

    double largeDouble = 100000000.0;
    double smallDouble = 1.0;

    float floatResult = largeFloat + smallFloat;
    double doubleResult = largeDouble + smallDouble;

    printf("===== IEEE 754 FLOATING-POINT DEBUGGING =====\n\n");

    printf("FLOAT:\n");
    printf("Large number = %.1f\n", largeFloat);
    printf("Small number = %.1f\n", smallFloat);
    printf("Result = %.1f\n", floatResult);
    printFloatBits(floatResult);

    printf("\nDOUBLE:\n");
    printf("Large number = %.1f\n", largeDouble);
    printf("Small number = %.1f\n", smallDouble);
    printf("Result = %.1f\n", doubleResult);

    printf("\nExpected mathematical result = 100000001.0\n");

    if (floatResult != 100000001.0f) {
        printf("Float precision loss detected.\n");
    }

    if (doubleResult == 100000001.0) {
        printf("Double precision preserves the small value.\n");
    }

    printf("\nOptimization: Use double precision for calculations requiring higher accuracy.\n");

    return 0;
}