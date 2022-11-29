cmake_policy(SET CMP0007 NEW) # Suppress warnings see `cmake --help-policy CMP0007`

if (NOT EXISTS "/home/kalind/Documents/GitHub/CS773_Comp_Arch_Perf_Sec/course_content/project/sc2020-main-solvers/cryptominisat-ccnr/cms/build/install_manifest.txt")
    message(FATAL_ERROR "Cannot find install manifest: \"/home/kalind/Documents/GitHub/CS773_Comp_Arch_Perf_Sec/course_content/project/sc2020-main-solvers/cryptominisat-ccnr/cms/build/install_manifest.txt\"")
endif(NOT EXISTS "/home/kalind/Documents/GitHub/CS773_Comp_Arch_Perf_Sec/course_content/project/sc2020-main-solvers/cryptominisat-ccnr/cms/build/install_manifest.txt")

file(READ "/home/kalind/Documents/GitHub/CS773_Comp_Arch_Perf_Sec/course_content/project/sc2020-main-solvers/cryptominisat-ccnr/cms/build/install_manifest.txt" files)
string(REGEX REPLACE "\n" ";" files "${files}")
list(REVERSE files)
foreach (file ${files})
    message(STATUS "Uninstalling \"$ENV{DESTDIR}${file}\"")
    if (EXISTS "$ENV{DESTDIR}${file}")
        execute_process(
            COMMAND /home/kalind/Documents/GitHub/CS773_Comp_Arch_Perf_Sec/course_content/project/sc2020-main-solvers/cryptominisat-ccnr/cmake-3.12.0/bin/cmake -E remove "$ENV{DESTDIR}${file}"
            OUTPUT_VARIABLE rm_out
            RESULT_VARIABLE rm_retval
        )
        if(NOT ${rm_retval} EQUAL 0)
            message(FATAL_ERROR "Problem when removing \"$ENV{DESTDIR}${file}\"")
        endif (NOT ${rm_retval} EQUAL 0)
    else (EXISTS "$ENV{DESTDIR}${file}")
        message(STATUS "File \"$ENV{DESTDIR}${file}\" does not exist.")
    endif (EXISTS "$ENV{DESTDIR}${file}")
endforeach(file)
