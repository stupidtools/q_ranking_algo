This is the python script for the monte carlo simulation.  

This simulation assumes that a volunteer with a higher skill level will always beat one with a lower skill level.

Everything in the settings block at the beginning can be modified, including the functions that determine  how a volunteers score should be incremented/decremented.


volunteer_dictionary = {
	skill: <randomly determined skill rank.  This is a static value between 0 & 1>
	rank: <current rank score for this volunteer. >
	key: <id for this volunteer>,
	entrance_time: <the round during which the volunteer entered (0 means they were there from the beginning)>
	
}

dict(skill = random.random() * 10, rank = settings['start_rank'], key=i)

Explanation of the settings:



'vol_count':  the number of volunteers that will ultimately be participating

'start_rank': the starting rank of each volunteer

'iterations': number of “questions answered” during the monte carlo simulations (how many loops)

'bump_chance':  a function determining the chance that a volunteer will get a “bump” to it’s score during this evaluation.  Takes the volunteer dictionary as an argument 

'bump_perc': a function that determines the percentage by which a volunteers score should be bumped during this evaluation if it qualifies based on the bump chance.  Takes the volunteer dictionary as an argument 

'increment_for_win':  A function that should return the new score for a volunteer after it wins a question eval by the questioner.  Takes the volunteer dictionary as an argument

'decrement_for_loss': A function that should return the new score for a volunteer after it looses a
 question eval by the questioner.  Takes the volunteer dictionary as an argument

'max_answerers_per_round': The maximum number of volunteers that can answer a question each round.  Between 2 and this many will be randomly selected from the volunteer pool.  Must be at least 2.

'starting_pool': the number of volunteers in the pool at the beginning

'odds_of_new_entry_per_cycle':.  The odds of a new volunteer joining each cycle
'run_c': Calls a c function to implement an insertion sort algorithm.  This is used to measure the difference between the volunteers sorted by “rank” and sorted by “skill”.  It can be run without the c function by changing the run_c setting, but running it in pure python is quite slow.
