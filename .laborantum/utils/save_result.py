import json_tricks
from pathlib import Path
from checker import get_student_path

def 

def apply_function(foo, inputs, key=''):
    res = []
    for inp in inputs:
        res.append(foo(**inp))
    students_path = Path('results')
    if key == '':
        fname = 'result.json'
    else:
        fname = key + '_result.json'
    students_path = get_student_path(
        students_path.resolve(), 
        fname=fname)
    students_path.parent.mkdir(parents=True, exist_ok=True)
    json_tricks.dump(res, str(students_path))