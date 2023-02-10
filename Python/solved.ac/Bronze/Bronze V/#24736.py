Th, Fh, Sh, Ph, Ch = map(int, input().split())
Ta, Fa, Sa, Pa, Ca = map(int, input().split())

homeTotal = Th*6 + Fh*3 + Sh*2 + Ph*1 + Ch*2
awayTotal = Ta*6 + Fa*3 + Sa*2 + Pa*1 + Ca*2

print(homeTotal, awayTotal)