rl_glue&
python dqn_agent_nature.py &
python test.py &
../ale_0.4.4/ale_0_4/ale -game_controller rlglue -use_starting_actions true -random_seed time -display_screen true -frame_skip 4 ./pong.bin
