

import requests

def order_dict(d:dict, sd: dict):
    
    sorted_d = sorted(d.items(), key= lambda x:x[1], reverse=True)
    sorted_sd = sorted(sd.items(), key=lambda x:x[1], reverse=True)
    return [sorted_d, sorted_sd]

szamok = {str(n):52000.0 for n in range(1, 51)}
kis_szamok = {str(n):52000.0 for n in range(1, 13)}

otos_url = "https://bet.szerencsejatek.hu/cmsfiles/eurojackpot.csv"

current_file = requests.get(otos_url)

rawdata: str = current_file.content.decode()
all_weeks = rawdata.split("\r\n")[1:]
for weeks_ago, week in enumerate(all_weeks, start=1):

    nums = week.split(";")[28:35]
    # print(nums)
    if nums == []:
        continue
    #nums = [int(numstring) for numstring in string_nums]
    

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


    if kis_szamok[nums[5]] > weeks_ago:
        kis_szamok[nums[5]] = float(weeks_ago)
    if kis_szamok[nums[6]] > weeks_ago:
        kis_szamok[nums[6]] = float(weeks_ago)

        # print(nums)

def calc_odds(nums_list):
    odd = 1

    for (num, weeks_ago) in nums_list:
        odd *= (1 - ((1- (1/50)) ** weeks_ago))

    return odd
    
def calc_small_ods(nums_list):
    odd = 1
    for (num, weeks_ago) in nums_list:
        odd *= (1 - ((1- (1/12)) ** weeks_ago))

    return odd

rendezett, kis_rendezett = order_dict(szamok, kis_szamok)
print(rendezett)
print(kis_rendezett)
print("top 5 nagy esélyes az ötös találatra:")
for i in range(0, 25, 5):
    print([rendezett[i][0] for i in range(i, i+5)])
    print(f"{calc_odds(rendezett[i:i+5])}%")
print("top 5 kis esélyes az ötös találatra:")
for i in range(0, 10, 2):
    print([kis_rendezett[i][0] for i in range(i, i+2)])
    print(f"{calc_odds(kis_rendezett[i:i+2])}%")