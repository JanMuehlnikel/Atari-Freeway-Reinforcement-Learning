import os
import numpy as np
import json

class EpisodeLogger:
    def __init__(self, log_files_dir="logs/"):
        self.log_file_path = log_files_dir
        os.makedirs(os.path.dirname(log_files_dir), exist_ok=True)
        self.rewards = []
        self.moving_averages = []
        self.distances = []
        self.epsilons = []

    def log_episode(self, total_reward, moving_average, epsilon, distance):
        self.rewards.append(total_reward)
        self.moving_averages.append(moving_average)
        self.distances.append(distance)
        self.epsilons.append(epsilon)

        self._save_all_logs()

    def _save_all_logs(self):
        np.save(self.log_file_path + "rewards.npy", np.array(self.rewards))

        np.save(self.log_file_path + "moving_avg.npy", np.array(self.moving_averages))

        np.save(self.log_file_path + "distances.npy", np.array(self.distances))

        np.save(self.log_file_path + "epsilons.npy", np.array(self.epsilons))

def save_params(param_dict, params_dir, MODEL_VERSION):
    def convert_to_serializable(obj):
        if isinstance(obj, dict):
            return {key: convert_to_serializable(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [convert_to_serializable(element) for element in obj]
        elif isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return obj
        
    serializable_params = convert_to_serializable(param_dict)
    os.makedirs(os.path.dirname(params_dir), exist_ok=True)
    with open(f"{params_dir}/parameters_{MODEL_VERSION}.json", "w") as f:
        json.dump(serializable_params, f, indent=4)
