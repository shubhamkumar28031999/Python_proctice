if __name__=="__main__":
    n=int(input())
    team_final_score=dict()
    for _ in range(n):
        team1,team2,score=map(str,input().strip().split())
        score_team1,score_team2=map(int,score.strip().split('-'))
        if score_team1>score_team2:
            if team1 in team_final_score:
                team_final_score[team1]+=3
            else:
                team_final_score[team1]=3
        if score_team1<score_team2:
            if team2 in team_final_score:
                team_final_score[team2]+=3
            else:
                team_final_score[team2]=3
        if score_team1==score_team2:
            if team1 not in team_final_score:
                team_final_score[team1]=0
            if team2 not in team_final_score:
                team_final_score[team2]=0
            team_final_score[team1] += 1
            team_final_score[team2] += 1
    
