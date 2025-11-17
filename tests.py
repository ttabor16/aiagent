from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file   import write_file
from functions.run_python_file import run_python_file

def get_files_info_tests():
    test_cases = [
        ["calculator","."],
        ["calculator","pkg"],
        ["calculator","/bin"],
        ["calculator","../"]
    ]

    for case in test_cases:
        results = get_files_info(case[0],case[1])
        if case[1] == ".":
            print(f"Result for current directory")
        else:
            print(f"Result for '{case[1]}' directory")
        print(results)

def get_file_content_tests():
    test_cases = [
        #["calculator","lorem.txt"],
        ["calculator","main.py"],
        ["calculator","pkg/calculator.py"],
        ["calculator","/bin/cat"],
        ["calculator","pkg/does_not_exist.py"]
    ]

    for case in test_cases:
        results = get_file_content(case[0],case[1])
        print(results)

def write_file_tests():
    test_cases = [
        ["calculator","lorem.txt","wait, this isn't lorem ipsum"],
        ["calculator","pkg/morelorem.txt","lorem ipsum dolor sit amet"],
        ["calculator","/tmp/temp.txt", "this should not be allowed"]
    ]

    for case in test_cases:
        results = write_file(case[0],case[1],case[2])
        print(results)

def run_python_file_tests():
    test_cases = [
        ["calculator", "main.py"],
        ["calculator", "main.py", ["3 + 5"]],
        ["calculator", "tests.py"],
        ["calculator", "../main.py"],
        ["calculator", "nonexistent.py"],
        ["calculator", "lorem.txt"]
    ]

    for case in test_cases:
        if len(case) == 2:
            results = run_python_file(case[0],case[1])
        if len(case) == 3:
            results = run_python_file(case[0],case[1],case[2])
        print(results)

if __name__ == "__main__":
    #get_files_info_tests()
    #get_file_content_tests()
    #write_file_tests()
    run_python_file_tests()
    