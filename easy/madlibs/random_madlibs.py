from sample_madlibs import hp, code, zombie, hungergames
import random

if __name__ == "__main__":
    modules = [hp, code, zombie, hungergames]
    rand_module_selected = random.choice(modules)
    rand_module_selected.madlib()
