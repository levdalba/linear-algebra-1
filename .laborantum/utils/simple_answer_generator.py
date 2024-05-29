from importlib.machinery import SourceFileLoader
from json_tricks import dump, load
import os
import argparse

parser = argparse.ArgumentParser(
    prog='Simple Answer Generator',
    description='''
        This script takes students code that is supposed
        to contain the `answer` data structure which holds
        the answer for the task. This data structure is
        saved to json file.
    ''')

parser.add_argument(
    '-s', '--student', 
    help="Path of student's python script with the answer", 
    type=str)

parser.add_argument(
    '-t', '--task',
    help="Task path",
    type=str
)

args = parser.parse_args()

code_path = args.student

## Getting the student's code
user_code = SourceFileLoader("user_code", code_path).load_module()
answer = user_code.answer

## Saving the results
task_path = args.task

answer_path = task_path.split('/')
answer_path[0] = 'solutions'
answer_path.append('answer.json')
answer_path = '/'.join(answer_path)

answer_dir = '/'.join(answer_path.split('/')[:-1])

os.makedirs(answer_dir, exist_ok=True)
dump(answer, answer_path)