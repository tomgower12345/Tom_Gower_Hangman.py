from random import choice

words=['rarely', 'universe', 'notice', 'sugar', 'interference', 'constitution', 'we', 'minus', 'breath', 'clarify', 'take', 'recording', 'amendment', 'hut', 'tip', 'logical', 'cast', 'title', 'brief', 'none', 'relative', 'recently', 'detail', 'port', 'such', 'complex', 'bath', 'soul', 'holder', 'pleasant', 'buy', 'federal', 'lay', 'currently', 'saint', 'for', 'simple', 'deliberately', 'means', 'peace', 'prove', 'sexual', 'chief', 'department', 'bear', 'injection', 'off', 'son', 'reflect', 'fast', 'ago', 'education', 'prison', 'birthday', 'variation', 'exactly', 'expect', 'engine', 'difficulty', 'apply', 'hero', 'contemporary', 'that', 'surprised', 'fear', 'convert', 'daily', 'yours', 'pace', 'shot', 'income', 'democracy', 'albeit', 'genuinely', 'commit', 'caution', 'try', 'membership', 'elderly', 'enjoy', 'pet', 'detective', 'powerful', 'argue', 'escape', 'timetable', 'proceeding', 'sector', 'cattle', 'dissolve', 'suddenly', 'teach', 'spring', 'negotiation', 'solid', 'seek', 'enough', 'surface', 'small', 'search']
mystery_word= choice(words)
if '\n' in mystery_word:
    mystery_word=mystery_word[:-1]
print(f'Word has {len(mystery_word)} letters')
lives=7
st=[]
for j in mystery_word:
    st.append('-')
temp_st_0=''
for d in st:
    temp_st_0+=d
print(f'Word to be tested:{temp_st_0};You have {lives} lives left')
o=0
xc=1
stat=''
log_l=[]
lv=[]
while lives>0:
    if o==0:
        ch=str(input('Please enter your next guess : '))
        if ch in mystery_word:
            for y in range(len(mystery_word)):
                if mystery_word[y]==ch:
                    st[y]=mystery_word[y]
                    lv.append(lives)
                    o+=1
                    xc=1
                else:
                    o+=1
        else:
            lives-=1
            print(f'The letter {ch} is not in the mystery word;you got {lives} lives left')
            xc=0
            o+=1
    else:
        temp_st=''
        for g in st:
            temp_st+=g
        
        print(f'Word to search for:{temp_st};you got {lives} lives left')
        ch=str(input('Please enter your next guess : '))
        if ch in mystery_word:
            for y in range(len(mystery_word)):
                if mystery_word[y]==ch:
                    st[y]=mystery_word[y]
                    xc=1

            if '-' not in st:
                stat='congratulations you win'
                print(stat)
                break
        else:
            lives-=1
            print(f'The letter {ch} is not in the mystery word;you got {lives} lives left')
            xc=0
else:
    if lives==0:
        print('you lose')
