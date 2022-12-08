from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass
class directory:
    name: str
    parent: directory | None
    folders: dict[str, directory]

    # File: name, size
    files: list[tuple[str, int]]
    size: int | None


def get_dir_size(dir: directory) -> int:

    # If size was already calculated, return it
    if dir.size:
        return dir.size

    to_handle = [dir]

    size = 0

    while to_handle:
        current = to_handle.pop()
        current_files_size = sum([size for _, size in current.files])
        current_folders_size = sum([get_dir_size(folder) for folder in current.folders.values()])

        size += current_files_size + current_folders_size

    # Caching the size
    dir.size = size

    return size

def find_dir(root: directory, name: str) -> directory:
    if root.name == name:
        return root

    for folder in root.folders.values():
        return find_dir(folder, name)

    raise ValueError(f'Could not find directory {name}')

def iterate_dirs(root: directory):
    yield root

    for folder in root.folders.values():
        yield from iterate_dirs(folder)

def create_directory_tree(input_file: str) -> directory:
    assert os.path.exists(input_file), f'File {input_file} does not exist'

    root = directory('/', None, {}, [], None)

    with open(input_file, 'r') as f:
        commands = [line.strip() for line in f.read().splitlines() if line.strip()]

        assert commands[0] == '$ cd /', f'Expected to start in the root dir'

        current_dir = root

        idx = 1
        while idx < len(commands):
            command = commands[idx]
            print(f'Command {idx}: {command}')
            if command.startswith('$ cd '):
                # Change directory
                tgt = command.removeprefix('$ cd ')
                print(f'Target: {tgt}')

                if tgt == '..':
                    # Go up one level
                    assert current_dir.parent is not None, f'Cannot go up from root'
                    current_dir = current_dir.parent
                else:
                    # Checking if we already know the folder
                    known_folder = tgt in current_dir.folders.keys()
                    print(f'Folder is known: {known_folder}')

                    if known_folder:
                        current_dir = current_dir.folders[tgt]
                    else:
                        # Create new folder
                        new_dir = directory(tgt, current_dir, {}, [], None)
                        current_dir.folders[tgt] = new_dir
                        current_dir = new_dir

                # Going to the next instruction
                idx += 1

            elif command.startswith('$ ls'):
                # List directory
                next_command_index = [i for i in range(idx + 1, len(commands)) if commands[i].startswith('$')]

                # Last command
                if not next_command_index:
                    next_command_index = len(commands)
                else:
                    # Not last command
                    next_command_index = next_command_index[0]
                    print(f'Next command: {commands[next_command_index]} - {next_command_index}')

                for entry in range(idx + 1, next_command_index):
                    content = commands[entry]
                    if content.startswith('dir '):
                        # Directory
                        dir_name = content.removeprefix('dir ')
                        assert dir_name not in current_dir.folders.keys(), f'Directory {dir_name} already exists'
                        print(f'Found dir: {dir_name}')
                        current_dir.folders[dir_name] = directory(dir_name, current_dir, {}, [], None)
                    else:
                        size, name = content.split(' ')
                        size = int(size)
                        print(f'Found file: {name} - {size}')
                        current_dir.files.append((name, size))

                # Going to the next instruction
                idx = next_command_index
            else:
                # Unknown command
                raise ValueError(f'Unknown command: {command} in line {idx})')
    return root

def solve(input_file: str)-> tuple[int, int]:

    res1 = 0
    root = create_directory_tree(input_file)
    for dir in iterate_dirs(root):
        size = get_dir_size(dir)
        if size <= 100_000:
            res1 += size

    res2 = 0

    disk_space = 70_000_000
    total_space_required = 30_000_000
    current_space = get_dir_size(root)
    free_space = disk_space - current_space
    missing_space_required = total_space_required - free_space

    res2 = min([d for d in iterate_dirs(root) if d.size >= missing_space_required ], key=lambda d: d.size).size

    return res1, res2


if __name__ == '__main__':


    # Testing size of directories
    root1 = create_directory_tree('day07/sample_input.txt')
    assert get_dir_size(root1) == 48381165, f'Expected 48381165, got {get_dir_size(root1)}'
    assert get_dir_size(find_dir(root1, 'e')) == 584, f'Expected 584, got {get_dir_size(find_dir(root1, "e"))}'

    res_sample = solve('day07/sample_input.txt')

    assert res_sample[0] == 95437, f'Expected 95437, got {res_sample[0]}'
    assert res_sample[1] == 24933642, f'Expected 24933642, got {res_sample[1]}'

    res = solve('day07/input.txt')
    print(f'Part 1: {res[0]} - Part 2: {res[1]}')
