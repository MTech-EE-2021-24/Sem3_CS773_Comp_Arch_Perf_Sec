
# standard imports
import os
import sys
import argparse
import math
import subprocess


NUM_WARM_INSTR = 50 * 1e6	# number of instructions for warm up
NUM_SIM_INSTR = 100 * 1e6	# number of instructions to be simulated


def run_simulation(trace_dir, result_dir):
	"""Run ChampSim simulation for all traces in trace_dir and save results in result_dir

	Args:
		trace_dir (str): directory containing traces
		result_dir (str): directory to save results
	"""
	
	# run simulation for all traces in trace_dir
	for trace_file in os.listdir(trace_dir):

		trace_file = os.path.join(trace_dir, trace_file)

		result_file_name = os.path.splitext(os.path.basename(os.path.splitext(os.path.basename(trace_file))[0]))[0]
		result_file = os.path.join(result_dir, result_file_name + '.txt')

		print("\nRunning simulation for trace: {} ...".format(trace_file))
		print("Results file name: {}".format(result_file))

		command = " ".join(["$CHAMPSIM_ROOT/bin/champsim", "--warmup_instructions", str(int(NUM_WARM_INSTR)),
							"--simulation_instructions", str(int(NUM_SIM_INSTR)), trace_file, ">", result_file, "&"])
		print(); print(command); print()

		subprocess.Popen(command, env=os.environ, shell=True)


if __name__ == '__main__':
	
	# parse arguments
	parser = argparse.ArgumentParser(description='Run ChampSim simulation for generated PIN traces.',
										epilog='Make sure $CHAMPSIM_ROOT is set to the root of your ChampSim installation.')
	parser.add_argument('-t', '--trace_dir', help='path of champsim traces directory', required=True)
	parser.add_argument('-s', '--result_dir', help='path of directory for saving simulation results', required=True)
	args = parser.parse_args()

	# check if trace directory exists
	if not os.path.exists(args.trace_dir):
		print("Error: Trace directory does not exist.")
		sys.exit()
	
	# check if result directory exists
	if not os.path.exists(args.result_dir):
		print("Error: Result directory does not exist.")
		sys.exit()

	trace_dir = args.trace_dir
	result_dir = args.result_dir
	print("Trace directory: {}".format(trace_dir))
	print("Result directory: {}".format(result_dir))

	# run ChampSim simulation on all trace files in trace directory and save results in result directory
	run_simulation(trace_dir, result_dir)
