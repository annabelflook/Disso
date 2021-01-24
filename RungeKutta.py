def rungekutta(differential, x, y):
    '''
    Iterative method to solve a differential equation, dy/dx. 
    Takes x and y as starting points.
    Returns the new 'y'
    '''
    
    h = 0.05 # small value of 'h' gives smaller change in 'y' along the differential.
    k1 = h * differential(x, y)
    k2 = h * differential(x + (h / 2), y + (k1 / 2))
    k3 = h * differential(x + (h / 2), y + (k2 / 2))
    k4 = h * differential(x + h, y + k3)

    y = y + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    
    return y
