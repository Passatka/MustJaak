import cv2
import numpy as np
import time
import os
import Cards
url = "https://192.168.74.45:8080/video"
cap = cv2.VideoCapture(url)
IM_WIDTH = 1920
IM_HEIGHT = 1080 
FRAME_RATE = 2
frame_rate_calc = 1
freq = cv2.getTickFrequency()
font = cv2.FONT_HERSHEY_SIMPLEX
path = os.path.dirname(os.path.abspath(__file__))
train_ranks = Cards.load_ranks( path + '/Card_Imgs/')
train_suits = Cards.load_suits( path + '/Card_Imgs/')
cards = []
current_cards = []
loendur = 0
new_game_counter = 0
time.sleep(1)
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
                # rank = cards[k].rank_img
                # suit = cards[k].suit_img
                # if len(rank) > 5 and len(suit) > 5:
                #     cv2.imshow("r", rank)
                #     cv2.imshow("s", suit)
                k = k + 1

        if loendur % 5 == 0:
            new_cards = [(i.best_rank_match, i.side) for i in cards]
        loendur += 1
        if len(new_cards) > len(current_cards) and ("Unknown", "Player") not in new_cards and ("Unknown", "Dealer") not in new_cards:
            current_cards = new_cards
        if new_cards == []:
            new_game_counter += 1
            if new_game_counter == 3:
                current_cards = []
                new_game_counter = 0
                loendur = 0
        if new_cards != []:
            new_game_counter = 0

    if current_cards:
        dealer_cards = []
        player_cards = []
        for i in current_cards:
            if i[1] == "Dealer":
                dealer_cards.append(i[0])
            if i[1] == "Player":
                player_cards.append(i[0])
        if loendur % 5 == 0:
            print(dealer_cards)
            print(player_cards)
    if (len(cards) != 0):
        temp_cnts = []
        for i in range(len(cards)):
            temp_cnts.append(cards[i].contour)
        cv2.drawContours(frame,temp_cnts, -1, (255,0,0), 2)
    cv2.putText(frame,"FPS: "+str(int(frame_rate_calc)),(10,26),font,0.7,(255,0,255),2,cv2.LINE_AA)
    cv2.imshow("Card Detector",frame)

    # print("New: ", new_cards)
    # print("Current: ",current_cards)
    t2 = cv2.getTickCount()
    time1 = (t2-t1)/freq
    frame_rate_calc = 1/time1
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Vajuta 'q' lõpetamiseks
        break

cap.release()
cv2.destroyAllWindows()