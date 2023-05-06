import os

r_val = [0.015625, 0.0625, 0.25, 4, 16, 64]
file_name = "data22d_20.txt"

for r in r_val:
    os.system(f"echo *r:{r}* >> {file_name}")
    os.system(f"echo \n >> {file_name}")
    for i in range(10):
        os.system(f"echo seed:{i} >> {file_name}")
        os.system(f"echo \n >> {file_name}")
        # os.system(f" python localization.py pf --seed {i} --data-factor {r} --filter-factor {r} >> {file_name}")  # b
        # os.system(f" python localization.py pf --seed {i} --filter-factor {r} >> {file_name}")  # c
        os.system(f" python localization.py pf --seed {i} --filter-factor {r} --num-particles {20} >> {file_name}")  # d
        os.system(f"echo \n >> {file_name}")
        os.system(f"echo \n >> {file_name}")
    os.system(f"echo \n >> {file_name}")
    os.system(f"echo \n >> {file_name}")
