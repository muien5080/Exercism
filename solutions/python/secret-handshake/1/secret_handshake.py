def commands(binary_str):
    actions = []
    
    # Ensure we only look at the rightmost 5 bits
    binary_str = binary_str[-5:].zfill(5)
    
    if binary_str[-1] == "1":
        actions.append("wink")
    if binary_str[-2] == "1":
        actions.append("double blink")
    if binary_str[-3] == "1":
        actions.append("close your eyes")
    if binary_str[-4] == "1":
        actions.append("jump")
    
    # If the 5th bit is 1, reverse the actions
    if binary_str[-5] == "1":
        actions.reverse()
    
    return actions