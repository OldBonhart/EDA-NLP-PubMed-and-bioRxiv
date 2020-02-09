from PIL import Image
import numpy as np
import random

import matplotlib.pyplot as plt
from matplotlib import cm
import seaborn as sns

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors

import os
import tempfile
import imageio
import shutil

# set theme
sns.set_context("poster", font_scale=0.8, rc={"lines.linewidth": 1.1})

def get_color():
    color = random.choice(["mediumspringgreen",
                           "cyan",
                           "darkcyan",
                           "mediumvioletred",
                           "seagreen",
                           "purple",
                           "darkmagenta"])
    return color


def tsne_plot_2d(filename, label, embeddings, words=[], a=1, color=get_color()):
    sns.set_context("poster", font_scale=0.8, rc={"lines.linewidth": 1.1})
    plt.figure(figsize=(16, 9))
    colors = cm.rainbow(np.linspace(0, 1, 1))
    x = embeddings[:,0]
    y = embeddings[:,1]
    plt.scatter(x, y, c=color, alpha=a, label=label)
    for i, word in enumerate(words):
        plt.annotate(word, alpha=0.3, xy=(x[i], y[i]), xytext=(5, 2), 
                     textcoords='offset points', ha='right', va='bottom', size=10)
    plt.legend(loc="best")
    plt.grid(True)
    plt.savefig(f"{filename}.png", format='png', dpi=150, bbox_inches='tight')
    plt.axis("off")
    plt.close()
    



def tsne_plot_3d_gif(title,
                     label,
                     embeddings,
                     c=get_color(),
                     filename="3d.gif",
                     a=0.4):
    sns.set_context("poster", font_scale=0.5, rc={"lines.linewidth": 0.4})
    fig = plt.figure(figsize=(15,10))
    ax = Axes3D(fig)

    a = plt.scatter(embeddings[:, 0], embeddings[:, 1], embeddings[:, 2], c=c, alpha=a)

    plt.title(title, fontsize=18)

    red_patch = mpatches.Patch(color=c, label=label)
    plt.legend(handles=[red_patch], loc=3, fontsize=15)

    dirpath = tempfile.mkdtemp()
    images = []
    for angle in range(0, 360, 5):
        ax.view_init(30, angle)
        fname = os.path.join(dirpath, str(angle) + '.png')
        plt.savefig(fname, dpi=120, format='png', bbox_inches='tight')
        images.append(imageio.imread(fname))
    imageio.mimsave(filename, images)
    shutil.rmtree(dirpath)
    plt.close()
    
def tsne_plot_similar_words(title,
                            labels,
                            embedding_clusters,
                            word_clusters,
                            a,
                            filename):
    sns.set_context("poster", font_scale=0.5, rc={"lines.linewidth": 0.7})
    plt.figure(figsize=(20, 15))
    colors = random.choices(list(mcolors.CSS4_COLORS.keys()),k=len(labels))
    idx_color = 0
    for label, embeddings, words, color in zip(labels, embedding_clusters, word_clusters, colors):

        x = embeddings[:, 0]
        y = embeddings[:, 1]

        plt.scatter(x, y, c=colors[idx_color], alpha=a, label=label)
        for i, word in enumerate(words):
            plt.annotate(word, alpha=0.5, xy=(x[i], y[i]), xytext=(5, 2),
                         textcoords='offset points', ha='right', va='bottom', size=8)
        idx_color += 1

    plt.legend(loc=4, fontsize=12)
    plt.title(title, fontsize=15)
    plt.grid(True)
    plt.axis("off")
    if filename:
        plt.savefig(f"{filename}.png", format='png', dpi=150, bbox_inches='tight')
    plt.close()
    
    
def get_mask(img_path):
    img = Image.open(img_path).convert("L")
    return np.array(img)