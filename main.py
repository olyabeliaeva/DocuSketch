from docu import Drawer
from jsonutils import JsonUtils

if __name__ == '__main__':
    dataframe = JsonUtils.read_json('https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json')

    xsys = [
        {
            'index': ['min', 'floor_min', 'ceiling_min']
        },
        {
            'index': ['max', 'floor_max', 'ceiling_min']
        },
        {
            'index': ['mean', 'floor_mean', 'ceiling_mean']
        },
        {
            'index': ['delta_corners']
        }

    ]

    print(Drawer.draw_plots(dataframe, xsys))
