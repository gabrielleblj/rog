import numpy as np

MAP = np.full((20,20), None)

MAP[0][:8] = '-'
MAP[7][:8] = '-'
MAP[10][:4] = '-'
MAP[12][:4] = '-'
MAP[15][:11] = '-'
MAP[19][:11] = '-'
MAP[3][13:18] = '-'
MAP[19][13:18] = '-'
MAP[7][14:17] = '-'

MAP[3:20][13] = '|'
#MAP[3:20][17] = '|'
MAP[:8][0] = '|'
MAP[:8][7] = '|'
MAP[15:20][0] = '|'
MAP[15:20][10] = '|'
MAP[7:12][9] = '|'
MAP[7:12][12] = '|'

print(MAP)