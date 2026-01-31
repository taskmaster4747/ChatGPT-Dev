cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(pico_nn C CXX ASM)
set(CMAKE_C_STANDARD 11)

pico_sdk_init()

add_executable(pico_nn
    main.c
)

target_link_libraries(pico_nn
    pico_stdlib
    m
)

pico_enable_stdio_usb(pico_nn 1)
pico_enable_stdio_uart(pico_nn 0)

pico_add_extra_outputs(pico_nn)

