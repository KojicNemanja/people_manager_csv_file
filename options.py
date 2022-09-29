
def title():
    print("[0] Informations")

def show_options():
    options = "[1] All, [2] Add, [3] Edit, [4] Delete, [5] Search\n[q] Exit"
    print(options)
    """
    print("[1] All")
    print("[2] Add")
    print("[3] Edit")
    print("[4] Delete")
    print("[5] Search")
    print("[q] Exit")"""

def get_answer()->str:
    return input("Answer -> ").strip().casefold()
