# -*- coding: utf-8 -*-
"""
Simple RL glue experiment setup
"""

import rlglue.RLGlue as RLGlue

def runEpisode(is_learning_episode):

    RLGlue.RL_episode(0)
    totalSteps = RLGlue.RL_num_steps()
    totalReward = RLGlue.RL_return()

    print "Evaluation ::\t " + str(totalSteps) + " steps \t" + str(totalReward) + " total reward\t "


# Main Program starts here
print "\n\nDQN-ALE Experiment starting up!"
RLGlue.RL_init()

print "Freeze learning for Evaluation"
RLGlue.RL_agent_message("freeze learning")
RLGlue.RL_agent_message("load model")
runEpisode(is_learning_episode=False)

RLGlue.RL_cleanup()
