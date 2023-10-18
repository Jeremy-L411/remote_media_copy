import sys
import os
import shutil

from rich.progress import Progress, TransferSpeedColumn, FileSizeColumn, TotalFileSizeColumn

progress = Progress(
    *Progress.get_default_columns(),
    TransferSpeedColumn(),
    FileSizeColumn(),
    TotalFileSizeColumn()
)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        files = os.listdir(sys.argv[1])
        with progress as progress:
            for item in files:
                arg1 = os.path.join(sys.argv[1], item)
                arg2 = os.path.join(sys.argv[2], item)

                desc = os.path.basename(arg1)
                with progress.open(arg1, "rb", description=desc) as src:
                    with open(arg2, "wb") as dst:
                        shutil.copyfileobj(src, dst)
    else:
        print("Copy a file with a progress bar.")
        print("Usage:\n\tpython cp_progress.py SRC DST")
