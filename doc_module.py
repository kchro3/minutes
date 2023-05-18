import os


def search_for_main_py():
    for root, dirs, files in os.walk('.'): 
        if 'main.py' in files:
            with open(os.path.join(root, 'main.py'), 'r') as f:
                return f.read()


def generate_docstring():
    main_py = search_for_main_py()
    lines = main_py.split('\n')
    docstring = ''
    for line in lines:
        if 'def' in line:
            function_name = line.split(' ')[1].split('(')[0]
            docstring += f"""\n    {function_name}
    """
    return docstring


def update_module_docstring():
    with open('doc_module.py', 'r') as f:
        lines = f.readlines()
    with open('doc_module.py', 'w') as f:
        for i, line in enumerate(lines):
            if i == 0:
                f.write(generate_docstring())
            f.write(line)


if __name__ == '__main__':
    update_module_docstring()
