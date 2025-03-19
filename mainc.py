import cv2
import numpy as np
import time
import os
import Cards
url = "https://192.168.219.17:8080/video" #NB! Muutub!
url = "https://192.168.219.17:8080/video" #NB! Muutub!
cap = cv2.VideoCapture(url)
IM_WIDTH = 1920
IM_HEIGHT = 1080 
FRAME_RATE = 1
frame_rate_calc = 1
f = open("decision.txt", "w")
freq = cv2.getTickFrequency()
font = cv2.FONT_HERSHEY_SIMPLEX
path = os.path.dirname(os.path.abspath(__file__))
train_ranks = Cards.load_ranks( path + '/Card_Imgs/')
train_suits = Cards.load_suits( path + '/Card_Imgs/')
rank_map = {
            'Two': 2,
            'Three': 3,
            'Four': 4,
            'Five': 5,
            'Six': 6,
            'Seven': 7,
            'Eight': 8,
            'Nine': 9,
            "Ten": 10,
            "Jack": 10,
            "Queen": 10,
            "King": 10,
            "Ace" : 11
        }
cards = []
current_cards = []
loendur = 0
new_game_counter = 0
dealer_cards = []
player_cards = []
dealer_aces = 0
player_aces = 0
dealer_value = 0
player_value = 0
old_dealer_value = 0
old_player_value = 0
counter = 0
counter = 0
n1 = 0
n2 = 0
new_games = 0
new_games = 0
new_game = True
decidable = False
def player_decision(player_value, dealer_value, player_aces):
    if player_aces > 0:
        if player_value <= 17:
            decision = "HIT"    
        elif player_value == 18:
            if dealer_value <= 8:
                decision = "STAND"
            elif dealer_value >= 9:
                decision = "HIT"
        elif player_value >= 19:
            decision = "STAND"
        return decision
    elif player_aces == 0:
        if player_value <= 11:
            decision = "HIT"
        elif player_value == 12:
            if dealer_value in (2,3,7,8,9,10,11):
                decision = "HIT"
            elif dealer_value in (4,5,6):
                decision = "STAND"
        elif player_value <= 16:
            if dealer_value <= 6:
                decision = "STAND"
            elif dealer_value >= 7:
                decision = "HIT"
        elif player_value >= 17:
            decision = "STAND"
        return decision
    return -1

while True:
    ret, frame = cap.read()  # Loeb kaadri
    if not ret:
        break
    t1 = cv2.getTickCount()
    pre_proc = Cards.preprocess_image(frame)
    cnts_sort, cnt_is_card = Cards.find_cards(pre_proc)
    if len(cnts_sort) != 0:
        cards = []
        k = 0

        for i in range(len(cnts_sort)):
            if (cnt_is_card[i] == 1):
                cards.append(Cards.preprocess_card(cnts_sort[i],frame))
                cards[k].best_rank_match,cards[k].best_suit_match,cards[k].rank_diff,cards[k].suit_diff = Cards.match_card(cards[k],train_ranks,train_suits)
                frame = Cards.draw_results(frame, cards[k])
                rank = cards[k].rank_img
                suit = cards[k].suit_img
                if len(rank) > 5 and len(suit) > 5:
                    cv2.imshow("r", rank)
                    cv2.imshow("s", suit)
                rank = cards[k].rank_img
                suit = cards[k].suit_img
                if len(rank) > 5 and len(suit) > 5:
                    cv2.imshow("r", rank)
                    cv2.imshow("s", suit)
                k = k + 1

        if loendur % 4 == 0:
        if loendur % 4 == 0:
            new_cards = [(i.best_rank_match, i.side) for i in cards]
            if len(new_cards) > len(current_cards) and ("Unknown", "Player") not in new_cards and ("Unknown", "Dealer") not in new_cards:
                current_cards = new_cards
                decidable = True
            if new_cards == []:
                new_game_counter += 1
                if new_game_counter == 3:
                    current_cards = []
                    new_game_counter = 0
                    new_game = True
                    old_dealer_value = 0
                    old_player_value = 0
                    loendur = 0
                counter = 0
                new_games += 1
            if new_cards != []:
                new_game_counter = 0

    if current_cards and loendur % 4 == 0:
    if current_cards and loendur % 4 == 0:
        dealer_cards = []
        player_cards = []
        dealer_aces = 0
        player_aces = 0
        dealer_value = 0
        player_value = 0
        blackjack = False
        for i in current_cards:
            if i[1] == "Dealer":
                dealer_cards.append(i[0])
            if i[1] == "Player":
                player_cards.append(i[0])
        for card in dealer_cards:
            if card == "Ace":
                dealer_aces += 1
            dealer_value += rank_map[card]
        for card in player_cards:
            if card == "Ace":
                player_aces += 1
            player_value += rank_map[card]
        for _ in range(dealer_aces):
            if dealer_value > 21 and dealer_aces > 0:
                dealer_aces -= 1
                dealer_value -= 10
        for _ in range(player_aces):
            if player_value > 21 and player_aces > 0:
                player_aces -= 1
                player_value -= 10
        if dealer_value == old_dealer_value:
            n1 += 1
        else:
            n1 = 0
        if player_value == old_player_value:
            n2 += 1
        else:
            n2 = 0
        old_dealer_value = dealer_value
        old_player_value = player_value
        print(old_dealer_value,old_player_value)
    if len(player_cards) == 2 and player_value == 21:
        blackjack = True
        if dealer_value < 10 or (dealer_value == 21 and len(dealer_cards > 2)):
            f.write("WIN 0 0")
    if player_value > 21:
        f.write("BUST 0 0")
    elif dealer_value > 21:
        f.write("WIN 0 0")
    elif not new_game and dealer_value >= 17: #DEALER MUST STAND ON 17
        if (player_value == dealer_value and not blackjack) or (blackjack and dealer_value == 21 and len(dealer_cards) == 2):
            f.write("PUSH 0 0")
        elif player_value > dealer_value:
            f.write("WIN 0 0")
        elif player_value < dealer_value:
            f.write("LOSS 0 0")
    elif new_game and n1 > 2 and n2 > 2 and not blackjack and decidable:
        decision = player_decision(player_value, dealer_value, player_aces)
        counter += 1
        f = open("decision.txt", "w")
        f.write(f"{decision} {counter} {new_games}")
        f.close()
        counter += 1
        f = open("decision.txt", "w")
        f.write(f"{decision} {counter} {new_games}")
        f.close()
        if decision == "STAND":
            new_game = False
        decidable = False
        n1 = 0
        n2 = 0
    loendur += 1
    if (len(cards) != 0):
        temp_cnts = []
        for i in range(len(cards)):
            temp_cnts.append(cards[i].contour)
        cv2.drawContours(frame,temp_cnts, -1, (255,0,0), 2)
    cv2.putText(frame,"FPS: "+str(int(frame_rate_calc)),(10,26),font,0.7,(255,0,255),2,cv2.LINE_AA)
    cv2.imshow("Card Detector", frame)
    cv2.imshow("Card Detector", frame)

    # print("New: ", new_cards)
    # print("Current: ",current_cards)
    t2 = cv2.getTickCount()
    time1 = (t2-t1)/freq
    frame_rate_calc = 1/time1
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Vajuta 'q' lõpetamiseks
        break

cap.release()
cv2.destroyAllWindows()