
import requests

def order_dict(d:dict):
    
    sorted_d = sorted(d.items(), key= lambda x:x[1], reverse=True)
    return sorted_d

szamok = {str(n):52000.0 for n in range(1, 91)}

otos_url = "https://bet.szerencsejatek.hu/cmsfiles/otos.csv"

current_file = requests.get(otos_url)

rawdata: str = current_file.content.decode()
all_weeks = rawdata.split("\r\n")
for weeks_ago, week in enumerate(all_weeks, start=1):

    nums = week.split(";")[11:16] #11:16
    # print(nums)
    if nums == []:
        continue
    # nums = [int(numstring) for numstring in string_nums]
    if szamok[nums[0]] > weeks_ago:
        szamok[nums[0]] = float(weeks_ago)
    if szamok[nums[1]] > weeks_ago:
        szamok[nums[1]] = float(weeks_ago)
    if szamok[nums[2]] > weeks_ago:
        szamok[nums[2]] = float(weeks_ago)
    if szamok[nums[3]] > weeks_ago:
        szamok[nums[3]] = float(weeks_ago)
    if szamok[nums[4]] > weeks_ago:
        szamok[nums[4]] = float(weeks_ago)
    

        # print(nums)

def calc_odds(nums_list):
    odd = 1

    for (num, weeks_ago) in nums_list:
        odd *= (1 - ((1- (1/90)) ** weeks_ago))

    return odd
    
    

rendezett = order_dict(szamok)
print("top 5 esélyes az ötös találatra:")
for i in range(0, 25, 5):
    print([rendezett[i][0] for i in range(i, i+5)])
    print(f"{calc_odds(rendezett[i:i+5])*100}%")