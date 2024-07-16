# Implementing RF to play the Atari Freeway game

https://gymnasium.farama.org/environments/atari/freeway/

## Schriftliche Ausarbeitung
https://www.overleaf.com/read/bytbrzgrtssh#d2c941

# Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone [https://github.com/yourusername/your-repo.git](https://github.com/JanMuehlnikel/Atari-Freeway-Reinforcement-Learning)
    cd your-repo
    ```

2. **Create and Activate a New Conda Environment**:
    ```bash
    conda create --name new_env_name python=3.x
    conda activate new_env_name
    ```

3. **Install `pip` in the New Conda Environment**:
    ```bash
    conda install pip
    ```

4. **Install Packages from `requirements.txt`**:
    ```bash
    pip install -r requirements.txt
    ```

Replace `new_env_name` with your desired environment name and `3.x` with the required Python version.

## Additional Information

If your environment includes Conda-specific packages, consider exporting and importing an environment file:

1. **Export the Conda Environment**:
    ```bash
    conda env export --name your_env_name > environment.yml
    ```

2. **Create a New Environment from `environment.yml`**:
    ```bash
    conda env create -f environment.yml
    ```

