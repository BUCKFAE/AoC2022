import os
import re

def main():
    print(f'Creating folders for days 1 to 25')

    with open('day00/day00.py', 'r') as f:
        py_lines = f.read().splitlines()
    with open('day00/test_day00.py', 'r') as f:
        test_lines = f.read().splitlines()

    for day in range(1, 26):
        day_folder = f'day{day:02d}'

        py_file = '\n'.join([re.sub('00', str(day), line) for line in py_lines])
        test_file = '\n'.join([re.sub('00', str(day), line) for line in test_lines])

        if os.path.exists(day_folder):
            print(f'Folder {day_folder} already exists')
            continue

        print(f'Creating folder {day_folder}')
        os.mkdir(day_folder)

        # Creating python file
        with open(f'{day_folder}/day{day:02d}.py', 'w') as f:
            f.writelines(py_file)

        # Creating test file
        with open(f'{day_folder}/test_day{day:02d}.py', 'w') as f:
            f.writelines(test_file)

        # Creating input file
        with open(f'{day_folder}/input.txt', 'w') as f:
            f.writelines('')

        # Creating sample input file
        with open(f'{day_folder}/sample_input.txt', 'w') as f:
            f.writelines('')

        # Creating __init__.py file
        with open(f'{day_folder}/__init__.py', 'w') as f:
            f.writelines('')

if __name__ == '__main__':
    main()
