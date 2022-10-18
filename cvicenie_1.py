def riadok(n, text=''):
    if text != '':
        text = ' ' + text+ ' '
    a = (n-len(text))//2
    b = n-len(text)-a
    print('*'* a + text +'*'* b)

sir = 40
riadok(sir)
riadok(sir, 'Ján Botto')
riadok(sir, 'Žltá ľalija')
riadok(sir, '-')
riadok(sir, 'Stojí stojí mohyla')
riadok(sir, 'Na mohyle zlá chvíľa')
riadok(sir, 'na mohyle tŕnie chrastie')
riadok(sir, 'a v tom tŕní chrastí rastie')
riadok(sir)