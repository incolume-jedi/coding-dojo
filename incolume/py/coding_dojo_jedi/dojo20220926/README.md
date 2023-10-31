# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

---

## Problema

**RNA to Protein Sequence Translation**

O dogma central da biologia molecular é que o DNA é transcrito em RNA, que é então traduzido em proteína. O RNA, como o DNA, é uma longa fita de ácidos nucléicos mantidos juntos por um esqueleto de açúcar (ribose neste caso). Cada segmento de três bases é chamado de códon . Máquinas moleculares chamadas ribossomos traduzem os códons de RNA em cadeias de aminoácidos, chamadas polipeptídeos, que são então dobradas em uma proteína.

As sequências de proteínas são facilmente visualizadas da mesma forma que o DNA e o RNA, como grandes sequências de letras. Uma coisa importante a notar é que os códons 'Stop' não codificam um aminoácido específico. Sua única função é interromper a tradução da proteína, pois não são incorporadas à cadeia polipeptídica. Os códons 'Stop' não devem estar na sequência final da proteína. Para poupar um monte de digitação desnecessária (e chata) as chaves e valores para o seu dicionário de aminoácidos são fornecidos.

Dada uma sequência de RNA, crie uma função que traduza o RNA em sua sequência de proteínas. Nota: os casos de teste sempre produzirão uma string válida.

```bash
protein('UGCGAUGAAUGGGCUCGCUCC') returns 'CDEWARS'
```

Incluído como casos de teste está um exemplo do mundo real! O último caso de teste de exemplo codifica uma proteína chamada proteína fluorescente verde; uma vez inseridas no genoma de outro organismo, proteínas como a GFP permitem que os biólogos visualizem os processos celulares!

Dicionário de aminoácidos
```bash
    # Phenylalanine
    'UUC':'F', 'UUU':'F',
    # Leucine
    'UUA':'L', 'UUG':'L', 'CUU':'L', 'CUC':'L','CUA':'L','CUG':'L',
    # Isoleucine
    'AUU':'I', 'AUC':'I', 'AUA':'I',
    # Methionine
    'AUG':'M',
    # Valine
    'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
    # Serine
    'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S', 'AGU':'S', 'AGC':'S',
    # Proline
    'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    # Threonine
    'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    # Alanine
    'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    # Tyrosine
    'UAU':'Y', 'UAC':'Y',
    # Histidine
    'CAU':'H', 'CAC':'H',
    # Glutamine
    'CAA':'Q', 'CAG':'Q',
    # Asparagine
    'AAU':'N', 'AAC':'N',
    # Lysine
    'AAA':'K', 'AAG':'K',
    # Aspartic Acid
    'GAU':'D', 'GAC':'D',
    # Glutamic Acid
    'GAA':'E', 'GAG':'E',
    # Cystine
    'UGU':'C', 'UGC':'C',
    # Tryptophan
    'UGG':'W',
    # Arginine
    'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    # Glycine
    'GGU':'G',  'GGC':'G', 'GGA':'G', 'GGG':'G',
    # Stop codon
    'UAA':'Stop', 'UGA':'Stop', 'UAG':'Stop'
```

## Exemplos
```
protein('AUG'), 'M'
protein('AUGUGA'), 'M'
protein('AUGGUUAGUUGA'), 'MVS'
protein('UGCGAUGAAUGGGCUCGCUCC'), 'CDEWARS'
protein('AUGUCCUUCCAUCAAGGAAACCAUGCGCGUUCAGCUUUCUGA'), 'MSFHQGNHARSAF'
protein('AUGCUUCAAGUGCACUGGAAAAGGAGAGGGAAAACCAGUUGA'), 'MLQVHWKRRGKTS'
protein('AUGGCGUUCAGCUUUCUAUGGAGGGUAGUGUACCCAUGCUGA'), 'MAFSFLWRVVYPC'
protein('AUGCAGCUUUCUAUGGAGGGUAGUGUUAACUACCACGCCUGA'), 'MQLSMEGSVNYHA'
protein('AUGCUAUGGAGGGUAGUGUUAACUACCACGCCCAGUACUUGA'), 'MLWRVVLTTTPST'
protein('AUGUAUCCUUCCAUCAAGGAAACCAUGCGCGUUCAGCUUUCUAUGGAGGGUAGUGUUAACUACCACGCCUUCAAGUGCACUGGAAAAGGAGAGGGAAAACCAUACGAAGGCACCCAAAGCCUGAAUAUUACAAUAACUGAAGGAGGUCCUCUGCCAUUUGCUUUUGACAUUCUGUCACACGCCUUUCAGUAUGGCAUCAAGGUCUUCGCCAAGUACCCCAAAGAAAUUCCUGACUUCUUUAAGCAGUCUCUACCUGGUGGUUUUUCUUGGGAAAGAGUAAGCACCUAUGAAGAUGGAGGAGUGCUUUCAGCUACCCAAGAAACAAGUUUGCAGGGUGAUUGCAUCAUCUGCAAAGUUAAAGUCCUUGGCACCAAUUUUCCCGCAAACGGUCCAGUGAUGCAAAAGAAGACCUGUGGAUGGGAGCCAUCAACUGAAACAGUCAUCCCACGAGAUGGUGGACUUCUGCUUCGCGAUACCCCCGCACUUAUGCUGGCUGACGGAGGUCAUCUUUCUUGCUUCAUGGAAACAACUUACAAGUCGAAGAAAGAGGUAAAGCUUCCAGAACUUCACUUUCAUCAUUUGCGUAUGGAAAAGCUGAACAUAAGUGACGAUUGGAAGACCGUUGAGCAGCACGAGUCUGUGGUGGCUAGCUACUCCCAAGUGCCUUCGAAAUUAGGACAUAACUGA'), 'MYPSIKETMRVQLSMEGSVNYHAFKCTGKGEGKPYEGTQSLNITITEGGPLPFAFDILSHAFQYGIKVFAKYPKEIPDFFKQSLPGGFSWERVSTYEDGGVLSATQETSLQGDCIICKVKVLGTNFPANGPVMQKKTCGWEPSTETVIPRDGGLLLRDTPALMLADGGHLSCFMETTYKSKKEVKLPELHFHHLRMEKLNISDDWKTVEQHESVVASYSQVPSKLGHN', 'This gene encodes for a protein that fluoresces green in the Snakelocks anemone!')
```

## Artefatos

- [dojo](./dojo20220926.py)
- [test](./test_20220926.py)

## Referências

N/A.
