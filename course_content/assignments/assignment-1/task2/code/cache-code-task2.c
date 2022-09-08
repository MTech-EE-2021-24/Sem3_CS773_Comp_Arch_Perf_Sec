// CS773: Assignment-1 Task-2

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define KB_BYTES 1024		// 1KiB (Kibibyte) or 1KB = 1024 bytes

void mem_access(int arr_size)
{
	int arr_len_bytes = arr_size * KB_BYTES;
	char arr[arr_len_bytes];		// array of size in multiple of 1024 bytes (1 KiB data)
	int k;

	// accessing the same array multiple times to increase the code size
	// (specifically for smaller arrays) and hence number of instructions
	// for trace file generation
	for ( int j = 0; j < 1000; j++ )
	{
		for ( int i = 0; i < arr_len_bytes; i++ )
		{
			k = arr[i];
		}
	}
}

int main(int argc, char const *argv[])
{
	int arr_size = pow(2, atoi( argv[1]) ) / 1024;

	if ( arr_size >= 1024 )
		printf("Array size input: %d MB or MiB\n", arr_size / 1024);
	else
		printf("Array size input: %d KB or KiB\n", arr_size);

    // execute the function mem_access to access the array of given size input
	mem_access(arr_size);
    
    return 0;
}
