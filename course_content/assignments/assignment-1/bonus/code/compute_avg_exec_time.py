
import os
import time

task1_exe_cmd = "./cache-code-task1"

exec_time_list = []

for i in range(1000):
	exec_time = float(os.popen(task1_exe_cmd).read().strip()[16:27])
	exec_time_list.append(exec_time)
	time.sleep(0.1)

print("Average exec time in us: ", ( sum(exec_time_list) / len(exec_time_list) * 1e6 ))
