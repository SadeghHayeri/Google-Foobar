def answer(M, F):
    M, F = int(M), int(F)
    big, small = (M, F) if M > F else (F, M)
    
    genaration_count = 0
    
    while small >= 1:
        if big == small:
            break
        
        h = ((big-1)/small)
        genaration_count += h
        big -= small * h

        big, small = (big, small) if big > small else (small, big)
        
        
    return str(genaration_count) if (small == 1 and big == 1) else "impossible"
