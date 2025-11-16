from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

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

if __name__ == "__main__":
    #get_files_info_tests()
    get_file_content_tests()