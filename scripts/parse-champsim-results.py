
# standard imports
import os
import sys
import argparse

NUM_SIM_INSTR = 100 * 1e6	# number of instructions simulated

# parameters of interest from ChampSim result
params = {
	'ipc': 0,
	'per_l1d_hits': 0,
	'num_l1d_load_misses': 0,
	'l1d_mpki': 0,
	# 'per_l1i_hits': 0,
	'per_l2c_hits': 0,
	'num_l2c_load_misses': 0,
	'l2c_mpki': 0,
	'per_llc_hits': 0,
	'num_llc_load_misses': 0,
	'llc_mpki': 0,
	'per_branch_pred_acc': 0,
	'branch_mpki': 0,
	'avg_rob_occup_at_mispred': 0,
	'branch_dir_jump': 0,
	'branch_indir': 0,
	'branch_cond': 0,
	'branch_dir_call': 0,
	'branch_indir_call': 0,
	'branch_ret': 0,
	'branch_other': 0
}

# text to search for in ChampSim result
search_text = {
	'ipc': 'CPU 0 cumulative IPC:',
	'per_l1d_hits': 'cpu0_L1D TOTAL     ACCESS:',
	'num_l1d_load_misses': 'cpu0_L1D LOAD      ACCESS:',
	'l1d_mpki': '',
	# 'per_l1i_hits': 'cpu0_L1I TOTAL     ACCESS:',
	'per_l2c_hits': 'cpu0_L2C TOTAL     ACCESS:',
	'num_l2c_load_misses': 'cpu0_L2C LOAD      ACCESS:',
	'l2c_mpki': '',
	'per_llc_hits': 'LLC TOTAL     ACCESS:',
	'num_llc_load_misses': 'LLC LOAD      ACCESS:',
	'llc_mpki': '',
	'per_branch_pred_acc': 'CPU 0 Branch Prediction Accuracy:',
	'branch_mpki': 'CPU 0 Branch Prediction Accuracy:',
	'avg_rob_occup_at_mispred': 'CPU 0 Branch Prediction Accuracy:',
	'branch_dir_jump': 'BRANCH_DIRECT_JUMP:',
	'branch_indir': 'BRANCH_INDIRECT:',
	'branch_cond': 'BRANCH_CONDITIONAL:',
	'branch_dir_call': 'BRANCH_DIRECT_CALL:',
	'branch_indir_call': 'BRANCH_INDIRECT_CALL:',
	'branch_ret': 'BRANCH_RETURN:',
	'branch_other': ''
}


if __name__ == '__main__':

	# parse arguments
	parser = argparse.ArgumentParser(description='Parse the given ChampSim results txt file.')
	parser.add_argument('-c', '--champsim_result', help='champsim result file', required=True)
	args = parser.parse_args()

	# check if champsim result file exists
	if not os.path.exists(args.champsim_result):
		print("ChampSim result file not found.")
		sys.exit()
	
	champsim_result_file = args.champsim_result
	print("Parsing ChampSim result file: " + champsim_result_file)

	# read champsim result file
	with open(champsim_result_file, 'r') as f:
		lines = f.readlines()
	
	# parse champsim result file
	for item in params:
		text = ''
		searched_data = ''
		if item == 'l1d_mpki' or item == 'l2c_mpki' or item == 'llc_mpki' or item == 'branch_other':
			pass
		else:
			text = search_text[item]
			searched_data = lines[[i for i in range(len(lines)) if lines[i].startswith(text)][0]][len(text):].split()
		# print(item, "\t", text, searched_data)

		if item == 'ipc':
			params[item] = float(searched_data[0])
		elif item == 'per_l1d_hits':
			params[item] = round((float(searched_data[2]) / float(searched_data[0])) * 100, 4)
		elif item == 'num_l1d_load_misses':
			params[item] = int(searched_data[-1])
		elif item == 'l1d_mpki':
			params[item] = round((float(params['num_l1d_load_misses']) / NUM_SIM_INSTR) * 1000, 4)
		# elif item == 'per_l1i_hits':
		# 	params[item] = round((float(searched_data[2]) / float(searched_data[0])) * 100, 4)
		elif item == 'per_l2c_hits':
			params[item] = round((float(searched_data[2]) / float(searched_data[0])) * 100, 4)
		elif item == 'num_l2c_load_misses':
			params[item] = int(searched_data[-1])
		elif item == 'l2c_mpki':
			params[item] = round((float(params['num_l2c_load_misses']) / NUM_SIM_INSTR) * 1000, 4)
		elif item == 'per_llc_hits':
			params[item] = round((float(searched_data[2]) / float(searched_data[0])) * 100, 4)
		elif item == 'num_llc_load_misses':
			params[item] = int(searched_data[-1])
		elif item == 'llc_mpki':
			params[item] = round((float(params['num_llc_load_misses']) / NUM_SIM_INSTR) * 1000, 4)
		elif item == 'per_branch_pred_acc':
			params[item] = round(float(searched_data[0][:-1]), 4)
		elif item == 'branch_mpki':
			params[item] = round(float(searched_data[2]), 4)
		elif item == 'avg_rob_occup_at_mispred':
			params[item] = round(float(searched_data[-1]), 4)
		elif item == 'branch_dir_jump':
			params[item] = round(float(searched_data[-1]), 5)
		elif item == 'branch_indir':
			params[item] = round(float(searched_data[-1]), 5)
		elif item == 'branch_cond':
			params[item] = round(float(searched_data[-1]), 5)
		elif item == 'branch_dir_call':
			params[item] = round(float(searched_data[-1]), 5)
		elif item == 'branch_indir_call':
			params[item] = round(float(searched_data[-1]), 5)
		elif item == 'branch_ret':
			params[item] = round(float(searched_data[-1]), 5)
	
	# print parsed champsim result
	print("\nParsed ChampSim result:")
	for item in params:
		# print(item, "\t", params[item])
		print(params[item], end=",")
	print()
