
# standard imports
import os
import sys
import argparse
import math
import subprocess


INTERVAL_SIZE = 100 * 1e6	# 100M instructions


def create_traces(simpoint_file, program_file, benchmark_file, sorted_simpoints, trace_dir):
	"""Create traces for each simpoint for given program and benchmark.

	Args:
		simpoint_file (str): path to simpoint file
		program_file (str): path to program file
		benchmark_file (str): path to benchmark file
		sorted_simpoints (list): list of sorted simpoints
		trace_dir (str): path to trace directory
	"""
	
	# create trace directory
	if not os.path.exists(trace_dir):
		os.makedirs(trace_dir)
	
	# create traces
	for simpoint in sorted_simpoints[:3]:

		fast_forward_simpoint = (simpoint * INTERVAL_SIZE)
		trace_file_name = os.path.join(trace_dir, os.path.splitext(os.path.basename(simpoints_file))[0] +
										'-' + str(math.trunc(fast_forward_simpoint / 1e9)) + 'B.champsimtrace')
		
		print("\nCreating trace for simpoint: {} ...".format(simpoint))
		print("Trace file name: {}".format(trace_file_name))
		
		# p = subprocess.Popen(["echo $CHAMPSIM_ROOT"], env=os.environ, shell=True)
		# p.communicate()

		command = " ".join(["$PIN_ROOT/pin", "-t", "$CHAMPSIM_ROOT/tracer/pin/obj-intel64/champsim_tracer.so",
							"-o", trace_file_name, "-s", str(int(fast_forward_simpoint)), "-t", str(int(INTERVAL_SIZE)),
							"--", program_file, benchmark_file, "&&", "xz", trace_file_name, "&"])
		print(); print(command); print()

		subprocess.Popen(command, env=os.environ, shell=True)


if __name__ == '__main__':
	
	# parse arguments
	parser = argparse.ArgumentParser(description='Generate PIN traces for given simpoints and program with benchmarks.',
										epilog='Make sure $PIN_ROOT is set to the root of your PIN installation and \
												$CHAMPSIM_ROOT is set to the root of your ChampSim installation.')
	parser.add_argument('-s', '--simpoints', help='simpoints file', required=True)
	parser.add_argument('-w', '--weights', help='weights file', required=True)
	parser.add_argument('-p', '--program', help='program executable file', required=True)
	parser.add_argument('-b', '--benchmark', help='corresponding benchmark file', required=True)
	args = parser.parse_args()

	# check if simpoints file exists
	if not os.path.exists(args.simpoints):
		print("Simpoints file not found.")
		sys.exit()
	
	# check if weights file exists
	if not os.path.exists(args.weights):
		print("Weights file not found.")
		sys.exit()
	
	# check if program file exists
	if not os.path.exists(args.program):
		print("Program file not found.")
		sys.exit()
	
	# check if benchmark file exists
	if not os.path.exists(args.benchmark):
		print("Benchmark file not found.")
		exit()
	
	simpoints_file = args.simpoints
	weights_file = args.weights
	program_file = args.program
	benchmark_file = args.benchmark
	
	# get sorted simpoints and weights
	simpoints = []
	weights = []
	arranged_weights = []
	cluster_labels = []

	# read simpoints file
	with open(simpoints_file, 'r') as f:
		for line in f:
			line = line.strip()
			simpoints.append(int(line.split()[0]))
			cluster_labels.append(int(line.split()[1]))
	
	print("\nSimpoints: ", simpoints)
	print("Cluster labels: ", cluster_labels)
	
	# read weights file
	with open(weights_file, 'r') as f:
		for line in f:
			line = line.strip()
			weights.append(float(line.split()[0]))
	
	print("\nWeights: ", weights)
	print("Cluster labels: ", cluster_labels)

	# sort simpoints with cluster labels
	simpoints, cluster_labels = (list(t) for t in zip(*sorted(zip(simpoints, cluster_labels))))

	print("\nSorted simpoints: ", simpoints)
	print("Sorted cluster labels: ", cluster_labels)
	
	# arrange weights w.r.t. sorted simpoints
	for label in cluster_labels:
		arranged_weights.append(weights[label])
	
	print("\nSimpoint	|	Cluster Label	|	Weight")
	for idx in range(len(cluster_labels)):
		print(str(simpoints[idx]) + "\t|\t" + str(cluster_labels[idx]) + "\t|\t" + str(arranged_weights[idx]))

	# create traces for each simpoint
	trace_root_dir = os.path.join(os.getcwd(), '../simpoint_pin_traces')
	if not os.path.exists(trace_root_dir):
		os.makedirs(trace_root_dir)

	trace_dir = os.path.join(trace_root_dir, os.path.splitext(os.path.basename(simpoints_file))[0])
	print("\nTraces will be saved in this directory: ", trace_dir)

	create_traces(simpoints_file, program_file, benchmark_file, simpoints, trace_dir)

