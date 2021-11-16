import os
from documents import Documents
from inverted_index import InvertedIndex

def main():
    filenames = os.listdir("res/")
    documents_list = list()

    if os.path.exists("inv_file.data"):
        i = InvertedIndex()
    else:
        for f in filenames:
            d = Documents(f"res/{f}")
            documents_list.append(d)

        i = InvertedIndex(documents_list)

    print(i.inverted_index)
    print("----------------")
    print("Resultado da busca: ", i.find("internet"))
    print("Resultado da busca: ", i.find("direito"))

if __name__ == "__main__":
    main()
