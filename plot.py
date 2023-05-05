import matplotlib.pyplot as plt
import re
import numpy as np

file_name = "data2.txt"

with open(file_name, "r") as file:
    output = file.read()

mean_pos_err_pattern = r"Mean position error: ([\d\.]+)"
r_pattern = r"r:([\d\.]+)"
seed_pattern = r"seed:(\d+)"
mean_mahal_err_pattern = r"Mean Mahalanobis error: ([\d\.]+)"

mean_pos_err = re.findall(mean_pos_err_pattern, output)
r = re.findall(r_pattern, output)
seed = re.findall(seed_pattern, output)
mean_mahal_err = re.findall(mean_mahal_err_pattern, output)

mean_pos_err = [float(i) for i in mean_pos_err]
mean_mahal_err = [float(i) for i in mean_mahal_err]
r = [float(i) for i in r]

avg_pos_err = []
avg_mahal_err = []

for i in range(0, 60, 10):
    avg_pos_err.append(np.mean(mean_pos_err[i:i+10]))
    avg_mahal_err.append(np.mean(mean_mahal_err[i:i+10]))

print("r: ", r)
print("mean_pos_err: ", avg_pos_err)
print("mean_mahal_err: ", avg_mahal_err)

mahal = plt.figure()
plt.plot(r, avg_mahal_err, label="avg mahal err", color="tomato")
plt.title("2.2b")
plt.xlabel("r")
plt.show()

pos = plt.figure()
plt.plot(r, avg_pos_err, label="avg pos err", color="deepskyblue")
plt.title("2.2b")
plt.xlabel("r")
plt.show()
