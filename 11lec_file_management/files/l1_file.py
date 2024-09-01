from pathlib import Path
from time import ctime

file = Path("files/file-test.txt")

# file.exists() # Valid if the file exists
# file.unlink()  # remove the file or link
# file.rename("uno/file-test.txt") # It renames file path to target path
# file.stat() # It gives us the file statistics
print(file.stat())  # os.stat_result(st_mode=33206, st_ino=1125899907767792, st_dev=8954984664196371708, st_nlink=1, st_uid=0, st_gid=0, st_size=579, st_atime=1724139331, st_mtime=1724139072, st_ctime=1724139067)
# st_size: size file on disc
# st_atime: file's access date
# st_mtime: file's modify date
# st_ctime: In windows, It's the creation date, but in Linux/Mac It represents the metadata changed date

# by defaut the format date of st_atime is timestamp (unix date)
stat = file.stat()
print("access date", ctime(stat.st_atime))
print("creation date", ctime(stat.st_birthtime))
print("modification date", ctime(stat.st_mtime))
