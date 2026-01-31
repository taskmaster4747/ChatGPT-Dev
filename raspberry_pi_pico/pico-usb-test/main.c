#include <stdio.h>
#include "pico/stdlib.h"

int main() {
    stdio_init_all();
    sleep_ms(2000);

    while (!stdio_usb_connected()) {
        sleep_ms(100);
    }

    printf("Hello from Raspberry Pi Pico (WSL)!\n");

    while (true) {
        sleep_ms(1000);
        printf("Tick\n");
    }
}
