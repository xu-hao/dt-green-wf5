import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--cohort_id")
parser.add_argument("--maximum_p_value", type=float)
args = parser.parse_args()

from workflow5 import module2_4_question2

print(module2_4_question2(args.cohort_id, args.maximum_p_value))