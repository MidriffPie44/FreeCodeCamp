
# The idea here is to modify Abbey's code in order to solve this challenge.
# This is because when you pit the bots against each other, Abbey has the highest win rate with some instances above 60%.
# Abbey only looks at the past two moves, hence we will look at the past 5 moves (This was based on testing I've done pitting the bots against each other)

def player(prev_play, opponent_history=[], play_order={}):
    if not prev_play:
        prev_play = 'R'
        
    opponent_history.append(prev_play)
    prediction = 'S'

    ideal_response = {'P':'S', 'S':'R', 'R':'P'}

    guess = "R"
    if len(opponent_history) > 2:
        guess = opponent_history[-2]

    if len(opponent_history) > 4:
        last_five = ''.join(opponent_history[-5:])
        play_order[last_five] = play_order.get(last_five, 0) + 1

    potential_plays = [
            "".join([*opponent_history[-4:], v]) 
            for v in ['R', 'P', 'S']
        ]

    sub_order = {
        k: play_order[k]
        for k in potential_plays if k in play_order
    }

    if sub_order:
        prediction = max(sub_order, key=sub_order.get)[-1:]

    return ideal_response[prediction]
