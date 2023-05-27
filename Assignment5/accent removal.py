def remove_accents(text):
    accents = {
        'a': ['à', 'á', 'â', 'ã', 'ä', 'å', 'æ'],
        'c': ['ç'],
        'e': ['è', 'é', 'ê', 'ë', 'æ'],
        'i': ['ì', 'í', 'î', 'ï'],
        'n': ['ñ'],
        'o': ['ò', 'ó', 'ô', 'õ', 'ö', 'ø'],
        's': ['ß'],
        'u': ['ù', 'ú', 'û', 'ü'],
        'y': ['ÿ'],
    }

    for character, accents_list in accents.items():
        for accent in accents_list:
            text = text.replace(accent, character)

    return text

def main():
    text = "La 16e Japan Expo (2-5 juillet), où 250 000 visiteurs sont attendus, le confirme : la France est — aussi — un pays de mangas. Plus de 1 500 titres sont publiés chaque année dans l’Hexagone, soit autant que les albums franco-belges. La très grande majorité de ces recueils au format poche est composée de titres préalablement parus au Japon dont les droits ont été achetés. Une sujétion au made in Japan inéluctable ? Pas si sûr, car une tendance s’amorce chez les éditeurs français : la création ex nihilo de séries, commandées directement auprès d’auteurs nippons."

    text_ascii = remove_accents(text)
    print(text_ascii)

if __name__ == '__main__':
    main()
