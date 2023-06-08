import sys
if len(sys.argv) < 3:
        print_usage()

dataset = sys.argv[1]
metric_type = sys.argv[2]
eval_names = []
eval_files = []
eval_errs = []

for idx in range(3, len(sys.argv), 2):
    in_name = sys.argv[idx]
    in_file = sys.argv[idx+1]
    eval_names.append(in_name)
    eval_files.append(in_file)
print(eval_names, eval_files, eval_errs)