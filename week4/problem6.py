import sys
import random
import string


def main():
    files = [f"file_{''.join(random.choices(string.ascii_lowercase, k=6))}.pdf" for _ in range(100)]
    print("files = ", files)
    # print("length of files =", len(files))
    list_files = list(files)
    # print("list files=", list_files)
    # print("length of list files =", len(list_files))
    # files that have been completely processed
    processed = dict(
        zip(
            random.choices(files, k=10),
            random.choices(range(1, 100), k=10)
        )
    )
    print("Processed files=", processed)
    # list_processed = list(processed)
    # print('list processed', list_processed)
    # print("len processed", len(list_processed))
    # set_processed = set(processed)
    # print("set processed", set_processed)
    # print("length of set processed =", len(set_processed))
    # files currently processing
    processing = random.choices(list(set(files).difference(processed.keys())), k=15)
    print("Processing files =", processing)
    unprocessed = set(files).difference(set(processed).union(set(processing)))
    print("Unprocessed files =", unprocessed)
    print(len(set(processed)) + len(set(processing)) + len(set(unprocessed)) == len(set(files)))
    # list_processing = list(processing)
    # print('list processing', list_processing)
    # print("len processing", len(list_processing))
    # list_total = list_processing + list_processed
    # print("list total", list_total)
    # print("len list", len(list_total))
    # set_processing = set(processing)
    # print("set processing", set_processing)
    # print("length of set processing =", len(set_processing))
    # for i in zip(list_processing, list_processed):
    #    sum_proc = sum()
    #  print("sum proc", sum_proc)
    # unprocessed = list(set_files) - list(set_processing + set_processed)
    # print("unprocessed =", unprocessed)
    # print("length of unprocessed =", len(unprocessed))
    # print(len(set_processed)+len(unprocessed)+len(set_processing))
    # files yet to be processed
    # unprocessed = None
    # todo: files consists the parent set from which we get all files
    # todo: we can use special dictionary methods to get the keys and values ;-)
    # processing+unprocessed+processed = total no. of files
    # draw a picture of program

    return 0


if __name__ == "__main__":
    sys.exit(main())
