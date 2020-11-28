import os
import numpy as np
from pymol import *
import rdkit


def FindComStr(mols):
    res=rdFMCS.FindMCS(mols,bondCompare=rdFMCS.BondCompare.CompareAny).smartsString
    res=Chem.MolFromSmarts(res)
    return res

def addFig(fig, sub_fig, num_cols=4):
    """
    :param fig: object, a main figure object in bigger size
    :param sub_fig: object, a figure object in smaller size
    :param num_cols: int, number of sub figures per row in the main figure
    :return:
    """
    width = 2
    height = 2
    offset = height * 0.02
    num_exist = len(fig.axes)
    row_loc = num_exist // num_cols
    col_loc = num_exist % num_cols
    # print(row_loc, col_loc)
    left = col_loc * width + offset
    bottom = row_loc * height + offset
    ax = sub_fig.gca()
    ax.set_xticks([])
    ax.set_yticks([])
    ax.remove()
    ax.figure = fig
    fig.add_axes(ax)
    if (num_exist > 0) and (bottom > offset) and (left == offset):
        ax_bottom = fig.axes[-2]
        bottom_bounds = list(ax_bottom.get_position().bounds)
        bottom_bounds[0] = left
        ax.set_position(bottom_bounds)
        for i, ax_tmp in enumerate(fig.axes[:-1]):
            if i // num_cols == row_loc:
                pass
            else:
                bounds = list(ax_tmp.get_position().bounds)
                bounds[1] += height
                ax_tmp.set_position(bounds)
    else:
        ax.set_position([left, offset, width, height])
    plt.close(sub_fig)

    return fig

def drawMols(mols, saved_dir, legends=None, num_cols=5, batch_size=200, saved_format="svg", file_prefix=''):

    Draw.DrawingOptions.atomLabelFontSize = 12
    Draw.DrawingOptions.atomLabelMinFontSize = 5

    # batch_size = 12
    batch_num = math.ceil(len(mols) / batch_size)
    if legends == None:
        legends = ["mol_{}".format(i + 1) for i in range(len(mols))]
#       legends = ['E'+str(number[i])+'\n'+str(IC50[i])+'\n'+dockname[i] for i in range(len(mols))]
    for b in range(batch_num):
        plt.clf()
        fig = plt.figure()
        sub_mols = mols[b * batch_size:(b + 1) * batch_size]
        sub_legends = list(legends)[b * batch_size:(b + 1) * batch_size]

        for i, m in enumerate(sub_mols):
            if m.HasSubstructMatch(template1):
               Atomlist = m.GetSubstructMatch(template1)
               sub_fig = Draw.MolToMPL(m, coordScale=1.0, size=(170,170), highlightAtoms=Atomlist)
               ax = sub_fig.axes[0]
               ax.text(ax.get_xlim()[1] * 0.5, ax.get_ylim()[1] * 0.2, sub_legends[i], va="center", ha="center",
               fontdict={"size": 12, "weight":"semibold", "color":"black"})
               fig = addFig(fig, sub_fig, num_cols=num_cols)
#           elif m.HasSubstructMatch(template2):
#               Atomlist = m.GetSubstructMatch(template2)
#               sub_fig = Draw.MolToMPL(m, coordScale=1.0, size=(170,170), highlightAtoms=Atomlist)
#               ax = sub_fig.axes[0]
#               ax.text(ax.get_xlim()[1] * 0.5, ax.get_ylim()[1] * 0.2, sub_legends[i], va="center", ha="center",
#               fontdict={"size": 12, "weight":"semibold", "color":"black"})
#              fig = addFig(fig, sub_fig, num_cols=num_cols)
            else:
               Atomlist = ()
               sub_fig = Draw.MolToMPL(m, coordScale=1.0, size=(170,170), highlightAtoms=Atomlist)
               ax = sub_fig.axes[0]
               ax.text(ax.get_xlim()[1] * 0.5, ax.get_ylim()[1] * 0.2, sub_legends[i], va="center", ha="center",
               fontdict={"size": 12, "weight":"semibold", "color":"black"})
               fig = addFig(fig, sub_fig, num_cols=num_cols) 
        
            
        t = time.localtime()
        tm_str = "{:02d}{:02d}{:02d}{:02d}".format(t.tm_mon, t.tm_mday, t.tm_hour, t.tm_sec)
        if file_prefix:
            fig_file = os.path.join(saved_dir, 'batch_{}_Num_{}_{}.{}'.format(b+1,b * batch_size+1,(b + 1) * batch_size, saved_format))
        else:
            fig_file = os.path.join(saved_dir, 'batch_{}_Num_{}_{}.{}'.format(b+1,b * batch_size+1,(b + 1) * batch_size, saved_format))
        print("Saved fig: ", fig_file)
        fig.savefig(fig_file, dpi=300, bbox_inches='tight')
        plt.close(fig)
