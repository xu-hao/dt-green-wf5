import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--cohort_id")
parser.add_argument("--maximum_p_value", type=float)
args = parser.parse_args()

from workflow5 import module2_4_question1

print(module2_4_question1(args.cohort_id, args.maximum_p_value))