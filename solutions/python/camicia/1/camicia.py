from collections import deque

def simulate_game(player_a, player_b):
    A = deque(player_a)
    B = deque(player_b)
    
    pile = []
    tricks = 0
    cards_played = 0
    
    # Payment mapping
    payment = {'J': 1, 'Q': 2, 'K': 3, 'A': 4}
    
    def normalize(deck):
        return tuple(c if c in payment else 'N' for c in deck)
    
    seen = set()
    
    current = 'A'  # A starts
    
    while True:
        # Loop detection (start of round = no active penalty)
        state = (normalize(A), normalize(B))
        if state in seen:
            return {
                "status": "loop",
                "cards": cards_played,
                "tricks": tricks
            }
        seen.add(state)
        
        penalty_due = 0
        last_face_player = None
        
        while True:
            # Choose player
            if current == 'A':
                player, opponent = A, B
            else:
                player, opponent = B, A
            
            # Player cannot play
            if not player:
                # opponent collects pile
                opponent.extend(pile)
                tricks += 1
                pile.clear()
                
                # check win
                if not player:
                    return {
                        "status": "finished",
                        "cards": cards_played,
                        "tricks": tricks
                    }
                
                current = 'A' if current == 'B' else 'B'
                break
            
            # Play card
            card = player.popleft()
            pile.append(card)
            cards_played += 1
            
            if card in payment:
                penalty_due = payment[card]
                last_face_player = current
                current = 'A' if current == 'B' else 'B'
            else:
                if penalty_due > 0:
                    penalty_due -= 1
                    
                    if penalty_due == 0:
                        # last_face_player collects
                        if last_face_player == 'A':
                            A.extend(pile)
                            current = 'A'
                        else:
                            B.extend(pile)
                            current = 'B'
                        
                        tricks += 1
                        pile.clear()
                        
                        # check win
                        if not A or not B:
                            return {
                                "status": "finished",
                                "cards": cards_played,
                                "tricks": tricks
                            }
                        
                        break
                else:
                    current = 'A' if current == 'B' else 'B'