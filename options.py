
def title():
    print("[0] Informations")

def show_options():
    options = "[1] All, [2] Add, [3] Edit, [4] Delete, [5] Search\n[q] Exit"
    print(options)

def get_answer()->str:
    return input("Answer -> ").strip().casefold()
