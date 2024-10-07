# photo_organiser/__main__
import re
import sys

from photo_organiser.parser import parse_args

month_map = {
    '01': 'jan mar',
    '02': 'jan mar',
    '03': 'jan mar',
    '04': 'apr jun',
    '05': 'apr jun',
    '06': 'apr jun',
    '07': 'jul sep',
    '08': 'jul sep',
    '09': 'jul sep',
    '10': 'oct dec',
    '11': 'oct dec',
    '12': 'oct dec',
}


def main():
    # Get command line arguments
    args = parse_args(sys.argv[1:])

    # validate source directory exists
    if not args.source.exists():
        sys.exit(f"Error: Source path '{args.source}' does not exist")

    # iterate over files in source directory
    file_moved_count = 0
    for file_path in args.source.iterdir():
        # ignore subfolders
        if not file_path.is_file():
            continue

        # attempt to extract date from filename
        file_date = re.findall(r'\d{8}', str(file_path))
        if len(file_date) == 0:
            print(f"Warning: Could not extract date from file '{file_path}'")
            continue
        file_date = file_date[0]

        # check if file already exists
        dest_file_path = args.dest.joinpath(file_date[0:4], month_map[file_date[4:6]])
        dest_file_path.mkdir(parents=True, exist_ok=True)
        if dest_file_path.joinpath(file_path.name).exists():
            print(f"Warning: file '{dest_file_path}' already exists in directory '{dest_file_path}'")
            continue

        # move file to destination directory
        file_path.rename(dest_file_path / file_path.name)

        file_moved_count += 1

    print(f"Moved {file_moved_count} files")


if __name__ == '__main__':
    main()
