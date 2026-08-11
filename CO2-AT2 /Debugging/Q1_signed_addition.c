#include <stdio.h>
#include <stdint.h>

int main() {
    int8_t a = 120;
    int8_t b = 50;

    int16_t result = (int16_t)a + (int16_t)b;

    printf("Signed Integer Addition\n");
    printf("-----------------------\n");

    printf("A = %d\n", a);
    printf("B = %d\n", b);
    printf("A + B = %d\n", result);

    if (result > 127 || result < -128) {
        printf("Overflow detected!\n");
        printf("Result cannot be stored in 8-bit signed integer.\n");
    } else {
        printf("No overflow.\n");
        printf("Result can be stored in 8-bit signed integer.\n");
    }

    return 0;
}