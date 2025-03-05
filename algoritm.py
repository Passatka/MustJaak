def card_value(rank):
    
    if rank in ['Jack', 'Queen', 'King', 'Ten']:
        return 10
    elif rank == 'Ace':
        return 11
    else:
        rank_map = {
            'Two': 2,
            'Three': 3,
            'Four': 4,
            'Five': 5,
            'Six': 6,
            'Seven': 7,
            'Eight': 8,
            'Nine': 9
        }
        return rank_map.get(rank, 0)


def hand_value(cards):
   
    total = 0
    aces = 0
    for card in cards:
        value = card_value(card[0])
        total += value
        if card[0] == 'Ace':
            aces += 1
    # Kui summa ületab 21, muuda mõni Ace väärtuseks 1
    while total > 21 and aces:
        total -= 10
        aces -= 1
    is_soft = (aces > 0)
    return total, is_soft


def hi_lo_count(rank):
    
    if rank in ['Two', 'Three', 'Four', 'Five', 'Six']:
        return 1
    elif rank in ['Seven', 'Eight', 'Nine']:
        return 0
    elif rank in ['Ten', 'Jack', 'Queen', 'King', 'Ace']:
        return -1
    return 0


def update_running_count(visible_cards):
   
    count = 0
    for card in visible_cards:
        count += hi_lo_count(card[0])
    return count


def blackjack_decision(player_cards, dealer_card, count):

    total, is_soft = hand_value(player_cards)
    dealer_val = card_value(dealer_card[0])
    
    # Kui blackjack (kaks kaarti ja kokku 21), siis jääd alati standima.
    if total == 21 and len(player_cards) == 2:
        return 'STAND'
    
    # Põhiline strateegia
    decision = None
    if not is_soft:
        # Hard käed
        if total <= 11:
            decision = 'HIT'
        elif total == 12:
            if dealer_val in [4, 5, 6]:
                decision = 'STAND'
            else:
                decision = 'HIT'
        elif 13 <= total <= 16:
            if dealer_val in [2, 3, 4, 5, 6]:
                decision = 'STAND'
            else:
                decision = 'HIT'
        else:  # 17 või rohkem
            decision = 'STAND'
    else:
        # Soft käed
        if total <= 17:
            decision = 'HIT'
        elif total == 18:
            # Kui diileri kaart on tugev (9, 10 või Ace, mis loetakse 11-na),
            # võib kaaluda kaardi võtmist (HIT), muudel juhtudel jäädakse (STAND)
            if dealer_val in [9, 10, 11]:
                decision = 'HIT'
            else:
                decision = 'STAND'
        else:
            decision = 'STAND'
