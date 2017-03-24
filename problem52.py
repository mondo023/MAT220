def prob52():
    for a in range(1, 999, 2):
        for b in range(a + 2, 999, 2):
            for c in range(b + 2, 999, 2):
                if ( (1.0/a) + (1.0/b) + (1.0/c) == (1.0/3.0)):
                    return(a, b, c)
