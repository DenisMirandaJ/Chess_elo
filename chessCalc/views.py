from django.shortcuts import render
from .elo.elo import calculate_elo


def elo_calculator(request):
    return render(request, "chessCalc/calc.html")


def results(request):
    print(request.POST)
    white_elo = float(request.POST['white_elo'])
    white_matches = float(request.POST['white_matches'])
    black_elo = float(request.POST['black_elo'])
    black_matches = float(request.POST['black_matches'])
    winner = request.POST['winner']

    if winner == 'white':
        new_white_elo = calculate_elo(white_elo, black_elo, 1)
        new_black_elo = calculate_elo(black_elo, white_elo, 0)
    elif winner == 'black':
        new_white_elo = calculate_elo(white_elo, black_elo, 0)
        new_black_elo = calculate_elo(black_elo, white_elo, 1)
    else:
        new_white_elo = calculate_elo(white_elo, black_elo, 0.5)
        new_black_elo = calculate_elo(black_elo, white_elo, 0.5)
    context = {'new_white_elo': new_white_elo, 'new_black_elo': new_black_elo, 'winner': winner}
    return render(request, "chessCalc/results.html", context=context)