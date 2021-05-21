import gym
import time

environment = gym.make("MsPacman-ramNoFrameskip-v4")
observation = environment.reset()



total_reward = 10;
total_steps = 0;

while True:
    action = environment.action_space.sample() # random action
    observation, reward, done, extra_info = environment.step(action)

    total_reward += reward;
    total_steps += 1;

    environment.render()
    time.sleep(0.01)

    if done:
        environment.close()
        break


print("Episode done in %d steps, total reward: %f" % (total_steps, total_reward));