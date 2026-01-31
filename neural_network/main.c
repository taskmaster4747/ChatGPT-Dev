#include <stdio.h>
#include "pico/stdlib.h"
#include <math.h>

// Network structure
#define INPUT_NODES 2
#define HIDDEN_NODES 3
#define OUTPUT_NODES 1

// Sigmoid
float sigmoid(float x) {
    return 1.0f / (1.0f + expf(-x));
}

// Pre-trained weights (example values)
float weights_input_hidden[INPUT_NODES][HIDDEN_NODES] = {
    {0.5f, -0.3f, 0.8f},
    {-0.2f, 0.7f, 0.1f}
};

float weights_hidden_output[HIDDEN_NODES][OUTPUT_NODES] = {
    {0.6f},
    {-0.4f},
    {0.9f}
};

float bias_hidden[HIDDEN_NODES] = {0.1f, 0.2f, -0.1f};
float bias_output[OUTPUT_NODES] = {0.05f};

void forward_propagation(float input[], float output[]) {
    float hidden[HIDDEN_NODES];

    // Hidden layer
    for (int i = 0; i < HIDDEN_NODES; i++) {
        hidden[i] = bias_hidden[i];
        for (int j = 0; j < INPUT_NODES; j++) {
            hidden[i] += input[j] * weights_input_hidden[j][i];
        }
        hidden[i] = sigmoid(hidden[i]);
    }

    // Output layer
    for (int i = 0; i < OUTPUT_NODES; i++) {
        output[i] = bias_output[i];
        for (int j = 0; j < HIDDEN_NODES; j++) {
            output[i] += hidden[j] * weights_hidden_output[j][i];
        }
        output[i] = sigmoid(output[i]);
    }
}

int main() {
    stdio_init_all();
    sleep_ms(2000); // wait for USB serial

    float input[2] = {0, 1};
    float output[1];

    while (true) {
        forward_propagation(input, output);
        printf("NN Output: %f\n", output[0]);
        sleep_ms(1000);
    }
}
