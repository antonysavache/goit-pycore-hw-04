from pathlib import Path
from colorama import init, Fore, Style

init()

def visualize_directory(directory_path: str):
    directory = Path(directory_path)
    if not directory.is_dir():
        print(f"{Fore.RED}Ошибка: {directory} не является директорией.{Style.RESET_ALL}")
        return

    paths = sorted(directory.rglob('*'))

    tree = {}

    for path in paths:
        rel_path = path.relative_to(directory)
        parts = rel_path.parts

        current = tree
        for part in parts:
            if part not in current:
                current[part] = {}
            current = current[part]

    def print_tree(node, prefix=""):
        items = list(node.items())
        for i, (name, subtree) in enumerate(items):
            is_last = i == len(items) - 1
            print(f"{prefix}{'└── ' if is_last else '├── '}", end="")

            if subtree:
                print(f"{Fore.BLUE}{name}{Style.RESET_ALL}")
                new_prefix = prefix + ("    " if is_last else "│   ")
                print_tree(subtree, new_prefix)
            else:
                print(f"{Fore.GREEN}{name}{Style.RESET_ALL}")

    print(f"{Fore.YELLOW}Структура директории: {directory_path}{Style.RESET_ALL}")
    print_tree(tree)

if __name__ == "__main__":
    path = '.'
    visualize_directory(path)
