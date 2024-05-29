from importlib.machinery import SourceFileLoader
from json_tricks import dump, load
import os
import sys
import argparse
import shutil
import yaml

from checker import check_json, write_result
from checker import get_student_path, get_teacher_path
from checker import get_report_path
from checker import ipynb_to_py

from pathlib import Path

print(os.getcwd(), file=sys.stderr)
print(os.listdir('.'), file=sys.stderr)

with open('.laborantum/config.yml') as fin:
    config = yaml.safe_load(fin)

parser = argparse.ArgumentParser(
    prog='Simple Answer Checker',
    description='''
        This script takes student's answer given
        in form of Python data structure (possibly wiht
        Numpy structs) and checks its correspondence with
        the reference answer.

        The answer is supposed to be stored in `answer`
        variable.
    ''')

parser.add_argument(
    '-c', '--code-path', 
    help="Path of student's python script with the answer", 
    type=Path,
    default=None)

parser.add_argument(
    '-t', '--task',
    help="Task path",
    type=Path
)

args = parser.parse_args()

# if args.task is not None:
#     args.task = Path(args.task)

# if args.code_path is not None:
#     args.code_path = Path(args.code_path)

# print(args, file=sys.stderr)

## Trying to resolve the code file if `code_file` is not defined
if args.code_path is None:
    if (args.task / 'task.ipynb').exists():
        args.code_path = args.task / 'task.ipynb'
    elif (args.task / 'task.py').exists():
        args.code_path = args.task / 'task.py'
    else:
        print(args.task.resolve(), file=sys.stderr)
        raise ValueError("""
            Neither `task.py` or `task.ipynb` are found in
            the task directory and no specific `code_path` is
            provided.
        """)

## Converting IPYNB to PY if the code file is IPYNB
if args.code_path.suffix == '.ipynb':
    new_code_path = Path(
        str(args.code_path).replace('.ipynb', '.py'))
    ipynb_to_py(args.code_path, new_code_path)
    args.code_path = new_code_path

code_path = args.code_path
# print(code_path, file=sys.stderr)

## Getting the student's code
# print("Here0", file=sys.stderr)
user_code = SourceFileLoader(
    "user_code", str(args.code_path)).load_module()
# print("Here1", file=sys.stderr)
answer = user_code.answer
# print("Here2", file=sys.stderr)

# print(answer, file=sys.stderr)

## Saving the results
student_path = get_student_path(args.task)
student_path.parent.mkdir(parents=True, exist_ok=True)
student_path.unlink(missing_ok=True)
dump(answer, str(student_path))

## Getting paths
student_path = get_student_path(args.task)
teacher_path = get_teacher_path(args.task)
report_path = get_report_path(args.task)

## Creating teachers answer
if not teacher_path.exists():
    if config['editable']:
        teacher_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(student_path, teacher_path)
    else:
        raise ValueError("""
            No teacher's answer found and the editing mode
            is turned off.
        """)

## Loading answers
student_result = load(str(student_path))
teacher_path = load(str(teacher_path))

# Checking answers
report = check_json(args.task)




