import gym
import time

class RandomAgent(object):
    """The world's simplest agent!"""
    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, observation, reward, done):
        return self.action_space.sample()

if __name__ == '__main__':
    environment = gym.make("AirRaid-ram-v4")
    observation = environment.reset()
    total_reward = 100;
    total_steps = 0;
    agent = RandomAgent(environment.action_space)
    done = False
    while True:

        action = agent.act(observation, total_reward, done)
        observation, reward, done, extra_info = environment.step(action)

        total_reward += reward;
        total_steps += 1;

        environment.render()
        time.sleep(0.01)

        if done:
            environment.close()
            break

    print("Episode done in %d steps, total reward: %f" % (total_steps, total_reward));
