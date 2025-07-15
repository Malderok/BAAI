from functions.get_files_info import get_files_info


def test():




    # Print each test result
    print(get_files_info("calculator", "."))
    print(get_files_info('directory', 'pkg'))


    # result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    # print("Result for 'pkg' directory:")
    # print(result)

    # result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    # print("Result for '/bin' directory:")
    # print(result)

    # result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    # print("Result for '../' directory:")
    # print(result)



if __name__ == "__main__":
    test()