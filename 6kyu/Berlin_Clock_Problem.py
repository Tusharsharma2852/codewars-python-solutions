#Requirement = The clock is read from the top row to the bottom:
# the round Yellow light on top blinks to denote even- (when on) or odd-numbered (off) seconds,
# the first row of four Red fields denote five full hours each,
# the second row, also of four Red fields, which denote one full hour each (displaying the hour value in 24-hour format)
# the third row consists of eleven Yellow-and-Red fields, which denote five full minutes each (the red ones also denoting 15, 30 and 45 minutes past),
# the bottom row has another four Yellow fields, which mark one full minute each.
# Example : "12:56:01"  ==>  "O\nRROO\nRROO\nYYRYYRYYRYY\nYOOO"
# RROO
# RROO
# YYRYYRYYRYY
# YOOO
# "00:00:00"  ==>  "Y\nOOOO\nOOOO\nOOOOOOOOOOO\nOOOO"
# "22:32:45"  ==>  "O\nRRRR\nRROO\nYYRYYROOOOO\nYYOO"
#Link : https://www.codewars.com/kata/5a1463678ba9145a670000f9/train/python
def berlin_clock(time):
    parts = time.split(":")
    hour = int(parts[0])
    min = int(parts[1])
    sec = int(parts[2])
    if sec%2 ==0:
        row1 = "Y"
    else:
        row1= "O"
    n = hour // 5
    count = ""
    for i in range(n):
        count += "R"
    for i in range(4-n):
        count += "O"
    m = hour % 5
    count1 =""
    for i in range(m):
        count1 += "R"
    for i in range(4-m):
        count1 += "O"
    a = min // 5
    result = ""
    for i in range(1,12):
        if i<= a:
            if i % 3== 0:
                result += "R"
            else:
                result += "Y"
        else:
            result += "O"
    b = min % 5
    row5 = ""
    for i in range(b):
        row5 += "Y"
    for i in range(b,4):
        row5 += "O"
    return row1 + "\n" + count +"\n"+ count1 +"\n"+ result +"\n"+ row5

        
    

    
