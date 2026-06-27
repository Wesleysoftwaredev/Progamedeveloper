team = [2, 4, 5, 6, 7, 8, 10, 11, 14, 16]

players_selected=int(input('Which players were selected for the team:'))

found = False

for player in team:
    if player == players_selected:
        found=True
        break

if found:
    print('This player was selected')

else:
    print('This player was not selected')