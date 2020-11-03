import os
import pandas as pd
from datetime import date

def xlsx_to_csv(in_path, out_path):
    """Soubory s příponou (.xlsx) v adresáři (input) konvertuje na (.csv) do adresáře (output). """

    for file in os.listdir(in_path):
        if file.endswith(".xlsx"):
            read_file = pd.read_excel(in_path + file)
            file_name = os.path.splitext(file)[0] # odstranění přípony xlsx (pro správné pojmenování nového souboru)
            read_file.to_csv(out_path + str(date.today()) + "_" + file_name + ".csv", index=None, header=True)
            print(file_name)
        else:
            print("(" + file + ")")
    
    # * Počet vyexportovaných souborů 
    num_files = len([f for f in os.listdir(out_path)if os.path.isfile(os.path.join(out_path, f))])


    print("--- Konvertování dokončeno [", num_files, "] ---")


