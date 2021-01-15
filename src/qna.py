import pickle

qna = [
    ["Výraz na -á označující správce informačního systému, který má neomezená užívací práva. Jak se funkci říká?", "Administrátor"],
    ["Jak nazýváme prefix a sufix v češtině?", "předpona a přípona"],
    ["Tento hlodavec žije v lese, kde šplhá po stromech a dokáže skákat ze stromu na strom i na několik metrů. Jak jej nazýváme písmeny na VO?", "veverka obecná"],
    ["Jak se původně jmenoval celým jménem Lenin?", "Vladimír Iljič Uljanov"],
    ["Hlavní město Šalamounových ostrovů?", "Honiara"],
    ["Nejvyšší pevný bod ČR?", "vrchol vysílače Praděd"],
    ["Jaký byl název Československa před rozpadem v roce 1993?", "Česká a Slovenská federatvní republika"],
    ["Kde byla podepsána kapitulace Japonska 2. září 1945?", "Paluba bitevní lodi Missouri v Tokijském zálivu"],
    ["Nejmenší stát na světě?", "Vatikán"],
    ["Zastaralý český název pro Cl?", "Kostík"],
]

pickle.dump(qna, open("qna.dat", "wb"))