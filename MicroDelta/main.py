import os
from load_data import load_data, align_measurements
from plot import plot_measurements, plot_measured_position
from pathlib import Path

def get_files_in_directory(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def get_files_per_degree(files):
    degrees = ["1degree", "5degree", "10degree"]
    files_per_degree = {degree: [] for degree in degrees}
    for file in files:
        for degree in degrees:
            if file.startswith(degree):
                files_per_degree[degree].append(file)
    return files_per_degree

def get_kp_from_file(file):
    whole_kp = file.split("_")[1]
    whole_kp = whole_kp.split(".")[0]
    value = whole_kp.split("p")[1]
    return f"kp = {value}"

def get_ki_from_file(file):
    whole_ki = file.split("_")[2]
    whole_ki = whole_ki.split(".")[0]
    value = whole_ki.split("i")[1]
    return f"ki = {value}"

def get_kd_from_file(file):
    whole_kd = file.split("_")[2]
    whole_kd = whole_kd.split(".")[0]
    value = whole_kd.split("d")[1]
    return f"kd = {value}"

def get_PID_values_from_file(file):
    whole_pid = file.split("_")
    kp = whole_pid[2]
    ki = whole_pid[3]
    kd = whole_pid[4].split(".")[0]
    kp = kp.split("p")[1]
    ki = ki.split("i")[1]
    kd = kd.split("d")[1]
    return f"kp = {kp}, ki = {ki}, kd = {kd}"

def get_degree(degree):
    if degree == "1degree":
        return 1
    elif degree == "5degree":
        return 5
    elif degree == "10degree":
        return 10
    else:
        return 0
    

def plot_KP(directory_path):
    files = get_files_in_directory(directory_path)
    files_per_degree = get_files_per_degree(files)
    for degree, files in files_per_degree.items():
        measurements = []
        labels = []
        for file in files:
            measurements.append(load_data(directory_path / file))
            labels.append(get_kp_from_file(file))
        plot_measured_position(align_measurements(measurements, get_degree(degree)), labels, save_fig=True, fig_name=f"KP_{degree}.png", title=f"Measured Position: {get_degree(degree)}° increment")
        
def plot_KI(directory_path):
    kp = 20
    degree = 1
    files = get_files_in_directory(directory_path)
    measurements = []
    labels = []
    for file in files:
        measurements.append(load_data(directory_path / file))
        labels.append(get_ki_from_file(file))
    plot_measured_position(align_measurements(measurements, degree), labels, save_fig=True, fig_name=f"KI_{kp}.png", title=f"Measured Position varying ki: kp= {kp}")
    
    
def plot_KD(directory_path):
    kp = 30
    degree = 1
    files = get_files_in_directory(directory_path)
    measurements = []
    labels = []
    for file in files:
        measurements.append(load_data(directory_path / file))
        labels.append(get_kd_from_file(file))
    plot_measured_position(align_measurements(measurements, degree), labels, save_fig=True, fig_name=f"KD_{kp}.png", title=f"Measured Position varying ki: kp = {kp}")   
        
def plot_PID(directory_path):
    degree = 1
    files = get_files_in_directory(directory_path)
    measurements = []
    labels = []
    for file in files:
        measurements.append(load_data(directory_path / file))
        labels.append(get_PID_values_from_file(file))
    plot_measured_position(align_measurements(measurements, degree), labels, save_fig=True, fig_name=f"PID_{degree}.png", title=f"Measured Position for different PID values")
    
def main():
    mod_path = Path(__file__).parent
    plot_KP((mod_path / "../../micro_delta/KP").resolve())
    plot_KI((mod_path / "../../micro_delta/KI").resolve())
    plot_KD((mod_path / "../../micro_delta/KD").resolve())
    plot_PID((mod_path / "../../micro_delta/PID").resolve())
    
if __name__ == "__main__":
    main()