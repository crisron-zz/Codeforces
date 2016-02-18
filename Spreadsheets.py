# Problem link: http://codeforces.com/contest/1/problem/B

import re

# Maps 0 - Z, 1 - A, 2 - B, ..., 25 - Y
def charAt( position ):
    if position:
        return chr( position + ord( 'A' ) - 1 )
    return 'Z'

def NumberToString( cellCoord ):
    i = 1
    row = ""
    # Get the row from the coordinates
    while cellCoord[ i ] != 'C':
        row += cellCoord[ i ]
        i += 1

    i += 1
    col = ""
    # Get the column from the coordinates
    while i < len( cellCoord ):
        col += cellCoord[ i ]
        i += 1

    # Convert the column string into integer
    col = int( col )

    colLen = 1
    x = 26
    power = 2
    # Calculate the length of the resultant column string
    while col > x:
        x += 26 ** power
        colLen += 1
        power += 1

    colStr = ""
    # Convert base 10 to base 26
    while colLen:
        rem = col % 26
        colStr += charAt( rem )
        if col % 26: 
            col /= 26
        else:
            col /= 26
            col -= 1
        colLen -= 1

    # Reverse the column string
    colStr = colStr[ ::-1 ]

    output = colStr + row
    print output 


# Maps A - 1, B - 2, ..., Z - 26
def pos( char ):
    return ( ord( char ) - ord( 'A' ) + 1 )

def StringToNumber( cellCoord ):
    col = ""
    row = ""
    # Fetch row and column parts from the coordinates
    # Row part consists of only numbers
    # Column part consists of only characters
    for i in range( len( cellCoord ) ):
        if re.match( '[0-9]', cellCoord[ i ] ):
           row += cellCoord[ i ] 
        else:
            col += cellCoord[ i ]

    n = len( col )
    offset = 0

    # Leave all strings of length 1 to n-1
    for i in range( 1, n ):
        offset += 26 ** i

    # I saw this pattern while calculating some
    # answers by hand
    # An easier way to do this would be to just
    # convert the given col in base 26 to base 10
    # using the standard method
    for i in range( 1, n ):
        offset += ( 26 ** ( n - i ) ) * ( pos( col[ i - 1 ] ) - 1 )
    offset += pos( col[ n - 1 ] )

    output = "R" + row + "C" + str( offset )
    print output

t = raw_input()
t = int( t )

while t:
    cellCoord = raw_input()
    if re.match( '[A-Z]+[0-9]+[A-Z]+[0-9]+', cellCoord ):
        NumberToString( cellCoord )
    else:
        StringToNumber( cellCoord )
    t -= 1
