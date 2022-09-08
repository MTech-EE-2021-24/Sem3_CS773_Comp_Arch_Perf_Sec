// CS773: Assignment-1 Bonus Task

#include <stdio.h>
#include <time.h>

#define KB_BYTES 1024		// 1KiB (Kibibyte) or 1KB = 1024 bytes

void mem_access()
{
	int arr_len = 1024 * KB_BYTES;
	char arr[arr_len];		// array of size in multiple of 1024 bytes (1 KiB data)
	int k;

	for ( int i = 0; i < arr_len; i++ )
	{
		k = arr[i];

	}
}
void mem_thrash()
{
	int thrash_arr_len = 8 * KB_BYTES * KB_BYTES;
	char large_arr[thrash_arr_len];	// array of large size approx. equal to L3 cache (8 MiB)
	int j;

	for ( int i = 0; i < thrash_arr_len; i++ )
	{
		j = large_arr[i];
	}
}

int main()
{
	// execute the function	mem_thrash
	// to clear all caches
	mem_thrash();

	// clock object for timing
	clock_t start_time, end_time;
	
	// note the start time before executing memory access
	start_time = clock();

	// execute the function mem_access
	mem_access();

	// note the end time after executing memory access
	end_time = clock() - start_time;

	// compute the time taken in seconds
	long double exec_time = ((long double) end_time) / CLOCKS_PER_SEC;

	printf("mem_access took %.9Lf seconds to execute\n", exec_time);

	return 0;
}
