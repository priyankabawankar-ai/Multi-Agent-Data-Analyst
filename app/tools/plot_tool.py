import matplotlib.pyplot as plt

def create_plot(df):
    try:
        df.plot()
        plt.savefig("output.png")
        return "Plot saved as output.png"
    except Exception as e:
        return str(e)