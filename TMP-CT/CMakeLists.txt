cmake_minimum_required(VERSION 3.13)
include(pico_sdk_import.cmake)

project(temp_alert C CXX ASM)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

pico_sdk_init()

add_executable(temp_alert
    main.c
)

target_link_libraries(temp_alert pico_stdlib hardware_adc)

pico_add_extra_outputs(temp_alert)
