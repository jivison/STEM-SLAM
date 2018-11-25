class Themes():

    # Add custom themes here:
    sunset = ["#fffa00", '#ff8c00', '#ff270f', 'coral']
    cyan = ['cyan', 'darkcyan', 'white']
    forest = ['green', '#aaff00', '#00ff87']
    vaporwave = ['cyan', 'darkcyan', 'white', 'hotpink', 'violet', 'pink']
    purple = ['magenta', 'violet', 'indigo', 'purple', 'hotpink']


    # Don't add anything past this

    def __init__(self):
        pass
    
    def __call__(self, theme):
        try:
            return getattr(self, theme)
        except Exception:
            pass