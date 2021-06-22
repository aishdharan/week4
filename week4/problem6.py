import sys
import random
import string


def main():
    files = [f"file_{''.join(random.choices(string.ascii_lowercase, k=6))}.pdf" for _ in range(100)]
    # files that have been completely processed
    processed = dict(
        zip(
            random.choices(files, k=10),
            random.choices(range(1, 100), k=10)
        )
    )
    set_processed = set(processed)
    print(set_processed)
    # files currently processing
    processing = random.choices(list(set(files).difference(processed.keys())), k=15)
    #print(processing)
    set_processing = set(processing)
    print(set_processing)
    unprocessed = set_processing.difference(set_processed)
    print(unprocessed)
    # files yet to be processed
    # unprocessed = None
    # todo: files consists the parent set from which we get all files
    # todo: we can use special dictionary methods to get the keys and values ;-)


    return 0


if __name__ == "__main__":
    sys.exit(main())
