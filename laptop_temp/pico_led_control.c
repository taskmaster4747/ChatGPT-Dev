#include <stdio.h>
#include "pico/stdlib.h"
#include <string.h>

#define LED_PIN 25

int main() {
    stdio_init_all();
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);

    char buffer[32];
    bool hot = false;

    // Wait for USB serial to connect
    sleep_ms(2000);

    while (true) {
        if (fgets(buffer, sizeof(buffer), stdin)) {

            if (strstr(buffer, "HOT")) {
                hot = true;
            }
            else if (strstr(buffer, "OK")) {
                hot = false;
                gpio_put(LED_PIN, 1); // LED ON
            }
        }

        if (hot) {
            gpio_put(LED_PIN, 1);
            sleep_ms(300);
            gpio_put(LED_PIN, 0);
            sleep_ms(300);
        } else {
            gpio_put(LED_PIN, 1);
            sleep_ms(100);
        }
    }
}
