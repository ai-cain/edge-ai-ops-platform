cmake_minimum_required(VERSION 3.20)

project(external_runtime_c LANGUAGES C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

add_executable(external_runtime_c main.c)
