import os
import numpy as np

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