from gym import Env
from gym.spaces import Discrete, Box
import numpy as np
import random
import tensorflow as tf

from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

print('Using Tensorflow version: ', tf.version.VERSION)

def isThereGPU():
    print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
    print("Num CPUs Available: ", len(tf.config.list_physical_devices('CPU')))

isThereGPU()


class ShowerEnv(Env):
    def __init__(self):
        # Actions we can take, down, stay, up
        self.action_space = Discrete(3)
        # Temperature array
        self.observation_space = Box(low=np.array([0]), high=np.array([100]))
        # Set start temp
        self.state = 38 + random.randint(-3,3)
        # Set shower length
        self.shower_length = 60
        
    def step(self, action):
        # Apply action
        # 0 -1 = -1 temperature
        # 1 -1 = 0 
        # 2 -1 = 1 temperature 
        self.state += action -1 
        # Reduce shower length by 1 second
        self.shower_length -= 1 
        
        # Calculate reward
        if self.state >=37 and self.state <=39: 
            reward =1 
        else: 
            reward = -1 
        
        # Check if shower is done
        if self.shower_length <= 0: 
            done = True
        else:
            done = False
        
        # Apply temperature noise
        #self.state += random.randint(-1,1)
        # Set placeholder for info
        info = {}
        
        # Return step information
        return self.state, reward, done, info

    def render(self):
        # Implement viz
        pass
    
    def reset(self):
        # Reset shower temperature
        self.state = 38 + random.randint(-3,3)
        # Reset shower time
        self.shower_length = 60 
        return self.state
    



env = ShowerEnv()


    
env.observation_space.sample()





episodes = 10
for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    score = 0 
    
    while not done:
        #env.render()
        action = env.action_space.sample()
        n_state, reward, done, info = env.step(action)
        score+=reward
    print('Episode:{} Score:{}'.format(episode, score))









states = env.observation_space.shape
actions = env.action_space.n


actions




def build_model(states, actions):

    model = tf.keras.models.Sequential([
      tf.keras.layers.Dense(24, activation='relu', input_shape=states),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(1568, activation='relu'),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(2080, activation='relu'),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(1568, activation='relu'),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(784, activation='relu'),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(actions, activation='softmax')
    ])

    return model





model = build_model(states, actions)

model.summary()




def build_agent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=50000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy, 
                  nb_actions=actions, nb_steps_warmup=10, target_model_update=1e-2)
    return dqn



dqn = build_agent(model, actions)
dqn.compile(tf.keras.optimizers.legacy.Adam(learning_rate =1e-5), metrics=['mae'])
dqn.fit(env, nb_steps=300000, visualize=False, verbose=1)




scores = dqn.test(env, nb_episodes=100, visualize=False)
print(np.mean(scores.history['episode_reward']))




_ = dqn.test(env, nb_episodes=15, visualize=True)




#Save model
dqn.save_weights('dqn_weights.h5f', overwrite=True)

#Load model
dqn.load_weights('dqn_weights.h5f')


_ = dqn.test(env, nb_episodes=5, visualize=True)





