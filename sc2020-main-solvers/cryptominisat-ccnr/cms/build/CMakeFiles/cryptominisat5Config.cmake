# Config file for the installed cryptominisat Package
# It defines the following variables
#  CRYPTOMINISAT5_INCLUDE_DIRS - include directories for cryptominisat5
#  CRYPTOMINISAT5_LIBRARIES    - libraries to link against
#  CRYPTOMINISAT5_EXECUTABLE   - the cryptominisat executable

# Compute paths
get_filename_component(CRYPTOMINISAT5_CMAKE_DIR "${CMAKE_CURRENT_LIST_FILE}" PATH)
set(CRYPTOMINISAT5_INCLUDE_DIRS "/usr/local/include")

# Our library dependencies (contains definitions for IMPORTED targets)
include("${CRYPTOMINISAT5_CMAKE_DIR}/cryptominisat5Targets.cmake")

# These are IMPORTED targets created by cryptominisat5Targets.cmake
set(CRYPTOMINISAT5_LIBRARIES cryptominisat5)
set(CRYPTOMINISAT5_STATIC_LIBRARIES cryptominisat5)
set(CRYPTOMINISAT5_STATIC_LIBRARIES_DEPS /home/kalind/Documents/GitHub/CS773_Comp_Arch_Perf_Sec/course_content/project/sc2020-main-solvers/cryptominisat-ccnr/m4ri-20200125/myinstall/lib/libm4ri.a)
set(CRYPTOMINISAT5_VERSION_MAJOR 5)
set(CRYPTOMINISAT5_VERSION_MINOR 6)
set(CRYPTOMINISAT5_EXECUTABLE cryptominisat5)
