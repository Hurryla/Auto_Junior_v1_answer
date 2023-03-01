def round_up(num, divisor):
    if num%divisor == 0:
        r = num
    if num%divisor != 0:
        r = num + 5- (num%divisor)
    return r

thisdict = {'德瑞克': 33,
            '尚恩': 73,
            '傑夫': 63,
            '馬基': 39
                  }

for name, old_score in thisdict.items():
    new_score = round_up(old_score, 5)
    if new_score >=40 and new_score - old_score <= 3:
        final_score = new_score
    else:
        final_score = old_score
    print(name, final_score)


H = 100
cnt =0
sum_=100
while cnt<=10:
    
    H =H *0.5
    cnt= cnt + 1
    sum_ = sum_ + H*2
    if cnt==9:
        print(f"第{str(cnt+1)}次落第時，共經歷{str(sum_)}公分")
    if cnt==10:
        print(f"第{str(cnt)}次反彈高度為{str(H)}公分")
