from l2rpn_baselines.DuelQSimple import DuelQSimple, DuelQ_NNParam, DuelQ_NN

"""
This file explains a simple script that you can use to reload a trained baseline.

This supposes that you have a trained baselines, and that you save it in the "saved_baseline" repository and that you
named it "my_saved_baseline"

It works with the following baselines:
- DeepQSimple
- DuelQSimple
- DuelQLeapNet
- SAC

Contact the authors of the other baselines in the l2rpn_baselines repository if you want to use them here.

We show here only to reload a "DuelQSimple". There are no particular difficulties to change the import in case you 
would want to use a different one (among the 4 listed above).

Again, you cn contact the authors of the other baselines in the l2rpn_baselines repository if you want to use them here.
"""

name = "my_saved_baseline" 
from Toto import tata

def make_agent(env, submission_dir):
    """
    This function will be used by codalab to create your agent. It should accept exactly an environment and a path
    to your sudmission directory and return a valid agent.
    """
    path_model, path_target_model = DuelQ_NN.get_path_model(load_path, name)
    nn_archi = DuelQ_NNParam.from_json(os.path.join(path_model, "nn_architecture.json"))
    res = DuelQSimple(env.action_space,
                      name=name,
                      nn_archi=nn_archi,
                      observation_space=env.observation_space
                     )
    res.load(load_path)
    return res
