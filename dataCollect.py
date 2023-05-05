import os

r_val = [0.015625, 0.0625, 0.25, 4, 16, 64]
file_name = "data2.txt"

for r in r_val:
    os.system(f"echo *r:{r}* >> {file_name}")
    os.system(f"echo \n >> {file_name}")
    for i in range(10):
        os.system(f"echo seed:{i} >> {file_name}")
        os.system(f"echo \n >> {file_name}")
        os.system(f" python localization.py pf --seed {1} --data-factor {r} --filter-factor {r} >> {file_name}")
        os.system(f"echo \n >> {file_name}")
        os.system(f"echo \n >> {file_name}")
    os.system(f"echo \n >> {file_name}")
    os.system(f"echo \n >> {file_name}")
