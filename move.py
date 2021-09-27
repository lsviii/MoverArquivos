import os

listaDeArquivos = os.listdir("Mover")

for arquivo in listaDeArquivos:
    if ".xlsx" in arquivo:
        if "Jan" in arquivo:
            os.rename(f"Mover/{arquivo}", f"Mover/Jan/{arquivo}")
        if "Fev" in arquivo:
           os.rename(f"Mover/{arquivo}", f"Mover/Fev/{arquivo}")
        if "Mar" in arquivo:
            os.rename(f"Mover/{arquivo}", f"Mover/Mar/{arquivo}")