
import gym
from stable_baselines3 import PPO
import os

models_dir = "models/PPO"
logs_dir = "logs"

if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)




env = gym.make("LunarLander-v2")
'''env = gym.make("LunarLander-v2", render_mode='human')'''
env.reset()


model = PPO("MlpPolicy", env, verbose=1, tensorboard_log=logs_dir)



TIMESTEP = 100000

for i in range(1,100):
    model.learn(TIMESTEP,reset_num_timesteps=False,tb_log_name="PPO")
    model.save(f"{models_dir}/{TIMESTEP*i}")
    

'''
episodes = 10

for ep in range(episodes):

    obs = env.reset()
    done = False

    while not done:
        env.render()
        obs, reward, done, info = env.step(env.action_space.sample())
'''

env.close()


