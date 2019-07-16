# --------------
import json
from collections import Counter
with open(path) as f:
    data = json.load(f)

print(type(data)) 
 
# Code starts here
class PlayerStat:
    def __init__(self,batter,data):
        self.batter = batter
        self.data = data
    
        
    def ball_faced(self):
        for key,val in data.items():
            if key == 'innings':
                first_innings = val[0]['1st innings']['deliveries']
                balls_faced=0
                for i in range(len(first_innings)):
                    del_stat=first_innings[i]
                    #print(type(del_stat))
                    for key1,val1 in del_stat.items():
                        if val1['batsman'] == self.batter:
                            balls_faced+=1
                return(balls_faced)
                
    def runs_scored(self):
        for key,val in data.items():
            if key == 'innings':
                first_innings = val[0]['1st innings']['deliveries']
                run_scored=0
                for i in range(len(first_innings)):
                    del_stat=first_innings[i]
                    #print(type(del_stat))
                    for key1,val1 in del_stat.items():
                        if val1['batsman'] == self.batter:
                            runs_stat=val1['runs']
                            runs_val=runs_stat['batsman']
                            run_scored+=runs_val
                            
                return(run_scored)
#  Can you find how many deliveries were faced by batsman  `SC Ganguly`.
player_stat=PlayerStat('SC Ganguly',data)
print("Balls faced by batsmen SC Ganguly are {}".format(player_stat.ball_faced()))             

#  Who was man of the match and how many runs did he scored ?
MoM=data['info']['player_of_match'][0]
#print(type(MoM))
print("Man of the match:{}".format(MoM))

player_MoM=PlayerStat(MoM,data)
print("Runs scored by Man of the match {0} are {1}".format(MoM,player_MoM.runs_scored())) 

#  Which batsman played in the first inning?
batsman_list=[]
for key,val in data.items():
    if key == 'innings':
        first_innings = val[0]['1st innings']['deliveries']
        for i in range(len(first_innings)):
            del_stat=first_innings[i]
            for key1,val1 in del_stat.items():
                if (val1['batsman'] not in batsman_list):
                    batsman_list.append(val1['batsman'])
                elif (val1['non_striker'] not in batsman_list):
                    batsman_list.append(val1['non_striker'])
                          
print("Batsmen played in 1st innings are:{}".format(batsman_list))

# Which batsman had the most no. of sixes in first inning ?
batsman_six_count=[]
for i in range(len(batsman_list)):
    batsman_six_count.append(0)
#print(batsman_six_count)
for key,val in data.items():
    if key == 'innings':
        first_innings = val[0]['1st innings']['deliveries']
        for i in range(len(first_innings)):
            del_stat=first_innings[i]
            for key1,val1 in del_stat.items():
                for i in range(0,len(batsman_list)):
                    if (val1['batsman']==batsman_list[i]) and (val1['runs']['batsman'] == 6):
                        batsman_six_count[i]=(batsman_six_count[i])+1
                        #batsman_sixes.update({batsman_list[i]=)
                
                
#print(batsman_six_count)   
             
batsman_sixes={}
for i in range(len(batsman_list)):
    batsman_sixes.update({batsman_list[i]:batsman_six_count[i]})
max_sixes=max(batsman_six_count)

#print(batsman_sixes)                          

for player,sixes in batsman_sixes.items():
    if sixes==max_sixes:
        print("Batsman hitted the most no. of sixes in first inning is {}".format(player))



# Find the names of all players that got bowled out in the second innings.
wicket_bowled=[]
for key,val in data.items():
    if key == 'innings':
        second_innings = val[1]['2nd innings']['deliveries']
        for i in range(0,len(second_innings)):
            del_stat=second_innings[i]
            for key1,val1 in del_stat.items():
                wicket_data=val1
                for key2,val2 in wicket_data.items():
                    if key2=='wicket':
                        if val2['kind']=='bowled':
                            wicket_bowled.append(val2['player_out'])
                        
print("Bowlers got out as bowled in 2nd innings: {}".format(wicket_bowled))  


# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?
wides=0 
legbyes=0             
for key,val in data.items():
    if key == 'innings':
        second_innings = val[1]['2nd innings']['deliveries']
        for i in range(0,len(second_innings)):
            del_stat=second_innings[i]
            for key1,val1 in del_stat.items():
                extras_data=val1
                for key2,val2 in extras_data.items():
                    if key2=='extras':
                        extras_stat=val1['extras']
                        for key3,val3 in extras_stat.items():
                            if key3=='wides':
                                wides_val=extras_stat['wides']
                                wides+=wides_val
                            elif key3=='legbyes':
                                legbyes_val=int(extras_stat['legbyes'])
                                legbyes+=legbyes_val

#print(wides,legbyes)
extras_count=wides+legbyes
print("Total extras in 2nd nnings : {}".format(extras_count)+"("+"wides-{0} and legbyes-{1}".format(wides,legbyes)+")")


# Code ends here


