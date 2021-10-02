import random
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

sports = [
    'cricket', 'bat', 'ball', 'run', 'stumps', 'worldcup', 'tournament', 'wicket',
    'bowler', 'batsmen', 'umpire', 'boundary', 'six', 'four', 'points', 'yorker',
    'bouncer', 'noball', 'wide', 'freehit', 'catch', 'score', 'powerplay', 'over',
    'lbw', 'bowled', 'drive', 'pull', 'sweep', 'hook', 'cut', 'pads', 'gloves',

]
cs = [
    'programming', 'java', 'computer', 'python', 'programe', 'execute',
    'code', 'coding', 'django', 'angular', 'software', 'module', 'class',
    'function', 'deploy', 'templates', 'github', 'parameter', 'object',
    'instance', 'user', 'admin', 'variable', 'keywords', 'arguments', 'html'
]
school = [
    'bag', 'pencil', 'eraser', 'duster', 'books', 'notebook', 'pen', 'ink',
    'slate', 'chalk', 'tiffin', 'bottle', 'divider', 'compass', 'marker',
    'highlighter', 'backpack', 'sharpener', 'calculator', 'scissor',
    'glue', 'ruler', 'punch', 'stapler', 'protractor', 'uniform', 'refill'
]
movies = [
    'baby', 'holiday', 'bahubali', 'race', 'shershah', 'andaz',
    'golmaal', 'dhamaal', 'rustom', 'houseful', 'laxmi', 'andhadhun',
    'ze ro', 'hero', 'sherni', 'sholey', 'krish', 'baghi', 'robot',
    'lagaan', 'guide', 'deewar', 'awaara', 'satya', 'anand', 'ghajini'
]

msg = ""


def rword():
    global jword
    global word
    word = random.choice(sports)
    jum = random.sample(word, len(word))
    jword = "".join(jum)


def rword2():
    global cword
    global soft
    soft = random.choice(cs)
    s = random.sample(soft, len(soft))
    cword = "".join(s)


def rword3():
    global schl
    global sword
    schl = random.choice(school)
    sch = random.sample(schl, len(schl))
    sword = "".join(sch)


def rword4():
    global mword
    global movi
    movi = random.choice(movies)
    m = random.sample(movi, len(movi))
    mword = "".join(m)


def home(request):
    return render(request, 'home.html')


def sport(request):
    global jword, word
    rword()
    return render(request, 'sport.html', {'jword': jword, 'msg': msg})


def cse(request):
    global cword, msg, soft
    rword2()
    return render(request, 'cse.html', {'cword': cword, 'msg': msg})


def schools(request):
    global sword, msg, schl
    rword3()
    return render(request, 'schools.html', {'sword': sword, 'msg': msg})


def movie(request):
    global mword, msg, movi
    rword4()
    return render(request, 'movie.html', {'mword': mword, 'msg': msg})


def checkcr(request):
    global jword
    global word
    global msg
    user_answer = request.POST['ans']
    print(user_answer)
    if user_answer == word:
        msg = "Correct"
        return redirect('sport')
    else:
        msg = "Opps! Wrong try again"
        return render(request, 'sport.html', {'jword': jword, 'msg': msg})


def checkcss(request):
    global cword
    global soft
    global msg
    user_answer = request.POST['ans']
    print(user_answer)
    if user_answer == soft:
        msg = "Correct answer"
        return redirect('cse')
    else:
        msg = "Opps! Wrong answer try again"
        return render(request, 'cse.html', {'cword': cword, 'msg': msg})


def checksc(request):
    global sword
    global schl
    global msg
    user_answer = request.POST['ans']
    print(user_answer)
    if user_answer == schl:
        msg = "Correct"
        return redirect('schools')
    else:
        msg = "Opps! Wrong try again"
        return render(request, 'schools.html', {'sword': sword, 'msg': msg})


def checkmv(request):
    global mword
    global movi
    global msg
    user_answer = request.POST['ans']
    print(user_answer)
    if user_answer == movi:
        msg = "Correct"
        return redirect('movie')
    else:
        msg = "Opps! Wrong try again"
        return render(request, 'movie.html', {'mword': mword, 'msg': msg})
