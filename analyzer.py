import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib import ticker
import seaborn as sns
import scipy.stats as stats

# LaTeX font
plt.style.use('default')
plt.rc('text', usetex = True)
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'serif'
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
font_size = 12
plt.rcParams['font.size'] = font_size

# Load the data
data_folder = 'labb2/'
save = False

# Seaborn style
sns.set_style('whitegrid', {'axes.facecolor': '0.95'})

def plotter(axis, data, fit, hist_color='tab:orange', fit_color='tab:blue'):
    axis.hist(data, bins=60, histtype='bar', color=hist_color, edgecolor='black', label='Data')
    max_counts = np.histogram(data, bins=60)[0].max()
    x = np.linspace(data.min(), data.max(), 1000)
    log_pdf = stats.lognorm.pdf(x, fit[0], fit[1], fit[2])
    pdf_max = log_pdf.max()
    log_pdf = log_pdf * max_counts / pdf_max
    axis.plot(x, log_pdf, color=fit_color, linestyle='-', lw=2.5, label='Log-normal fit')
    axis.vlines(x=fit[2], ymin=0, 
                ymax=stats.lognorm.pdf(fit[2], fit[0], fit[1], fit[2]) * max_counts / pdf_max, 
                color='salmon', linestyle='-', lw=2.5, label='Fit mean')
    
    fit_mean = stats.lognorm.mean(fit[0], fit[1], fit[2])
    fit_std = stats.lognorm.std(fit[0], fit[1], fit[2])
    fit_median = stats.lognorm.median(fit[0], fit[1], fit[2])

    return fit_mean, fit_std, fit_median

def plot_custom(axis, sub_folder, font_size=font_size):
    axis.minorticks_on()
    axis.xaxis.set_minor_locator(ticker.AutoMinorLocator(2))
    axis.yaxis.set_minor_locator(ticker.AutoMinorLocator(2))
    axis.tick_params(axis='x', labelsize=font_size)
    axis.tick_params(axis='y', labelsize=font_size)
    axis.tick_params(axis='both', direction='in', length=5, width=1.5, colors='black')
    axis.tick_params(axis='both', which='minor', direction='in', length=3, width=1, colors='black')

    axis.set_xlabel('Particle size (nm)')
    axis.set_ylabel('Counts')

    axis.legend(labelcolor='k', loc='upper center', fontsize=font_size, 
                ncol=3, bbox_to_anchor=(0.5, 1.15))
    # axis.set_title('$\\textbf{Particle size distribution}$')
    axis.set_xlim(0, 500)

    dilution, stab, pH, mix_method = exp_info(sub_folder)
    text_x = axis.get_xlim()[1] * 0.63
    text_y = axis.get_ylim()[1] * 0.8
    axis.text(text_x, text_y, 'Dilution: ' + dilution + '\nStabilizer: ' + 
                        stab + '\npH: ' + pH + '\nMixing method: ' + mix_method,  
                        bbox=dict(facecolor='white', alpha=0.5, edgecolor='black'))

def exp_info(sub_folder):
    dilution = sub_folder.split('_')[0]
    stab = sub_folder.split('_')[1]
    if stab == 'L':
        stab = 'Low'
    else:
        stab = 'High'
    pH = sub_folder.split('_')[2]
    mix_method = sub_folder.split('_')[3]
    if mix_method == '1':
        mix_method = 'Manual'
    elif mix_method == '2':
        mix_method = 'Vortex'
    else:
        mix_method = 'Spark '

    return dilution, stab, pH, mix_method

stds, means, medians, indices = [], [], [], []
for sub_folder in os.listdir(data_folder):
    if sub_folder.endswith('real'):
        plt.figure(figsize=(6, 5))
        ax = plt.subplot()
        sizes = np.array([])
        # diff_coeff_list = []
        for file in os.listdir(data_folder + sub_folder):
            if file.endswith('ParticleData.csv'):
                data_df = pd.read_csv(data_folder + sub_folder + '/' + file)
                # Filter by 'Included in distribution' == True
                data_df = data_df[data_df['Included in distribution?']]
                sizes = np.hstack((sizes, np.array(data_df['Size/nm'].values)))
                # diff_coeff_list.append(list(data_df['Diffusion coefficient/nm^2 s^-1']))

        fit = stats.lognorm.fit(sizes) 
        fit_mean, fit_std, fit_median = plotter(ax, sizes, fit, fit_color='k', hist_color='dodgerblue')
        plot_custom(ax, sub_folder)

        stds.append(fit_std)
        means.append(fit_mean)
        medians.append(fit_median)
        indices.append(sub_folder)

        if save:
            plt.savefig('figs/' + sub_folder + '.pdf', bbox_inches='tight')

df = pd.DataFrame({'std': stds, 'mean': means, 'median': medians}, index=indices)
print(df)

plt.show()

print('nejnejdå')