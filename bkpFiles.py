import shutil

backup04 = r'.\bkp\pythonsqlite_bkp_old4.db'
backup03 = r'.\bkp\pythonsqlite_bkp_old3.db'
backup02 = r'.\bkp\pythonsqlite_bkp_old2.db'
backup01 = r'.\bkp\pythonsqlite_bkp_old.db'
target = r'.\bkp\pythonsqlite_bkp.db'
original = r'pythonsqlite.db'

shutil.copyfile(backup03, backup04)
shutil.copyfile(backup02, backup03)
shutil.copyfile(backup01, backup02)
shutil.copyfile(target, backup01)
shutil.copyfile(original, target)
