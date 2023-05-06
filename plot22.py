import matplotlib.pyplot as plt
import re
import numpy as np

file_name = "data22d_20.txt"

with open(file_name, "r") as file:
    output = file.read()

mean_pos_err_pattern = r"Mean position error: ([\d\.]+)"
r_pattern = r"r:([\d\.]+)"
seed_pattern = r"seed:(\d+)"
mean_mahal_err_pattern = r"Mean Mahalanobis error: ([\d\.]+)"
anees_pattern = r"ANEES: ([\d\.]+)"
anees = re.findall(anees_pattern, output)

mean_pos_err = re.findall(mean_pos_err_pattern, output)
r = re.findall(r_pattern, output)
seed = re.findall(seed_pattern, output)
mean_mahal_err = re.findall(mean_mahal_err_pattern, output)

mean_pos_err = [float(i) for i in mean_pos_err]
mean_mahal_err = [float(i) for i in mean_mahal_err]
r = [float(i) for i in r]
anees = [float(i) for i in anees]

avg_pos_err = []
sd_pos_err = []
avg_mahal_err = []
avg_anees = []
sd_anees = []

for i in range(0, 60, 10):
    avg_pos_err.append(np.mean(mean_pos_err[i:i+10]))
    sd_pos_err.append(np.std(mean_pos_err[i:i+10]))
    avg_mahal_err.append(np.mean(mean_mahal_err[i:i+10]))
    avg_anees.append(np.mean(anees[i:i+10]))
    sd_anees.append(np.std(anees[i:i+10]))


print("r: ", r)
print("mean_pos_err: ", avg_pos_err)
print("sd pos_err: ", sd_pos_err)
print("mean_mahal_err: ", avg_mahal_err)
print("anees: ", avg_anees)
print("anees sd: ", sd_anees)

# anees = plt.figure()
# plt.plot(r, avg_anees, label="avg ANEES", color="mediumspringgreen")
# plt.fill_between(r, np.subtract(avg_anees, sd_anees), np.add(avg_anees, sd_anees), color="lightblue")
# plt.title("2.2b")
# plt.xlabel("r")
# plt.savefig("./plot/2.2b_ANEES.png")
# plt.show()

# pos = plt.figure()
# plt.plot(r, avg_pos_err, label="avg pos err", color="mediumspringgreen")
# plt.fill_between(r, np.subtract(avg_pos_err, sd_pos_err), np.add(avg_pos_err, sd_pos_err), color="lightblue")
# plt.title("2.2b")
# plt.xlabel("r")
# plt.savefig("./plot/2.2b_pos.png")
# plt.show()

# anees = plt.figure()
# plt.plot(r, avg_anees, label="avg ANEES", color="sienna")
# plt.fill_between(r, np.subtract(avg_anees, sd_anees), np.add(avg_anees, sd_anees), color="lightblue")
# plt.title("2.2c")
# plt.xlabel("r")
# plt.savefig("./plot/2.2c_ANEES.png")
# plt.show()

# pos = plt.figure()
# plt.plot(r, avg_pos_err, label="avg pos err", color="sienna")
# plt.fill_between(r, np.subtract(avg_pos_err, sd_pos_err), np.add(avg_pos_err, sd_pos_err), color="lightblue")
# plt.title("2.2c")
# plt.xlabel("r")
# plt.savefig("./plot/2.2c_pos.png")
# plt.show()

anees = plt.figure()
plt.plot(r, avg_anees, label="avg ANEES", color="fuchsia")
plt.fill_between(r, np.subtract(avg_anees, sd_anees), np.add(avg_anees, sd_anees), color="lightblue")
plt.title("2.2d 20 particles")
plt.xlabel("r")
plt.savefig("./plot/2.2d_20_ANEES.png")
plt.show()

pos = plt.figure()
plt.plot(r, avg_pos_err, label="avg pos err", color="fuchsia")
plt.fill_between(r, np.subtract(avg_pos_err, sd_pos_err), np.add(avg_pos_err, sd_pos_err), color="lightblue")
plt.title("2.2d 20 particles")
plt.xlabel("r")
plt.savefig("./plot/2.2d_20_pos.png")
plt.show()
