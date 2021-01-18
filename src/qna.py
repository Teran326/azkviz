import pickle

qna = [
    ["Správce informačního systému.", "Administrátor"],
    ["Jak nazýváme prefix a sufix v češtině?", "předpona a přípona"],
    ["Tento hlodavec žije v lese na stromech?", "veverka obecná"],
    ["Původní celé jméno Lenina?", "Vladimír Iljič Uljanov"],
    ["Hlavní město Šalamounových ostrovů?", "Honiara"],
    ["Nejvyšší pevný bod ČR?", "vrchol vysílače Praděd"],
    ["Zkratka Československa před rozpadem?", "ČSFR"],
    ["Místo podepsání kapitulace Japonska?", "Bitevní loď Missouri, Tokijský záliv"],
    ["Nejmenší stát na světě?", "Vatikán"],
    ["Zastaralý český název pro Cl?", "Kostík"],
]

pickle.dump(qna, open("qna.dat", "wb"))