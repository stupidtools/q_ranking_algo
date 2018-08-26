import random
import ctypes


####modifiables


def bump_perc_gen(vol):
    return int(vol['rank'] * 3)
    


def bump_chance_gen(vol):
    return .15

#currently half the distance to 10000
def inc_win_gen(vol):
    return ((10000 - vol['rank']) / 2 ) + vol['rank']

#currently half the distance to 0
def dec_loss_gen(vol):
    return vol['rank'] / 2
    


settings = {
    'vol_count':300,
    'start_rank':5000,
    'iterations':200000,
    'bump_chance':bump_chance_gen,
    'bump_perc': bump_perc_gen,
    'increment_for_win':inc_win_gen,
    'decrement_for_loss':dec_loss_gen,
    'max_answerers_per_round':5,
    'starting_pool':10,
    'odds_of_new_entry_per_cycle':.005,
    'run_c':True

}


########end modifiables


def gen_vols():
    vols = []
    for i in range(settings['vol_count']):
        x = dict(skill = random.random() * 10, rank = settings['start_rank'], key=i)
        vols.append(x)
    return vols



def check_for_new_entry(vols):
    if not vols:
        return False
    x = random.random()
    if x <= settings['odds_of_new_entry_per_cycle']:
        return True
    return False


def get_participants(vols):
    tot = len(vols)
    places = len(str(tot))
    answerers = int(random.random() * 10) % (settings['max_answerers_per_round'] -1) + 2
    output = []
    for i in range(answerers):
        p1 = int(random.random()*10**places) % tot
        output.append(vols[p1])
    return output


def match_participants(parts):
    to_use = []
    for p in parts:
        s = p['rank']
        r = random.random()
        if r <= settings['bump_chance'](p):
            s = settings['bump_perc'](p)
        to_use.append([s, p])
    to_use.sort(key = lambda x: x[0], reverse=True)
    to_use = to_use[:2]
    to_use.sort(key=lambda x: x[1]['skill'], reverse=True)
    to_use[0][1]['rank'] = settings['increment_for_win'](to_use[0][1])
    to_use[1][1]['rank'] = settings['decrement_for_loss'](to_use[1][1])


def gen_score(vols):
    if settings['run_c']:
        py_arr = list(vols)
        py_arr.sort(key = lambda x: x['skill'])
        py_arr = [x['rank'] for x in py_arr]
        arr = (ctypes.c_int * len(py_arr))(*py_arr)
        score_c = ctypes.CDLL('./score_c.so')
        return int(score_c.get_score(arr, ctypes.c_int(len(py_arr))))
    arr = list(vols)
    arr.sort(key = lambda x: x['skill'])
    score = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key['rank'] < arr[j]['rank'] :
                arr[j+1] = arr[j]
                score += 1
                j -= 1
        arr[j+1] = key
    return score



def run_simulation():
    vols = gen_vols()
    active_vols = []
    for i in range(settings['starting_pool']):
        v = vols.pop()
        v['entrance_time'] = 0
        active_vols.append(v)
    score_by_iteration = []
    for i in range(settings['iterations']):
        if check_for_new_entry(vols):
            v = vols.pop()
            v['entrance_time'] = i + 1
            active_vols.append(v)
        match_participants(get_participants(active_vols))
        score_by_iteration.append(gen_score(active_vols))
    return [active_vols, score_by_iteration, sum(score_by_iteration)]







    #the goal is to minimize  x = run_simulation()[2]

    if __name__ = "__main__":
        print(run_simulation()[2])