import taipy as tp

if __name__ == "__main__":
    gui = tp.Gui(page="# Getting started with *Taipy*")

    tp.run(gui, title="Taipy application")  # It is equivalent to gui.run(title="Taipy application")