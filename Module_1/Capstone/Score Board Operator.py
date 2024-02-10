'''wins: 3 points
draws: 1 point
losses: 0 points
Team London has played 8 matches in this tournament. They won 4 matches, lost 3 matches and drew 1. The operator is in need of assistance to calculate the total number of points earned by Team London. As a python expert adept with knowledge of integer, floats and boolean, you can help the operator by writing a solution for the following problem.'''

matches_won_TeamLondon = 4
matches_lost_TeamLondon = 3
matches_draw_TeamLondon = 1
win_score = 3
draw_score = 1
loss_score = 0
total_score = (matches_won_TeamLondon*win_score)+(matches_lost_TeamLondon*loss_score)+(matches_draw_TeamLondon*draw_score)
print("Total score of team london is " + str(total_score))