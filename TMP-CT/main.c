// main.c - Pico temperature alert
#include "pico/stdlib.h"
#include "hardware/adc.h"
#include <stdio.h>

int main() {
    // Initialize stdio over USB
    stdio_init_all();

    // Initialize internal temperature sensor (ADC4)
    adc_init();
    adc_set_temp_sensor_enabled(true);
    adc_select_input(4);

    while (true) {
        uint16_t raw = adc_read();
        // Convert ADC reading to voltage
        float voltage = raw * 3.3f / 65535.0f;
        // Convert voltage to temperature in Celsius (datasheet formula)
        float temperature = 27.0f - (voltage - 0.706f) / 0.001721f;

        // Print temperature
        printf("%.2f\n", temperature);
        fflush(stdout);  // make sure data is sent immediately

        // Alert if temp > 30°C
        if (temperature > 30.0f) {
            printf("ALERT\n");
            fflush(stdout);
        }

        sleep_ms(1000);  // wait 1 second
    }

    return 0;
}
