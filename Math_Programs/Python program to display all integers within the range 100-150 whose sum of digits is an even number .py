for i in range(100,150):
    num = i
    sum = 0
    while(num!=0):
        digit = num%10
        sum = sum + digit
        num = num//10
    if(sum%2==0):
        print(i)
      
Output:
101
103
105
107
109
110
112
114
116
118
121
123
125
127
129
130
132
134
136
138
141
143
145
147
149
