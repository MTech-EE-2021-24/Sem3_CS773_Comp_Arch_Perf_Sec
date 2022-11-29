/******************************************
Copyright (c) 2017, Mate Soos

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
***********************************************/

#include "src/GitSHA1.h"

const char* CMSat::get_version_sha1()
{
    static const char myversion_sha1[] = "51feb442e996885c5fb535afd1c37fa91530fe49";
    return myversion_sha1;
}

const char* CMSat::get_version_tag()
{
    static const char myversion_tag[] = "5.6.8";
    return myversion_tag;
}

const char* CMSat::get_compilation_env()
{
    static const char compilation_env[] =
    "CMAKE_CXX_COMPILER = /usr/bin/c++ | "
    "CMAKE_CXX_FLAGS =  -fno-stack-protector -fvisibility=hidden -Wlogical-op -Wrestrict -Wnull-dereference -Wdouble-promotion -Wshadow -Wformat=2 -Wextra-semi -pedantic | "
    "COMPILE_DEFINES =  -DUSE_GAUSS -DNDEBUG -D_FORTIFY_SOURCE=0 -DYALSAT_FPU -DUSE_M4RI -DUSE_BREAKID | "
    "STATICCOMPILE = ON | "
    "ONLY_SIMPLE = ON | "
    "Boost_FOUND =  | "
    "STATS = OFF | "
    "SQLITE3_FOUND = FALSE | "
    "ZLIB_FOUND =  | "
    "VALGRIND_FOUND =  | "
    "ENABLE_TESTING = OFF | "
    "M4RI_FOUND = TRUE | "
    "NOM4RI = OFF | "
    "SLOW_DEBUG = OFF | "
    "ENABLE_ASSERTIONS = OFF | "
    "PYTHON_EXECUTABLE = PYTHON_EXECUTABLE-NOTFOUND | "
    "PYTHON_LIBRARY = PYTHON_LIBRARY-NOTFOUND | "
    "PYTHON_INCLUDE_DIRS =  | "
    "MY_TARGETS =  | "
    "LARGEMEM = OFF | "
    "LIMITMEM = OFF | "
    "BREAKID_LIBRARIES = breakid | "
    "BREAKID-VER = 1.0 | "
    "BOSPHORUS_LIBRARIES =  | "
    "BOSPH-VER = . | "
    "compilation date time = " __DATE__ " " __TIME__
    ""
    ;
    return compilation_env;
}
