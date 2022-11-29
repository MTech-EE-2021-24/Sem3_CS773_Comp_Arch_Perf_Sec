# CMake generated Testfile for 
# Source directory: /home/kalind/Documents/GitHub/CS773_Comp_Arch_Perf_Sec/course_content/project/sc2020-main-solvers/cryptominisat-ccnr/cmake-3.12.0/Utilities/cmcurl
# Build directory: /home/kalind/Documents/GitHub/CS773_Comp_Arch_Perf_Sec/course_content/project/sc2020-main-solvers/cryptominisat-ccnr/cmake-3.12.0/Utilities/cmcurl
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(curl "LIBCURL" "http://open.cdash.org/user.php")
subdirs("lib")
