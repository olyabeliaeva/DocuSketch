from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from pandas import DataFrame


# this class:
# 1)draws plot for comparing different columns
# 2)saves plots in a folder called “plots”
# 3)returns paths to all plots

class Drawer:

    @staticmethod
    def draw_plot(df: DataFrame, x: str, y_s: [str], name_file: str):
        plot = df.plot(x=x, y=y_s)
        plt.title(f'Plot room indexes to {"-".join(y_s)}')
        fig: Figure = plot.get_figure()
        return Drawer.save_plot(fig, name_file)

    @staticmethod
    def save_plot(fig: Figure, name_file: str):
        path = Path("plots", name_file)
        fig.savefig(path)
        plt.show()
        return str(path)

    @staticmethod
    def draw_plots(df: DataFrame, xsys: [{str: [str]}]):
        paths = []
        for xys in xsys:
            for x, ys in xys.items():
                paths.append(Drawer.draw_plot(df, x, ys, f'{"-".join(ys)}.png'))
        return paths
