execute_process(
  COMMAND ${CMAKE_COMMAND} -P
          "/home/kalind/Documents/GitHub/CS773_Comp_Arch_Perf_Sec/course_content/project/sc2020-main-solvers/cryptominisat-ccnr/cmake-3.12.0/Tests/CMakeTests/MessageTestScript.cmake"
  OUTPUT_VARIABLE out
  ERROR_VARIABLE err
  RESULT_VARIABLE result
  )

message("out=[${out}]")
message("err=[${err}]")

if(NOT "${result}" STREQUAL "0")
  message(FATAL_ERROR "message script failed: [${result}]")
endif()

if(NOT "${out}" MATCHES "message-status")
  message(FATAL_ERROR "message(STATUS) did not go to stdout")
endif()

if(NOT "${err}" MATCHES "message-default")
  message(FATAL_ERROR "message() did not go to stderr by default")
endif()

if(NOT "${err}" MATCHES "CMake Warning at[^\n]*:\r?\n  message-warning")
  message(FATAL_ERROR "message(WARNING) did not appear properly")
endif()

if(NOT "${err}" MATCHES "CMake Warning \\(dev\\) at[^\n]*:\r?\n  message-author")
  message(FATAL_ERROR "message(AUTHOR_WARNING) did not appear properly")
endif()
