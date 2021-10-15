import grid2op

env = grid2op.make("l2rpn_icaps_2021_large")
nm_env_train, nm_env_val = env.train_val_split_random(pct_val=10.0)
