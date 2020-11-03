from deleter import deleter
from convertor import xlsx_to_csv

# TODO: Načti původní XLSX a převeď do CSV
# TODO: Vytvoř slovník z hlavičky [0] a prvního řádku [1]

# ? Cesty k adresářům:
in_path = "input/"
out_path = "output/"

# * Smazání starých dat v outputu:
deleter(out_path)

# * Konvertace dat z xlsx » csv:
xlsx_to_csv(in_path, out_path)



