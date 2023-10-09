
import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env


env = make_vec_env("LunarLander-v2", seed=1, n_envs=1)
env.reset()

models_dir="models/PPO"
model_path=f"{models_dir}/13400000.zip"
print(model_path)

model = PPO.load(model_path)

episodes = 10

for ep in range(episodes):

    obs = env.reset()
    done = False
    print(ep)

    while not done:
        action, _states = model.predict(obs)
        obs, reward, done, info = env.step(action)
        env.render('human')
    
env.close()


