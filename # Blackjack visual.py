# Blackjack

# CARTAS
# NAIPE, CARTA E VALOR

import pygame as pygame

import random
naipes  = ('Copas', 'Ouros', 'Paus', 'Espadas')
tipos = ('Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Oito', 'Nove', 'Dez', 'Valete', 'Dama', 'Rei', 'Manilha', 'Às')
valores = {'Dois':2, 'Três':3, 'Quatro':4, 'Cinco':5, 'Seis':6, 'Manilha':7, 'Oito':8, 
            'Nove':9, 'Dez':10, 'Valete':10, 'Dama':10, 'Rei':10, 'Às':11}
numeracao = list(range(1,53))
n = 0

Mesa = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/360_F_325387454_sPiaCL3tpIyVnA2YxQEFGl7IXRCqbjnJ.jpg')
Mesa = pygame.transform.scale(Mesa, (1280, 720))
Parte_Tras = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_001_51169850549_o.jpg')
Parte_Tras = pygame.transform.scale(Parte_Tras, (100, 165))
dois_e = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_005_51168395387_o.jpg')
dois_e = pygame.transform.scale(dois_e, (100, 165))
tres_e = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_006_51169292333_o.jpg')
tres_e = pygame.transform.scale(tres_e, (100, 165))
quatro_e = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_007_51170161085_o.jpg')
quatro_e = pygame.transform.scale(quatro_e, (100, 165))
cinco_e = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_008_51168395397_o.jpg')
cinco_e = pygame.transform.scale(cinco_e, (100, 165))
seis_e = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_009_51169069131_o.jpg')
seis_e = pygame.transform.scale(seis_e, (100, 165))
oito_e = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_011_51169069161_o.jpg')
oito_e = pygame.transform.scale(oito_e, (100, 165))
nove_e = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_012_51169292403_o.jpg')
nove_e = pygame.transform.scale(nove_e, (100, 165))
dez_e = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_013_51169069211_o.jpg')
dez_e = pygame.transform.scale(dez_e, (100, 165))
valete_e = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_014_51169850719_o.jpg')
valete_e = pygame.transform.scale(valete_e, (100, 165))
dama_e = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_015_51168395532_o.jpg')
dama_e = pygame.transform.scale(dama_e, (100, 165))
rei_e = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_016_51170161210_o.jpg')
rei_e = pygame.transform.scale(rei_e, (100, 165))
manilha_e = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_010_51168395432_o.jpg')
manilha_e = pygame.transform.scale(manilha_e, (100, 165))
as_e = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_004_51168395362_o.jpg')
as_e = pygame.transform.scale(as_e, (100, 165))
dois_c = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_054_51169291753_o.jpg')
dois_c = pygame.transform.scale(dois_c, (100, 165))
tres_c = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_053_51170160420_o.jpg')
tres_c = pygame.transform.scale(tres_c, (100, 165))
quatro_c = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_052_51169850004_o.jpg')
quatro_c = pygame.transform.scale(quatro_c, (100, 165))
cinco_c = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_051_51169850009_o.jpg')
cinco_c = pygame.transform.scale(cinco_c, (100, 165))
seis_c = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_050_51168394692_o.jpg')
seis_c = pygame.transform.scale(seis_c, (100, 165))
oito_c = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_048_51168394772_o.jpg')
oito_c = pygame.transform.scale(oito_c, (100, 165))
nove_c = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_047_51169291883_o.jpg')
nove_c = pygame.transform.scale(nove_c, (100, 165))
dez_c = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_046_51169291908_o.jpg')
dez_c = pygame.transform.scale(dez_c, (100, 165))
valete_c = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_045_51169068601_o.jpg')
valete_c = pygame.transform.scale(valete_c, (100, 165))
dama_c = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_044_51169291958_o.jpg')
dama_c = pygame.transform.scale(dama_c, (100, 165))
rei_c = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_044_51169291958_o.jpg')
rei_c = pygame.transform.scale(rei_c, (100, 165))
manilha_c = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_049_51169291808_o.jpg')
manilha_c = pygame.transform.scale(manilha_c, (100, 165))
as_c = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_055_51169849954_o.jpg')
as_c = pygame.transform.scale(as_c, (100, 165))
dois_o = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_018_51169292283_o.jpg')
dois_o = pygame.transform.scale(dois_o, (100, 165))
tres_o = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_019_51169069026_o.jpg')
tres_o = pygame.transform.scale(tres_o, (100, 165))
quatro_o = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_020_51169850499_o.jpg')
quatro_o = pygame.transform.scale(quatro_o, (100, 165))
cinco_o = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_021_51168395277_o.jpg')
cinco_o = pygame.transform.scale(cinco_o, (100, 165))
seis_o = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_022_51169068981_o.jpg')
seis_o = pygame.transform.scale(seis_o, (100, 165))
oito_o = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_024_51169292183_o.jpg')
oito_o = pygame.transform.scale(oito_o, (100, 165))
nove_o = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_025_51169292168_o.jpg')
nove_o = pygame.transform.scale(nove_o, (100, 165))
dez_o = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_026_51170160860_o.jpg')
dez_o = pygame.transform.scale(dez_o, (100, 165))
valete_o = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_027_51168395167_o.jpg')
valete_o = pygame.transform.scale(valete_o, (100, 165))
dama_o = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_028_51170160815_o.jpg')
dama_o = pygame.transform.scale(dama_o, (100, 165))
rei_o = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_029_51169850314_o.jpg')
rei_o = pygame.transform.scale(rei_o, (100, 165))
manilha_o = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_023_51168395212_o.jpg')
manilha_o = pygame.transform.scale(manilha_o, (100, 165))
as_o = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_017_51170161220_o.jpg')
as_o = pygame.transform.scale(as_o, (100, 165))
dois_p = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_041_51169291998_o.jpg')
dois_p = pygame.transform.scale(dois_p, (100, 165))
tres_p = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_040_51170160660_o.jpg')
tres_p = pygame.transform.scale(tres_p, (100, 165))
quatro_p = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_039_51170160680_o.jpg')
quatro_p = pygame.transform.scale(quatro_p, (100, 165))
cinco_p = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_038_51170160690_o.jpg')
cinco_p = pygame.transform.scale(cinco_p, (100, 165))
seis_p = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_037_51169292028_o.jpg')
seis_p = pygame.transform.scale(seis_p, (100, 165))
oito_p = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_035_51169850209_o.jpg')
oito_p = pygame.transform.scale(oito_p, (100, 165))
nove_p = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_034_51169292043_o.jpg')
nove_p = pygame.transform.scale(nove_p, (100, 165))
dez_p = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_033_51169850239_o.jpg')
dez_p = pygame.transform.scale(dez_p, (100, 165))
valete_p = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_032_51170160755_o.jpg')
valete_p = pygame.transform.scale(valete_p, (100, 165))
dama_p = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_031_51170160770_o.jpg')
dama_p = pygame.transform.scale(dama_p, (100, 165))
rei_p = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_030_51169068826_o.jpg')
rei_p = pygame.transform.scale(rei_p, (100, 165))
manilha_p = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_036_51169850204_o.jpg')
manilha_p = pygame.transform.scale(manilha_p, (100, 165))
as_p = pygame.image.load('C:/Users/joaob/Documents/Python Scripts/Visualcode/Cartas/bicycle-astronaut-snoopy_042_51169850144_o.jpg')
as_p = pygame.transform.scale(as_p, (100, 165))


num_dic = {1:dois_c, 2:tres_c, 3:quatro_c, 4:cinco_c, 5:seis_c, 6:oito_c, 7:nove_c, 8:dez_c, 9:valete_c, 10:dama_c, 11:rei_c, 12:manilha_c
           ,13:as_c, 14: dois_o, 15:tres_o, 16:quatro_o, 17:cinco_o, 18:seis_o, 19:oito_o, 20: nove_o, 21: dez_o, 22:valete_o, 23:dama_o, 
            24: rei_o, 25:manilha_o, 26:as_o, 27:dois_p, 28:tres_p, 29:quatro_p, 30:cinco_p, 31:seis_p, 32:oito_p, 33:nove_p, 34:dez_p, 
             35:valete_p, 36:dama_p, 37:rei_p, 38:manilha_p, 39:as_p, 40:dois_e, 41:tres_e, 42:quatro_e, 43:cinco_e, 44:seis_e, 45:oito_e,
              46:nove_e, 47:dez_e, 48:valete_e, 49:dama_e, 50:rei_e, 51:manilha_e, 52:as_e }

class Card:

    def __init__(self, naipe, tipo, numeracao, num_dic):
        self.naipe = naipe
        self.tipo = tipo
        self.valor = valores[tipo]
        self.numeracao = numeracao
        self.imagem = num_dic[numeracao]

    def __str__(self):
        return self.tipo + ' de ' + self.naipe
    

class Deck:

    def __init__(self, n, num_dic):

        self.all_cards = []

        for naipe in naipes:
            for tipo in tipos:
                n = n+1
                new_card = Card(naipe, tipo, n, num_dic)
                self.all_cards.append(new_card)
    
    def shuffle(self):

        random.shuffle(self.all_cards)

    def deal_one(self):

        return self.all_cards.pop()
    

class Hand:
    
    def __init__(self,name):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value = self.value + card.valor

        if card.tipo == 'Às':
            self.aces = self.aces + 1

    def adjust_for_ace(self):
        if self.aces != 0 and self.value > 21:
            self.value = self.value - 10
            self.aces = self.aces - 1


class Chips:

    def __init__(self):
        self.value = 200
        self.bet = 10

        

def take_bet(chips):
    
     while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.value:
                print("Sorry, your bet can't exceed",chips.value)
            else:
                break


def hit(deck, hand):

    added_card = deck.deal_one()
    hand.add_card(added_card)
    hand.adjust_for_ace()

       
def draw_some_cards(player, dealer):
    for i in range(len(player.cards)):
        screen.blit(player.cards[i].imagem, (70+70*i, 410))

    screen.blit(dealer.cards[0].imagem, (70, 155))
    screen.blit(Parte_Tras, (145, 155))


def draw_all_cards(player, dealer):
    for i in range(len(player.cards)):
        screen.blit(player.cards[i].imagem, (70+70*i, 410))
    for j in range(len(dealer.cards)):
       screen.blit(dealer.cards[j].imagem, (70+70*j, 155))

def draw_conclusion(conclusion):
    global chips
    if conclusion == 'PW':
        screen.blit(textfont.render('PLAYER WINS!', True, 'grey'), (460, 360))
        chips.value = chips.value + chips.bet
        chips.bet = 0
    if conclusion == 'DW':
        screen.blit(textfont.render('DEALER WINS!', True, 'grey'), (460, 360))
        chips.value = chips.value - chips.bet
        chips.bet = 0
    if conclusion == 'PUSH':
        screen.blit(textfont.render('PUSH!', True, 'grey'), (520, 360))


#GAME LOGIC

display_width = 1280
display_height = 720

backgroundcolor = (34,139,34)
white = (255,255,255)
grey = (220,220,220)
black = (0,0,0)
green = (0, 200, 0)
red = (255,0,0)
light_slat = (119,136,153)
dark_slat = (47, 79, 79)
dark_red = (255, 0, 0)
pygame.init()
font = pygame.font.SysFont("Arial", 20)
textfont = pygame.font.SysFont('Arial Bold', 70)
game_end = pygame.font.SysFont('dejavusans', 100)
blackjack = pygame.font.SysFont('roboto', 70)

screen = pygame.display.set_mode([display_width, display_height])
pygame.display.set_caption('Jogo de Blackjack')
fps = 60
timer = pygame.time.Clock()
active = True

def draw_game(act):
    button_list = []

    if not act:
        deal = pygame.draw.rect(screen, 'grey', [930,20,300,100], 0, 5)
        pygame.draw.rect(screen, 'green', [930,20,300,100], 3, 5)
        deal_text = font.render('DEAL HAND', True, 'black')
        screen.blit(deal_text, (945, 50))
        button_list.append(deal)
    else:
        hit = pygame.draw.rect(screen, 'grey', [800, 550, 200, 100], 0, 5)
        pygame.draw.rect(screen, 'green', [800, 550, 200, 100], 3, 5)
        hit_text = textfont.render('HIT', True, 'black')
        screen.blit(hit_text, (858, 575))
        button_list.append(hit)
        stand = pygame.draw.rect(screen, 'grey', [1055, 550, 200, 100], 0, 5)
        pygame.draw.rect(screen, 'green', [275+780, 550, 200, 100], 3, 5)
        stand_text = textfont.render('STAND', True, 'black')
        screen.blit(stand_text, (1075, 575))
        button_list.append(stand)
        restart = pygame.draw.rect(screen, 'grey', [1000, 0, 200, 100], 0, 5)
        pygame.draw.rect(screen, 'green', [1000, 0, 200, 100], 3, 5)
        stand_text = textfont.render('RESET', True, 'black')
        screen.blit(stand_text, (1020, 30))
        button_list.append(restart)

    return button_list
    
def draw_money():
    global chips
    screen.blit(textfont.render(f'CHIPS = {chips.value}', True, 'grey'), (520, 560))


def reset_game(n, num_dic):

    global deck, player, dealer, player_turn

    deck = Deck(n, num_dic)
    deck.shuffle()
    player = Hand('Player')
    dealer = Hand('Dealer')

    for _ in range(2):
        card = deck.deal_one()
        player.add_card(card)
        card = deck.deal_one()
        dealer.add_card(card)
        
    player_turn = True


reset_game(n, num_dic)

chips = Chips()
game = True

while game == True:

    
    timer.tick(fps)
    screen.fill('black')
    screen.blit(Mesa, (0, 0))
    buttons = draw_game(active)
    draw_some_cards(player, dealer)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.display.quit()
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            # if player can hit, allow them to draw a card
                # if buttons[2].collidepoint(event.pos) and chips.bet != 0
                if buttons[0].collidepoint(event.pos) and player.value < 21 and player_turn == True:
                    hit(deck, player)
                    draw_some_cards(player, dealer)
                    player_turn = True
                    if player.value >= 21:
                        player_turn = False
                # allow player to end turn (stand)
                elif buttons[1].collidepoint(event.pos) and player.value <21 and player_turn == True:
                    player_turn = False
                elif buttons[2].collidepoint(event.pos):
                    reset_game(n, num_dic)

    if player.value == 21:
        player.turn = False
    if player_turn == True:
        draw_some_cards(player, dealer)
    elif player_turn == False:
        if player.value < 21:
            while dealer.value < 17:
                hit(deck, dealer)
        
        draw_all_cards(player, dealer)
        
        if player.value == 21:
            conclusion = 'PW'
            draw_conclusion(conclusion)

        elif player.value > 21:
            conclusion = 'DW'
            draw_conclusion(conclusion)

        elif dealer.value > 21:
            conclusion = 'PW'
            draw_conclusion(conclusion)

        elif dealer.value > player.value:
            conclusion = 'DW'
            draw_conclusion(conclusion)
            
        elif dealer.value == player.value:
            conclusion = 'PUSH'
            draw_conclusion(conclusion)
            
        elif player.value > dealer.value:
            conclusion = 'PW'
            draw_conclusion(conclusion)

        draw_money()
            

    
    pygame.display.flip()

pygame.quit()