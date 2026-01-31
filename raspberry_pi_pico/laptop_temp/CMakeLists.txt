cmake_minimum_required(VERSION 3.13)

include($ENV{PICO_SDK_PATH}/external/pico_sdk_import.cmake)

project(laptop_temp_led C CXX)

pico_sdk_init()

add_executable(laptop_temp_led
    pico_led_control.c
)

target_link_libraries(laptop_temp_led pico_stdlib)

pico_enable_stdio_usb(laptop_temp_led 1)
pico_enable_stdio_uart(laptop_temp_led 0)

pico_add_extra_outputs(laptop_temp_led)

