import shutil

original = r'pythonsqlite.db'
target = r'.\bkp\pythonsqlite_bkp.db'

shutil.copyfile(original, target)
