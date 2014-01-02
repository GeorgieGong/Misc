import numpy
import matplotlib.pyplot
import matplotlib.colors

def KAUSTColor(color):
    # this returns the colors of KAUST logo
    # input parameter the name of the color
    # blue, orange, green, yellow, grey
    chart = {'blue': (46,141,150), 'orange': (231,113,33), 'green': (117,199,25), 'yellow': (246,183,31), 'grey': (128,118,111)}
    try:
        rv = chart[color]
    except KeyError:
        rv = chart['grey']
    return [a/255.0 for a in rv]

def KAUSTColorMap():
    # returns the "kaust-compliant"
    # colormap for 3d plots
    # idea stolen from
    # http://stackoverflow.com/questions/16834861/create-own-colormap-using-matplotlib-and-plot-color-scale
    seq = [KAUSTColor('blue'),KAUSTColor('green'),0.33,KAUSTColor('green'),KAUSTColor('yellow'),0.66,KAUSTColor('yellow'),KAUSTColor('orange')]
    seq = [(None,) * 3, 0.0] + list(seq) + [1.0, (None,) * 3]
    cdict = {'red': [], 'green': [], 'blue': []}
    for i, item in enumerate(seq):
        if isinstance(item, float):
            r1, g1, b1 = seq[i - 1]
            r2, g2, b2 = seq[i + 1]
            cdict['red'].append([item, r1, r2])
            cdict['green'].append([item, g1, g2])
            cdict['blue'].append([item, b1, b2])
    return matplotlib.colors.LinearSegmentedColormap('CustomMap', cdict)

