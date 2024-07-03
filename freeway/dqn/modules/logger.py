import os
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
        with open(self.log_file_path + "rewards.txt", 'w') as f:
            json.dump(self.rewards, f, indent=4)

        with open(self.log_file_path + "moving_avg.txt", 'w') as f:
            json.dump(self.moving_averages, f, indent=4)

        with open(self.log_file_path + "distances.txt", 'w') as f:
            json.dump(self.distances, f, indent=4)
        
        with open(self.log_file_path + "epsilons.txt", 'w') as f:
            json.dump(self.epsilons, f, indent=4)