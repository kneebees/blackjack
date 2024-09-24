import random
from os import system, name

deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
suits = ['D', 'C', 'H', 'S']

royalcards = ["K", "Q", "J"]
numcards = [2, 3, 4, 5, 6, 7, 8, 9, 10]

def morerounds(start):
  while start == '':
    deal1 = random.choice(deck)
    deal2 = random.choice(deck)
    deals = [deal1, deal2]
    cdeal1 = random.choice(deck)
    cdeal2 = random.choice(deck)
    cdeals = [cdeal1, cdeal2]
    yourgame('', deal1, deal2, deals, cdeals, cdeal1, points = pointkeep(deals, 0), cpoints = cpointkeep(cdeals))
    start = input('Click enter to play again or type a random character to end the game. ').lower()
    clear()

def print_card(deals):
  for i in deals:
    suit = random.choice(suits)
    value = str(i)
    if suit == 'S':
        suit_print = ' _____\n|'+str(value)+' .  |\n| /.\ |\n|(_._)|\n|  | '+str(value)+'|\n|_____|'
    elif suit == 'D':
        suit_print = ' _____\n|'+str(value)+' ^  |\n| / \ |\n| \ / |\n|  . '+str(value)+'|\n|_____|'
    elif suit == 'C':
        suit_print = ' _____\n|'+str(value)+' _  |\n| ( ) |\n|(_\'_)|\n|  | '+str(value)+'|\n|_____|'
    elif suit == 'H':
        suit_print = ' _____\n|'+str(value)+'_ _ |\n|( v )|\n| \ / |\n|  . '+str(value)+'|\n|_____|'
    print(suit_print)

def print_hit(hit):
  suit = random.choice(suits)
  value = str(hit)
  if suit == 'S':
      suit_print = ' _____\n|'+str(value)+' .  |\n| /.\ |\n|(_._)|\n|  | '+str(value)+'|\n|_____|'
  elif suit == 'D':
      suit_print = ' _____\n|'+str(value)+' ^  |\n| / \ |\n| \ / |\n|  . '+str(value)+'|\n|_____|'
  elif suit == 'C':
      suit_print = ' _____\n|'+str(value)+' _  |\n| ( ) |\n|(_\'_)|\n|  | '+str(value)+'|\n|_____|'
  elif suit == 'H':
      suit_print = ' _____\n|'+str(value)+'_ _ |\n|( v )|\n| \ / |\n|  . '+str(value)+'|\n|_____|'
  print(suit_print)

def print_computerdeal(cdeal1):
  suit = random.choice(suits)
  value = str(cdeal1)
  if suit == 'S':
    suit_print = ' _____\n|'+str(value)+' .  |\n| /.\ |\n|(_._)\n|  | '+str(value)+'|\n|_____|'
  elif suit == 'D':
    suit_print = ' _____\n|'+str(value)+' ^  |\n| / \ |\n| \ / |\n|  . '+str(value)+'|\n|_____|'
  elif suit == 'C':
    suit_print = ' _____\n|'+str(value)+' _  |\n| ( ) |\n|(_\'_)|\n|  | '+str(value)+'|\n|_____|'
  elif suit == 'H':
    suit_print = ' _____\n|'+str(value)+'_ _ |\n|( v )|\n| \ / |\n|  . '+str(value)+'|\n|_____|'
  print(suit_print)

def clear(): 
  if name == 'nt': 
      _ = system('cls') 
  else: 
      _ = system('clear')

def pointkeep(deals, x):
  points = 0
  for i in deals:
    if i in royalcards:
      points += 10
    elif i in numcards:
      points += i
    while i == 'A' and x == 1:
      acevalue = int(input("\nYou got an ace. Would you like it to be a 1 or an 11? "))
      if acevalue == 1:
        points += 1
        break
      elif acevalue == 11:
        points += 11
        break
      else:
        print("That answer is invalid. Try again.")
  return points

def cpointkeep(cdeals):
  cpoints = 0
  for i in cdeals:
    if i in royalcards:
      cpoints += 10
    elif i in numcards:
      cpoints += i
    elif i == 'A':
      if (cpoints + 11) <= 21:
        cpoints += 11
      elif (cpoints + 11) > 21:
        cpoints += 1
  return cpoints

def intro():
  rules = ''
  user = input("Welcome to BlackJack. What is your name? ").capitalize()
  clear()
  while rules != 'p' or rules != 'r':
    rules = input("Hello {}. Would you like to see the rules or start the game (r for rules and p for play)? ".format(user)).lower()
    if rules == 'r':
      start = input("\nRules: \n\nYou and the computer both get dealt 2 cards. \n\n2 - 10 are equivalent to their own value in points (2 = 2 points)\nRoyal cards are worth 10 points.\nAn ace can either be a 1 or an 11, which you can choose.\n\nThe goal of the game is to have your total points be as close to 21 as possible. To get to this, you can either choose to hit or stand. Hitting will give you another random card. Standing will end your turn so that you can keep your total. Going over 21 will make you lose, making the dealer/computer automatically win. If you get 21 points in the beginning, it's called a Blackjack and you automatically win. When it's the dealer's turn, they will hit until their points are 17 or higher. You can bet a certain amount each time you play and the dealer will match that amount.\n\nClick enter to start the game.")
      if start == '':
        rules = 'p'
    if rules == 'p':
      start = ''
      return start
      break
      
      
def yourpoints(deal1, deal2, deals, cdeal1):
  print("These are your cards: {}, and {}.\n".format(deal1, deal2))
  print_card(deals)

def computercard(cdeal1):
  print("\nThis is one of your opponent's cards: {}. \n".format(cdeal1))
  print_computerdeal(cdeal1)

def hitresult(points, hit, deals):
  if hit == "hit" or hit == 'h':
    hit = random.choice(deck)
    print("You drew a {}.".format(hit))
    deals.append(hit)
    print_hit(hit)
    print('\nYour hand: ', end = '')
    for i in deals:
      print(i, end = ' ')
    print('\n')
    if hit in royalcards:
      points += 10
    elif hit in numcards:
      points += hit
    elif hit == 'A':
      while hit == 'A':
        acevalue = int(input("You got an ace. Would you like it to be a 1 or an 11? "))
        if acevalue == 1:
          points += 1
          break
        elif acevalue == 11:
          points += 11
          break
        else:
          print("That answer is invalid. Try again.")
  return points

def stayresult(cpoints, hit, points, cdeals, game, ):
  if hit == 'stand' or hit == 's':
    cpointkeep(cdeals)
    while cpoints < 17:
      chit = random.choice(deck)
      if chit == 'J' or chit == 'Q' or chit == 'K':
        cpoints += 10
      elif chit == int:
        cpoints += chit
      elif chit == 'A':
        comhit = cpoints + 11
        if comhit <= 21:
          cpoints += 11
        if comhit >= 21:
          cpoints += 1
    if points < 21 and cpoints < 21 and points > cpoints:
      print("Congratulations. You won with {} points. The computer had {} points.".format(points, cpoints))
    elif points < 21 and cpoints < 21 and points < cpoints:
      print("Congratulations. You lost with {} points. The computer had {} points.".format(points, cpoints))
    elif cpoints > 21 and points < 21:
      print("Congratulations. You won with {} points and the computer went over 21.".format(points))
    elif points == cpoints:
      print("Congratulations. Both you and the computer tied with {} points.".format(points))
    game = 'end'
  if points == 21 and cpoints != 21:
    print("Congratulations. You won with exactly 21 points.")
    game = 'end'
  elif points == 21 and cpoints == 21:
    print("It was a tie. You and the computer both got 21.")
    game = 'end'
  return game
    

def over(points):
  if points > 21:
    print("You lost, going over 21 points.")
    game = 'end'
    return game

def blackjack(points):
  if points == 21:
    print("You got a BlackJack. Congratulations, you won.")
    game = 'end'
    return game

def yourgame(game, deal1, deal2, deals, cdeals, cdeal1, points, cpoints):
  clear()
  yourpoints(deal1, deal2, deals, yourpoints)
  computercard(cdeal1)
  points = pointkeep(deals, 1)
  game = blackjack(points)
  if game != 'end':
    while True:
      if game == 'end':
        break
      game = over(points)
      if game == 'end':
        break
      hit = input("\nWould you like to hit or stand? ").lower()
      clear()
      if hit != "hit" or hit != 'h' or hit != 'stand' or hit != 's':
        while True:
          if hit == "hit" or hit == 'h' or hit == 'stand' or hit == 's':
            break
          print("Write hit or stand.")
          hit = input("Would you like to hit or stand? ")
      points = hitresult(points, hit, deals)
      game = stayresult(cpoints, hit, points, cdeals, game)
      if game == 'end':
        break

morerounds(intro())
