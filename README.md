I’m trying to design a ranking algorithm for volunteers on a type of question and answer site. The algorithm will be structured as follows:

- When a question comes in from a questioner, a random selection of the available volunteers will be asked to answer it.  Each volunteer has a score determined by the results of their previous participation. The number of volunteers will be at least 2, and up to “max_answerers_per_round”.

-Of the volunteers that answer, only the 2 with the highest scores will have their answers displayed to the questioner.   This system, however, favors those that have been volunteering longer (and thus have had time to accumulate a higher score).  To counteract this, there is always a chance that a volunteer’s score will receive a “bump” during evaluation.  The odds of this bump percentage or “bump_perc”, are determined by a “bump_chance”.

-When the questioner is presented with the two highest scoring answers, they will choose one.  The one that is chosen will have its providing volunteer’s score incremented by “increment_for_win”.  The one that is not chosen will have  its providing volunteer’s score decremented by “decrement_for_loss”.

The goal is to create functions for bump_perc, bump_chance, increment_for_win, and  decrement_for_loss  such that the score of each volunteer reflects their skill in answering questions as fast as possible.  In addition, when new volunteers join, we would like their score to quickly move to reflect their skill level, and we would like to make sure they are still afforded the chance to answer questions (rather than being crowded out by existing volunteers with high scores).

In order to test this algorithm, I’ve created a Monte Carlo simulation.  The simulated volunteers are given a randomly assigned “skill” level.  They are also given a starting “rank” which represents their score.  As the simulation progresses,  new volunteers join.  The goal is for their “rank” order to match their “skill” order as quickly as possible.

 In order to assess the fitness of the algorithm,  I am generating a score after each question is answered.  This score is a measure of the difference between the ranking order and the skill order.  The goal is to minimize the sum of these scores. 
