# L2RPN

Second place solution for Learning to Run a Power Network - ICAPS 2021 Competition

[Competition link](https://competitions.codalab.org/competitions/33121)

### Files

- **final_submission**: Files submitted to the competition
- **src**: Source code for reproducing the submission

### Approach

For the operational portion of the competition I simply took the top 208 actions of the 2020's edition second place finisher [1]. When we are close to an overflow, we simulate each one of these actions and select the one that results in the lowest maximum rho.

For selecting when to trigger the alarm, I ran several episodes using this strategy and stored them. Then, I used this data to train a neural network to predict the probability of a certain state being close to a blackout. In run-time we use this probability to decide whether or not to trigger the alarm in the current timestep.

Due to time constrains I ended up hardcoding a probability threshold and combining it with a simple heuristic to trigger the alarm. Ideally, this threshold should depend on the current state and should be learned by evaluating the alarm in training data (different from the one used for training the model).

For the final submission, I ran 10k episodes and trained the model for ~2 hours in a p3.2xlarge instance.

[1] https://github.com/AsprinChina/L2RPN_NIPS_2020_a_PPO_Solution

### Running

The following packages are required:
```
Grid2Op==1.6.3
LightSim2Grid==0.5.4
tensorflow==2.5.0
numpy==1.18.4
```

First, split train and validation data (if you haven't already):
```bash
python3 split_train_val_data.py 
```

Run 10 episodes and store them:
```bash
python3 store_episode_data.py Train 10 1 0 0
```

Preprocess the stored data:
```bash
python3 preprocess_data.py Train -1 Raw
```

Train a model to predict the likelihood of being close to a game over:
```bash
python3 nn.py model_4 Train Raw 10 64
```

Evaluate our agent in 10 different scenarios
```bash
python3 main.py 10
```

### License ###

This content is released under the (http://opensource.org/licenses/MIT) MIT License.
