cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(pico_usb_test C CXX ASM)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

pico_sdk_init()

add_executable(pico_usb_test
    main.c
)

pico_enable_stdio_usb(pico_usb_test 1)
pico_enable_stdio_uart(pico_usb_test 0)

target_link_libraries(pico_usb_test pico_stdlib)

pico_add_extra_outputs(pico_usb_test)
