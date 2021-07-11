# Starting kit Content

In this starting kit you will find:
- 7 notebooks for you to learn about the Grid2op framework, and competition setup, submission process and evaluation.
- L2RPN related papers that can also help you get started, grab a good understanding of the problem and learn about possible solutions.
- [Optional when getting started] Requirements that you would need to install if you want to reproduce a python environment like the docker image. See https://github.com/rte-france/Grid2Op/issues/233 for up-to-date instructions. 

# Notebooks
To run the notebooks, you only need to install Grid2op (pip install grid2op). Here are the different notebooks you will find:

- 0_Basic_Competition_Information: It describes the competition set-up, the different phases and rules.
 

- 1_Power_Grid_101_notebook: It explains the problem of power grid operations on a small grid using the grid2op platform.
 
- 2_L2RPN_ICAPS_Alarm_feature_Notebook: It explains the alarm feature your agent can use to alert at the right time an operator when your agent is in trouble. That's the main innovation of this competition.

- 3_L2RPN_ICAPS_Opponent: It explains you in more details the role of the opponent, similarly to L2RPN 2020 NeuriPS Robustness Track.
 
- 4_Score_Agent: It explains the overall score composed of attention score and grid operation score cost based on which you will be ranked during the competition. Finally you will be able to create a simple agent in this notebook.
 
- 5_SubmitToCodalab: It details the submission process on codalab. In this competition you are required to submit code. This notebook details how to do that using the codalab interface.
 
- 6_DebugYourSubmission: You will be asked to submit code that will be evaluated on private environments on Codalab. This means that the code that runs perfectly fine on your machine will be run on distant machine in the cloud. The process of providing such reproducible code can be counter intuitive and we explain in this last notebook how to fix the most common issues participants encounter in previous competitions.
 
- 7_L2RPN_ICAPS_Baseline_Notebook: It shows you two learning agent examples, one taken from L2RPN-Baseline repository and the other one as an RL-Lib standard agent (you will need to install those dependencies here).

# Papers
You will find 3 categories of papers: Introductory papers, Competition and result descpription papers, Baseline and winning agent descritpion papers.
Here is the full list of papers you will find here:

- [1]  A. Kelly, A. O’Sullivan, P. de Mars, and A. Marot.  Reinforcement learning  for  electricity  network  operation.arXiv preprint arXiv:2003.07339,2020.
- [2]  B.  Donnot,  I.  Guyon,  M.  Schoenauer,  P.  Panciatici,  and  A.  Marot.Introducing machine learning for power system operation support.arXivpreprint arXiv:1709.09527, 2017.
- [3]  A.   Marot,   B.   Donnot,   G.   Dulac-Arnold,   A.   Kelly,   A.   O’Sullivan,J. Viebahn, M. Awad, I. Guyon, P. Panciatici, and C. Romero.  Learning to run a power network challenge: a retrospective analysis.arXiv preprintarXiv:2103.03104, 2021.
- [4]  A. Marot, B. Donnot, C. Romero, B. Donon, M. Lerousseau, L. Veyrin-Forrer,  and  I.  Guyon.Learning  to  run  a  power  network  challenge for  training  topology  controllers.Electric Power Systems Research,189:106635, 2020.
- [5]  A.  Marot,  B.  Donnot,  S.  Tazi,  and  P.  Panciatici.Expert  system  for topological remedial action discovery in smart grids.  2018.
- [6] T.  Lan,  J.  Duan,  B.  Zhang,  D.  Shi,  Z.  Wang,  R.  Diao,  and  X.  Zhang.Ai-based  autonomous  line  flow  control  via  topology  adjustment  for maximizing  time-series  atcs.   In2020 IEEE Power & Energy SocietyGeneral Meeting (PESGM), pages 1–5. IEEE, 2020
- [7]  D.  Yoon,  S.  Hong,  B.-J.  Lee,  and  K.-E.  Kim.Winning  the  l2rpn challenge:  Power  grid  management  via  semi-markov  after state  actor-critic.  InInternational Conference on Learning Representations, 2020.
- [8]  A.  Marot,  A.  Rozier,  M.  Dussartre,  L.  Crochepierre,  and  B.  Donnot. Towards  an  ai  assistant  for  human  grid  operators.arXiv preprintarXiv:2012.02026, 2020.
- [9]  A. Marot, I. Guyon, B. Donnot, G. Dulac-Arnold, P. Panciatici, M. Awad,A.  O’Sullivan,  A.  Kelly,  and  Z.  Hampel-Arias.  L2rpn:  Learning  to  run a  power  network  in  a  sustainable  world  neurips 2020  challenge  design.2020
- [10]  L.  Omnes,  A.  Marot,  and  B.  Donnot. Adversarial  training  for  continuous  robustness  control  problem  in  power  systems.arXiv preprintarXiv:2012.11390, 2020

# Install
As previously mentioned, you mostly only need to install grid2op to get started.

Once you will get more advance and will be training an agent you develop or ready to submit it, it is highly recommended that you use the same environment as the docker image used on codalab to evaluate your submissions.
For that you will find a requirements.txt here with the used versions of the different packages.
Because of some specific packages you need to follow some more steps than one simple pip install. All details described here:  https://github.com/rte-france/Grid2Op/issues/233 .