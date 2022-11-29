# Config file for the Build-tree breakid Package
# It defines the following variables
#  BREAKID_INCLUDE_DIRS - include directories for breakid
#  BREAKID_LIBRARIES    - libraries to link against
#  BREAKID_EXECUTABLE   - the breakid executable

# Compute paths
get_filename_component(BREAKID_CMAKE_DIR "${CMAKE_CURRENT_LIST_FILE}" PATH)
set(BREAKID_INCLUDE_DIRS "/home/kalind/Documents/GitHub/CS773_Comp_Arch_Perf_Sec/course_content/project/sc2020-main-solvers/cryptominisat-ccnr/breakid/build/include")

# Our library dependencies (contains definitions for IMPORTED targets)
include("${BREAKID_CMAKE_DIR}/breakidTargets.cmake")

# These are IMPORTED targets created by breakidTargets.cmake
set(BREAKID_LIBRARIES breakid)
set(BREAKID_STATIC_LIBRARIES breakid)
set(BREAKID_STATIC_LIBRARIES_DEPS )
set(BREAKID_VERSION_MAJOR 1)
set(BREAKID_VERSION_MINOR 0)
set(BREAKID_EXECUTABLE breakid)
