# Example of valid submissions

In this directory we put some example of valid submissions.
By valid submission we mean "if you zip them with the 
*[check_your_submission.py](../check_your_submission.py)* 
script and submit the resulting \*.zip file into codalab 
(see notebook [5_SubmitToCodalab](../5_SubmitToCodalab.ipynb) for more 
information) then the resulting submission will be accepted by codalab.

These repository is not meant to show "efficient" submissions but rather 
to illustrate how a submission file might be structured to be
valid.

For baselines, you can have a look at the [l2rpn-baselines](https://github.com/rte-france/l2rpn-baselines) repository.

This directory contains a few examples:

- [submission](./submission) propose the most basic submission package
- [submission_random](./submission_random) shows the import of an existing agent, namely RandomAgent, that can be directly used
- [submission_withreward](./submission_withotherreward) explains how to modify the reward that your agent
  will use on codalab during its scoring.
- [submission_withotherreward](./submission_withotherreward) shows how to use properly the "other_rewards"
  capability of grid2op (see 
  [training-with-multiple-rewards](https://grid2op.readthedocs.io/en/latest/reward.html#training-with-multiple-rewards)
  for more information about this feature)
- [submission_withdataloading](./submission_withdataloading) exhibits how to reload some data in your submision.
  Keep in mind that your code will be run in the cloud to get your score. We strongly recommend you
  to have a look here to know how you can tell your agent to restore some weights or load some 
  external data you might seem fit.
- [submission_withbaselines](./submission_withbaselines) indicates how you can submit a trained baselines
  coming from the [l2rpn-baselines](https://github.com/rte-france/l2rpn-baselines) python package.
  
In case of trouble with your submission, the *[check_your_submission.py](../check_your_submission.py)* 
file will give you information on what can be wrong. YOu can also have a look at the 
[6_DebugYourSubmission](../6_DebugYourSubmission.ipynb) notebooks for more information.

