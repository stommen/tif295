import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

plt.style.use('default')

# LaTeX font
plt.rc('text', usetex = True)
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'serif'
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
font_size = 14
plt.rcParams['font.size'] = font_size

# Seaborn style
sns.set_style('whitegrid', {'axes.facecolor': '0.95'})

N_detections_layer = np.array([
    4, 2, 5, 6, 3, 3, 2, 3, 1, 1, 3, 3, 3, 2, 1, 2, 4, 2, 3, 2, 3, 7, 
    11, 10, 13, 23, 23, 31, 32, 38, 45, 58, 63, 69, 74, 75, 89, 87, 100, 
    111, 119, 131, 127, 152, 140, 168, 167, 181, 193, 194, 218, 208, 236, 
    229, 262, 268, 276, 291, 288, 315, 307, 342, 336, 356, 364, 371, 400, 
    388, 427, 408, 445, 444, 440, 486, 472, 744, 802, 738, 786, 778, 779, 
    801, 777, 848, 785, 847, 843, 821, 865, 810, 910, 859, 875, 905, 877, 
    952, 895, 950, 912, 972, 978, 961, 1034, 968, 1061, 997, 1052, 1051, 
    1059, 1145, 1083, 1190, 1126, 1216, 1208, 1207, 1275, 1229, 1338, 1266, 
    1382, 1375, 1379, 1470, 1424, 1543, 1480, 1575, 1533, 1578, 1646, 1591, 
    1718, 1642, 1721, 1707, 1759, 1841, 1743, 1876, 1802, 1908, 1909, 1880, 
    2037, 1946, 2031, 1988, 2010, 2147, 2022, 2147, 2070, 2201, 2117, 2171, 
    2286, 2192, 2364, 2228, 2379, 2288, 2363, 2406, 2384, 2503, 2343, 2563, 
    2402, 2524, 2550, 2521, 2657, 2503, 2699, 2535, 2692, 2702, 2661, 2812, 
    2633, 2835, 2433, 2585, 2519, 2960, 3116, 3037, 3289, 3073, 3292, 3146, 
    3259, 3310, 3176, 3417, 3196, 3352, 3238, 3279, 3327, 3183, 3402, 3130, 
    3343, 3240, 3224, 3135, 3070, 3140, 1080, 752, 1022, 688, 823, 682, 623,
    694, 475, 617, 392, 451, 397, 356, 408, 271, 388, 265, 317, 313, 268, 357, 
    236, 336, 256, 276, 307, 241, 323, 227, 323, 261, 283, 311, 246, 335,
    230, 330, 254, 307, 300, 265, 351, 257, 354, 284, 335, 357, 295, 384, 282,
    385, 319, 341, 409, 312, 416, 310, 401, 396, 378, 444, 324, 452, 331, 429,
    414, 395, 465, 345, 489, 333, 450, 456
])

N_detections_4 = np.array([   2,    2,    3,    2,    2,    3,    3,    3,    2,    2,    3,
          3,    3,    3,    4,    7,    4,    6,   13,    8,   15,   11,
         15,    9,    8,   17,   20,   16,   19,   38,   55,   50,   68,
         64,   64,   69,   65,   91,   84,   78,   61,  101,   89,   70,
         80,  120,  133,  105,   92,  161,  162,  131,  146,  224,  199,
        146,  226,  248,  216,  223,  312,  315,  247,  298, 320,  343,
        289,  383,  409,  330,  306,  390,  437,  334,  358,  474,  467,
        385,  409,  506,  408,  428,  537,  571,  464,  535,  644,  544,
        455,  604,  637,  542,  501, 1094, 1082,  943,  873, 1040, 1110,
        931,  834, 1035, 1075,  927,  898, 1058, 1029,  868,  896, 1035,
       1019,  852,  883, 1035, 1035,  902,  822,  997, 1004,  859,  823,
        974,  947,  836,  855, 1079,  999,  831,  822, 1034,  962,  830,
        824, 1036, 1020,  931,  974, 1140,  996,  839,  988, 1130, 1013,
        846, 1002, 1138,  971,  875, 1073, 1042,  871,  839, 1157, 1101,
        920,  880, 1043, 1004,  892])

N_detections_7 = np.array([   4,    4,    4,    5,    3,    6,    4,    7,    9,   10,   15,
         22,   35,   28,   28,   36,   50,   51,   64,   64,  100,   70,
        103,   98,  105,  122,  127,  116,  133,  166,  117,  141,  132,
        113,  146,  152,  138,  154,  120,  137,  141,  151,  172,  128,
        121,  145,  141,  141,  149,  116,  144,  142,  182,  140,  134,
        149,  156,  173,  137,  119,  141,  137,  138, 141])

N_detcs = [N_detections_layer, N_detections_4, N_detections_7]
mix_method = 'Spark'
dilution = '100x'
pH = ['4', '7']
x_text = [-2.5, -1]
satur_lim = [95, 25]

fig, axs = plt.subplots(1, 2, figsize=(12, 6), sharey=True)
if not isinstance(axs, np.ndarray):
    axs = np.array([axs])
for i, N_detections in enumerate(N_detcs[:1]):
    axs[i].plot(N_detections, '-o', color='tab:blue', markersize=3, alpha=0.8, label='Detections')
    rolling_average = np.convolve(N_detections, np.ones(5)/5, mode='valid')
    axs[i].plot(rolling_average, '-', color='k', label='Rolling average')
    # axs[i].axhline(y=np.mean(N_detections[satur_lim[i]:]), color='tab:orange', linestyle='--', label='Saturated mean')
    axs[i].set_xlabel('Frame index')
    if i == 0:
        axs[i].set_ylabel('Number of detected particles')
    axs[i].legend(labelcolor='k', loc='upper center', fontsize=font_size, 
                   ncol=3, bbox_to_anchor=(0.5, 1.15))
    text_x = x_text[i]
    text_y = axs[i].get_ylim()[1] * 0.93
    # axs[i].text(text_x, text_y, 'Dilution: ' + dilution + '\npH: ' + pH[i] + 
    #                     '\nMixing method: ' + mix_method,  
    #                     bbox=dict(facecolor='white', alpha=0.5, edgecolor='black'))
    axs[i].text(text_x, text_y, 'Lipid bilayer formation', 
                        bbox=dict(facecolor='white', alpha=0.5, edgecolor='black'))

plt.tight_layout()

plt.savefig('figs/detections2.pdf', bbox_inches='tight')
plt.show()
