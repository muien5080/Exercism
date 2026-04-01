import math
import re

def cipher_text(plain_text):
    # Step 1: normalize (remove non-alphanumeric, lowercase)
    normalized = re.sub(r'[^a-z0-9]', '', plain_text.lower())
    length = len(normalized)
    
    if length == 0:
        return ""
    
    # Step 2: determine rows (r) and columns (c)
    c = math.ceil(math.sqrt(length))
    r = math.ceil(length / c)
    
    # Step 3: build the rectangle (row-wise)
    rows = [normalized[i:i+c] for i in range(0, length, c)]
    
    # Step 4: pad rows to ensure equal length
    rows = [row.ljust(c) for row in rows]
    
    # Step 5: read column-wise
    columns = []
    for col in range(c):
        chunk = ''.join(rows[row][col] for row in range(r))
        columns.append(chunk)
    
    # Step 6: join with spaces
    return ' '.join(columns)