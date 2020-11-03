import os

def deleter(path):
    """ Odstraní všechny soubory v adresáři (output) """

    # * Počet smazaných souborů
    num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
    
    for f in os.listdir(path):
        print("- odstraněno - ", f)
        os.remove(os.path.join(path, f))

    print("--- Odstranění dokončeno [", num_files, "] ---")

