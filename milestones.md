# Daddy Long Legs
## Milestone 1
I am choosing the Daddy Long Legs project. First I will add a vector to Solution's constructor that will randomly choose the length of the 4 lower legs. Additionally I will modify solution's Generate_Body to use these values as the lengths of each leg. I will demonstrate this with a video of search.py with one generation and population: 1, to show that the legs are different lengths. In addition, I will print the length of the legs to the terminal.

## Milestone 2
I will change Solution's Mutate function to evolve the size of the legs along with the synaptic weights. Additionally, I will modify the fitness function to include a penalty for robots that fall down, so the robot learns how to walk. I will demonstrate this with a video of search.py and showing the best result.


I modified the fitness function in 2 ways:
1. Included a penalty that punished the robot's torso hitting the ground. If the torso's touch sensor went off at any moment, then the penalty will be given. The goal here is to prevent the robot from doing a large forward lunge at the beginning of the simulation and then flipping over.

2. Included a penalty for high angles for roll and pitch (rotations along the x and y axis respectively). If the angle reached a certain threshold a penalty will be enforced. I included this penalty because in many runs of search.py, the robot that traveled the furthest would lean forward or backward, drag one leg completely on the ground, and use the other legs to push. I wanted the robot to learn how to walk on its legs, thus this penalty was included.



## Milestone 3
In a Separate branch, I will perform the steps same as in milestone 1, but this time I will modify the upper legs instead of the lower legs. I will demonstrate this with a video of search.py with one generation and population: 1, running with different length upper and lower legs, with the upper and lower leg lengths printed to the console.


## Milestone 4 (A/B Testing)
I will change Solution's mutate function to evolve the size of the upper leg along with the synaptic weights. I know have two different robots to compare in A/B Testing. I will demonstrate this with a video of search.py with both the upper and lower legs evolving and showing the best result.

I Modified the fitness function in two ways:

2. punished the robot for "dragging" one of it's lower legs on the ground, and pushing forward with it's other legs. I want the robot to balance on it's 4 legs and walk. The punishment for angulation was not working as well becuase the longer upper legs would result in a less angled robot so it wouldn't exceed the threshold required to add the penalty.

1. Removed the penalty for high angulation of the robot, since it was not working with the robot I was trying to evolve.






