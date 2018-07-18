# encoding: utf8
from __future__ import unicode_literals


# improved list from Stone, Denis, Kwantes (2010)
STOP_WORDS = set("""
a about above across after afterwards again against all almost alone
along already also although always am among amongst amoungst amount
an and another any anyhow anyone anything anyway anywhere are around
as at back be became because become becomes becoming been before
beforehand behind being below beside besides between beyond bill
both bottom but by call can cannot cant co computer con could couldnt
cry de describe detail did didn do does doesn doing don done down due
during each eg eight either eleven else elsewhere empty enough etc
even ever every everyone everything everywhere except few fifteen
fify fill find fire first five for former formerly forty found four
from front full further get give go had has hasnt have he hence her
here hereafter hereby herein hereupon hers herself him himself his
how however hundred i ie if in inc indeed interest into is it its
itself keep last latter latterly least less ltd just kg km made make
many may me meanwhile might mill mine more moreover most mostly move
much must my myself name namely neither never nevertheless next nine
no nobody none noone nor not nothing now nowhere of off often on once
one only onto or other others otherwise our ours ourselves out over
own part per perhaps please put rather re quite rather really regarding
same say see seem seemed seeming seems serious several she should
show side  since sincere six sixty so some somehow someone something
sometime sometimes somewhere still such system take ten than that the
their them themselves then thence there thereafter thereby therefore
therein thereupon these they thick thin third this those though three
through throughout thru thus to together too top toward towards twelve
twenty two un under until up unless upon us used using various very
very via was we well were what whatever when whence whenever where whereafter
whereas whereby wherein whereupon wherever whether which while whither
who whoever whole whom whose why will with within without would yet you
your yours yourself yourselves
""".split())


TAG_MAP = {
    ".": {"pos": "punct", "puncttype": "peri"},
    ",": {"pos": "punct", "puncttype": "comm"},
    "-LRB-": {"pos": "punct", "puncttype": "brck", "punctside": "ini"},
    "-RRB-": {"pos": "punct", "puncttype": "brck", "punctside": "fin"},
    "``": {"pos": "punct", "puncttype": "quot", "punctside": "ini"},
    "\"\"": {"pos": "punct", "puncttype": "quot", "punctside": "fin"},
    "''": {"pos": "punct", "puncttype": "quot", "punctside": "fin"},
    ":": {"pos": "punct"},
    "$": {"pos": "sym", "other": {"symtype": "currency"}},
    "#": {"pos": "sym", "other": {"symtype": "numbersign"}},
    "AFX": {"pos": "adj",  "hyph": "hyph"},
    "CC": {"pos": "conj", "conjtype": "coor"},
    "CD": {"pos": "num", "numtype": "card"},
    "DT": {"pos": "det"},
    "EX": {"pos": "adv", "advtype": "ex"},
    "FW": {"pos": "x", "foreign": "foreign"},
    "HYPH": {"pos": "punct", "puncttype": "dash"},
    "IN": {"pos": "adp"},
    "JJ": {"pos": "adj", "degree": "pos"},
    "JJR": {"pos": "adj", "degree": "comp"},
    "JJS": {"pos": "adj", "degree": "sup"},
    "LS": {"pos": "punct", "numtype": "ord"},
    "MD": {"pos": "verb", "verbtype": "mod"},
    "NIL": {"pos": ""},
    "NN": {"pos": "noun", "number": "sing"},
    "NNP": {"pos": "propn", "nountype": "prop", "number": "sing"},
    "NNPS": {"pos": "propn", "nountype": "prop", "number": "plur"},
    "NNS": {"pos": "noun", "number": "plur"},
    "PDT": {"pos": "adj", "adjtype": "pdt", "prontype": "prn"},
    "POS": {"pos": "part", "poss": "poss"},
    "PRP": {"pos": "pron", "prontype": "prs"},
    "PRP$": {"pos": "adj", "prontype": "prs", "poss": "poss"},
    "RB": {"pos": "adv", "degree": "pos"},
    "RBR": {"pos": "adv", "degree": "comp"},
    "RBS": {"pos": "adv", "degree": "sup"},
    "RP": {"pos": "part"},
    "SYM": {"pos": "sym"},
    "TO": {"pos": "part", "parttype": "inf", "verbform": "inf"},
    "UH": {"pos": "intJ"},
    "VB": {"pos": "verb", "verbform": "inf"},
    "VBD": {"pos": "verb", "verbform": "fin", "tense": "past"},
    "VBG": {"pos": "verb", "verbform": "part", "tense": "pres", "aspect": "prog"},
    "VBN": {"pos": "verb", "verbform": "part", "tense": "past", "aspect": "perf"},
    "VBP": {"pos": "verb", "verbform": "fin", "tense": "pres"},
    "VBZ": {"pos": "verb", "verbform": "fin", "tense": "pres", "number": "sing", "person": 3},
    "WDT": {"pos": "adj", "prontype": "int|rel"},
    "WP": {"pos": "noun", "prontype": "int|rel"},
    "WP$": {"pos": "adj", "poss": "poss", "prontype": "int|rel"},
    "WRB": {"pos": "adv", "prontype": "int|rel"},
    "SP": {"pos": "space"},
    "ADD": {"pos": "x"},
    "NFP": {"pos": "punct"},
    "GW": {"pos": "x"},
    "AFX": {"pos": "x"},
    "HYPH": {"pos": "punct"},
    "XX": {"pos": "x"},
    "BES": {"pos": "verb"},
    "HVS": {"pos": "verb"}
}

TOKENIZER_PREFIXES = r''', " ( [ { * < $ £ “ ' `` ` # US$ C$ A$ a- ‘ .... ...'''.split()


TOKENIZER_SUFFIXES = (r''', \" \) \] \} \* \! \? % \$ > : ; ' ” '' 's 'S ’s ’S ’'''
                      r'''\.\. \.\.\. \.\.\.\. (?<=[a-z0-9)\]”"'%\)])\. '''
                      r'''(?<=[0-9])km''').strip().split()


TOKENIZER_INFIXES = (r'''\.\.\.+ (?<=[a-z])\.(?=[A-Z]) (?<=[a-zA-Z])-(?=[a-zA-z]) '''
                     r'''(?<=[a-zA-Z])--(?=[a-zA-z]) (?<=[0-9])-(?=[0-9]) '''
                     r'''(?<=[A-Za-z]),(?=[A-Za-z])''').split()


TOKENIZER_EXCEPTIONS = {
  "and/or": [
      {
          "F": "and/or",
          "L": "and/or",
          "pos": "CC"
        }],
  "Ph.D.": [
    {
        "F": "Ph.D."
    }],
  "d.": [
    {
      "F": "d."
    }
  ],
  "Theydve": [
    {
      "L": "-PRON-",
      "F": "They"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  ":/": [
    {
      "F": ":/"
    }
  ],
  "shouldn't've": [
    {
      "F": "should"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "There'll": [
    {
      "F": "There"
    },
    {
      "F": "'ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "E.G.": [
    {
      "F": "E.G."
    }
  ],
  "howll": [
    {
      "F": "how"
    },
    {
      "F": "ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "6a.m.": [
    {
      "F": "6"
    },
    {
      "F": "a.m."
    }
  ],
  "Ore.": [
    {
      "F": "Ore."
    }
  ],
  "Hadn't've": [
    {
      "F": "Had",
      "L": "have",
      "pos": "VBD"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  ":>": [
    {
      "F": ":>"
    }
  ],
  "3p.m.": [
    {
      "F": "3"
    },
    {
      "F": "p.m."
    }
  ],
  "who'll": [
    {
      "F": "who"
    },
    {
      "F": "'ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "5a.m.": [
    {
      "F": "5"
    },
    {
      "F": "a.m."
    }
  ],
  ":(": [
    {
      "F": ":("
    }
  ],
  ":0": [
    {
      "F": ":0"
    }
  ],
  "10a.m.": [
    {
      "F": "10"
    },
    {
      "F": "a.m."
    }
  ],
  "aint": [
    {
      "F": "ai",
      "pos": "VBP",
      "number": 2,
      "L": "be"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  " ": [
    {
      "pos": "SP",
      "F": " "
    }
  ],
  "Dec.": [
    {
      "F": "Dec."
    }
  ],
  "Shouldnt": [
    {
      "F": "Should"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Ky.": [
    {
      "F": "Ky."
    }
  ],
  "when's": [
    {
      "F": "when"
    },
    {
      "F": "'s"
    }
  ],
  "Didnt": [
    {
      "F": "Did",
      "L": "do",
      "pos": "VBD"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "itll": [
    {
      "L": "-PRON-",
      "F": "it"
    },
    {
      "F": "ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "Who're": [
    {
      "F": "Who"
    },
    {
      "F": "'re"
    }
  ],
  "=D": [
    {
      "F": "=D"
    }
  ],
  "Ain't": [
    {
      "F": "Ai",
      "pos": "VBP",
      "number": 2,
      "L": "be"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Can't": [
    {
      "F": "Ca",
      "L": "can",
      "pos": "MD"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Whyre": [
    {
      "F": "Why"
    },
    {
      "F": "re"
    }
  ],
  "Aren't": [
    {
      "F": "Are",
      "pos": "VBP",
      "number": 2,
      "L": "be"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Neednt": [
    {
      "F": "Need"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "should've": [
    {
      "F": "should"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "shouldn't": [
    {
      "F": "should"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Idve": [
    {
      "L": "-PRON-",
      "F": "I"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "weve": [
    {
      "F": "we"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Va.": [
    {
      "F": "Va."
    }
  ],
  "D.C.": [
    {
      "F": "D.C."
    }
  ],
  "3am": [
    {
      "F": "3"
    },
    {
      "L": "a.m.",
      "F": "am"
    }
  ],
  "Ive": [
    {
      "L": "-PRON-",
      "F": "I"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Md.": [
    {
      "F": "Md."
    }
  ],
  ";D": [
    {
      "F": ";D"
    }
  ],
  "Mrs.": [
    {
      "F": "Mrs."
    }
  ],
  "Minn.": [
    {
      "F": "Minn."
    }
  ],
  "they'd": [
    {
      "L": "-PRON-",
      "F": "they"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "Youdve": [
    {
      "L": "-PRON-",
      "F": "You"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "theyve": [
    {
      "L": "-PRON-",
      "F": "they"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Weren't": [
    {
      "F": "Were"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "werent": [
    {
      "F": "were"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "whyre": [
    {
      "F": "why"
    },
    {
      "F": "re"
    }
  ],
  "g.": [
    {
      "F": "g."
    }
  ],
  "I'm": [
    {
      "L": "-PRON-",
      "F": "I"
    },
    {
      "pos": "VBP",
      "F": "'m",
      "tenspect": 1,
      "number": 1,
      "L": "be"
    }
  ],
  ":p": [
    {
      "F": ":p"
    }
  ],
  "She'd've": [
    {
      "L": "-PRON-",
      "F": "She"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "not've": [
    {
      "F": "not",
      "L": "not",
      "pos": "RB"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "we'll": [
    {
      "F": "we"
    },
    {
      "F": "'ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  ":O": [
    {
      "F": ":O"
    }
  ],
  "<33": [
    {
      "F": "<33"
    }
  ],
  "Don't": [
    {
      "L": "do",
      "F": "Do"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Whyll": [
    {
      "F": "Why"
    },
    {
      "F": "ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "''": [
    {
      "F": "''"
    }
  ],
  "they've": [
    {
      "L": "-PRON-",
      "F": "they"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "t.": [
    {
      "F": "t."
    }
  ],
  "wasn't": [
    {
      "F": "was"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "could've": [
    {
      "pos": "MD",
      "F": "could"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "what've": [
    {
      "F": "what"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "havent": [
    {
      "pos": "VB",
      "F": "have"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Who've": [
    {
      "F": "Who"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "11am": [
    {
      "F": "11"
    },
    {
      "L": "a.m.",
      "F": "am"
    }
  ],
  "Shan't": [
    {
      "F": "Sha"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "i'll": [
    {
      "L": "-PRON-",
      "F": "i"
    },
    {
      "F": "'ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "i.e.": [
    {
      "F": "i.e."
    }
  ],
  "you'd": [
    {
      "L": "-PRON-",
      "F": "you"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "w.": [
    {
      "F": "w."
    }
  ],
  "whens": [
    {
      "F": "when"
    },
    {
      "F": "s"
    }
  ],
  "whys": [
    {
      "F": "why"
    },
    {
      "F": "s"
    }
  ],
  "6pm": [
    {
      "F": "6"
    },
    {
      "L": "p.m.",
      "F": "pm"
    }
  ],
  "4p.m.": [
    {
      "F": "4"
    },
    {
      "F": "p.m."
    }
  ],
  "Whereve": [
    {
      "F": "Where"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "o_o": [
    {
      "F": "o_o"
    }
  ],
  "Mo.": [
    {
      "F": "Mo."
    }
  ],
  "Kan.": [
    {
      "F": "Kan."
    }
  ],
  "\u00a0": [
    {
      "pos": "SP",
      "L": "  ",
      "F": "\u00a0"
    }
  ],
  "there'd": [
    {
      "F": "there"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "N.H.": [
    {
      "F": "N.H."
    }
  ],
  "(^_^)": [
    {
      "F": "(^_^)"
    }
  ],
  "Mont.": [
    {
      "F": "Mont."
    }
  ],
  "hadn't've": [
    {
      "F": "had",
      "L": "have",
      "pos": "VBD"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "whatll": [
    {
      "F": "what"
    },
    {
      "F": "ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "wouldn't've": [
    {
      "F": "would"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "there's": [
    {
      "F": "there"
    },
    {
      "F": "'s"
    }
  ],
  "2pm": [
    {
      "F": "2"
    },
    {
      "L": "p.m.",
      "F": "pm"
    }
  ],
  "Who'll": [
    {
      "F": "Who"
    },
    {
      "F": "'ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "o_O": [
    {
      "F": "o_O"
    }
  ],
  "Nev.": [
    {
      "F": "Nev."
    }
  ],
  "youll": [
    {
      "L": "-PRON-",
      "F": "you"
    },
    {
      "F": "ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "wouldve": [
    {
      "F": "would"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Nov.": [
    {
      "F": "Nov."
    }
  ],
  "z.": [
    {
      "F": "z."
    }
  ],
  "xDD": [
    {
      "F": "xDD"
    }
  ],
  "Sen.": [
    {
      "F": "Sen."
    }
  ],
  "Wouldnt": [
    {
      "F": "Would"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Thered": [
    {
      "F": "There"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "Youre": [
    {
      "L": "-PRON-",
      "F": "You"
    },
    {
      "F": "re"
    }
  ],
  "Couldn't've": [
    {
      "pos": "MD",
      "F": "Could"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "who're": [
    {
      "F": "who"
    },
    {
      "F": "'re"
    }
  ],
  "Whys": [
    {
      "F": "Why"
    },
    {
      "F": "s"
    }
  ],
  "mightn't've": [
    {
      "F": "might"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Wholl": [
    {
      "F": "Who"
    },
    {
      "F": "ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "hadn't": [
    {
      "F": "had",
      "L": "have",
      "pos": "VBD"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Havent": [
    {
      "pos": "VB",
      "F": "Have"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Whatve": [
    {
      "F": "What"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  ":)": [
    {
      "F": ":)"
    }
  ],
  "o.O": [
    {
      "F": "o.O"
    }
  ],
  "Thats": [
    {
      "F": "That"
    },
    {
      "F": "s"
    }
  ],
  ":((": [
    {
      "F": ":(("
    }
  ],
  "Gov.": [
    {
      "F": "Gov."
    }
  ],
  "Howll": [
    {
      "F": "How"
    },
    {
      "F": "ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "p.": [
    {
      "F": "p."
    }
  ],
  "wouldn't": [
    {
      "F": "would"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "9pm": [
    {
      "F": "9"
    },
    {
      "L": "p.m.",
      "F": "pm"
    }
  ],
  "You'll": [
    {
      "L": "-PRON-",
      "F": "You"
    },
    {
      "F": "'ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "Ala.": [
    {
      "F": "Ala."
    }
  ],
  "12am": [
    {
      "F": "12"
    },
    {
      "L": "a.m.",
      "F": "am"
    }
  ],
  "=]": [
    {
      "F": "=]"
    }
  ],
  "Cant": [
    {
      "F": "Ca",
      "L": "can",
      "pos": "MD"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "i'd": [
    {
      "L": "-PRON-",
      "F": "i"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "a.m.": [
    {
      "F": "a.m."
    }
  ],
  "weren't": [
    {
      "F": "were"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "would've": [
    {
      "F": "would"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "i'm": [
    {
      "L": "-PRON-",
      "F": "i"
    },
    {
      "pos": "VBP",
      "F": "'m",
      "tenspect": 1,
      "number": 1,
      "L": "be"
    }
  ],
  "why'll": [
    {
      "F": "why"
    },
    {
      "F": "'ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "we'd've": [
    {
      "F": "we"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Shouldve": [
    {
      "F": "Should"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "can't": [
    {
      "F": "ca",
      "L": "can",
      "pos": "MD"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "thats": [
    {
      "F": "that"
    },
    {
      "F": "s"
    }
  ],
  "1p.m.": [
    {
      "F": "1"
    },
    {
      "F": "p.m."
    }
  ],
  "12a.m.": [
    {
      "F": "12"
    },
    {
      "F": "a.m."
    }
  ],
  "Hes": [
    {
      "L": "-PRON-",
      "F": "He"
    },
    {
      "F": "s"
    }
  ],
  "Needn't": [
    {
      "F": "Need"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "It's": [
    {
      "L": "-PRON-",
      "F": "It"
    },
    {
      "F": "'s"
    }
  ],
  "St.": [
    {
      "F": "St."
    }
  ],
  "Why're": [
    {
      "F": "Why"
    },
    {
      "F": "'re"
    }
  ],
  ":(((": [
    {
      "F": ":((("
    }
  ],
  "Hed": [
    {
      "L": "-PRON-",
      "F": "He"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "Mt.": [
    {
      "L": "Mount",
      "F": "Mt."
    }
  ],
  "couldn't": [
    {
      "pos": "MD",
      "F": "could"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "What've": [
    {
      "F": "What"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "4a.m.": [
    {
      "F": "4"
    },
    {
      "F": "a.m."
    }
  ],
  "Ind.": [
    {
      "F": "Ind."
    }
  ],
  "It'd": [
    {
      "L": "-PRON-",
      "F": "It"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "<3": [
    {
      "F": "<3"
    }
  ],
  "theydve": [
    {
      "L": "-PRON-",
      "F": "they"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "aren't": [
    {
      "F": "are",
      "pos": "VBP",
      "number": 2,
      "L": "be"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Mightn't": [
    {
      "F": "Might"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "'S": [
    {
      "L": "'s",
      "F": "'S"
    }
  ],
  "I've": [
    {
      "L": "-PRON-",
      "F": "I"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Whered": [
    {
      "F": "Where"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "Itdve": [
    {
      "L": "-PRON-",
      "F": "It"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "I'ma": [
    {
      "L": "-PRON-",
      "F": "I"
    },
    {
      "F": "'ma"
    }
  ],
  "whos": [
    {
      "F": "who"
    },
    {
      "F": "s"
    }
  ],
  "They'd": [
    {
      "L": "-PRON-",
      "F": "They"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "What'll": [
    {
      "F": "What"
    },
    {
      "F": "'ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  ":Y": [
    {
      "F": ":Y"
    }
  ],
  "You've": [
    {
      "L": "-PRON-",
      "F": "You"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Mustve": [
    {
      "F": "Must"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "whod": [
    {
      "F": "who"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "mightntve": [
    {
      "F": "might"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "I'd've": [
    {
      "L": "-PRON-",
      "F": "I"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Must've": [
    {
      "F": "Must"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "it'd": [
    {
      "L": "-PRON-",
      "F": "it"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "Ark.": [
    {
      "F": "Ark."
    }
  ],
  "Wis.": [
    {
      "F": "Wis."
    }
  ],
  "6p.m.": [
    {
      "F": "6"
    },
    {
      "F": "p.m."
    }
  ],
  "what're": [
    {
      "F": "what"
    },
    {
      "F": "'re"
    }
  ],
  "N.C.": [
    {
      "F": "N.C."
    }
  ],
  "Wasn't": [
    {
      "F": "Was"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "what's": [
    {
      "F": "what"
    },
    {
      "F": "'s"
    }
  ],
  "he'd've": [
    {
      "L": "-PRON-",
      "F": "he"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Jan.": [
    {
      "F": "Jan."
    }
  ],
  "She'd": [
    {
      "L": "-PRON-",
      "F": "She"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "shedve": [
    {
      "L": "-PRON-",
      "F": "she"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Tenn.": [
    {
      "F": "Tenn."
    }
  ],
  "ain't": [
    {
      "F": "ai",
      "pos": "VBP",
      "number": 2,
      "L": "be"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Wash.": [
    {
      "F": "Wash."
    }
  ],
  "She's": [
    {
      "L": "-PRON-",
      "F": "She"
    },
    {
      "F": "'s"
    }
  ],
  "i'd've": [
    {
      "L": "-PRON-",
      "F": "i"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "2a.m.": [
    {
      "F": "2"
    },
    {
      "F": "a.m."
    }
  ],
  "We'd've": [
    {
      "F": "We"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "must've": [
    {
      "F": "must"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "That's": [
    {
      "F": "That"
    },
    {
      "F": "'s"
    }
  ],
  "Sept.": [
    {
      "F": "Sept."
    }
  ],
  "whatre": [
    {
      "F": "what"
    },
    {
      "F": "re"
    }
  ],
  "you'd've": [
    {
      "L": "-PRON-",
      "F": "you"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Dont": [
    {
      "L": "do",
      "F": "Do"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "i.": [
    {
      "F": "i."
    }
  ],
  "Jun.": [
    {
      "F": "Jun."
    }
  ],
  "thered": [
    {
      "F": "there"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "Youd": [
    {
      "L": "-PRON-",
      "F": "You"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "couldn't've": [
    {
      "pos": "MD",
      "F": "could"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Whens": [
    {
      "F": "When"
    },
    {
      "F": "s"
    }
  ],
  "8a.m.": [
    {
      "F": "8"
    },
    {
      "F": "a.m."
    }
  ],
  "Isnt": [
    {
      "F": "Is",
      "L": "be",
      "pos": "VBZ"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "mightve": [
    {
      "F": "might"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "'ol": [
    {
      "F": "'ol"
    }
  ],
  "2p.m.": [
    {
      "F": "2"
    },
    {
      "F": "p.m."
    }
  ],
  "9a.m.": [
    {
      "F": "9"
    },
    {
      "F": "a.m."
    }
  ],
  "q.": [
    {
      "F": "q."
    }
  ],
  "didnt": [
    {
      "F": "did",
      "L": "do",
      "pos": "VBD"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "ive": [
    {
      "L": "-PRON-",
      "F": "i"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "It'd've": [
    {
      "L": "-PRON-",
      "F": "It"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "e.g.": [
    {
      "F": "e.g."
    }
  ],
  "\t": [
    {
      "pos": "SP",
      "F": "\t"
    }
  ],
  "Mich.": [
    {
      "F": "Mich."
    }
  ],
  "Itll": [
    {
      "L": "-PRON-",
      "F": "It"
    },
    {
      "F": "ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "didn't": [
    {
      "F": "did",
      "L": "do",
      "pos": "VBD"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "3pm": [
    {
      "F": "3"
    },
    {
      "L": "p.m.",
      "F": "pm"
    }
  ],
  "Jul.": [
    {
      "F": "Jul."
    }
  ],
  "7pm": [
    {
      "F": "7"
    },
    {
      "L": "p.m.",
      "F": "pm"
    }
  ],
  "cant": [
    {
      "F": "ca",
      "L": "can",
      "pos": "MD"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Miss.": [
    {
      "F": "Miss."
    }
  ],
  "im": [
    {
      "L": "-PRON-",
      "F": "i"
    },
    {
      "pos": "VBP",
      "F": "m",
      "tenspect": 1,
      "number": 1,
      "L": "be"
    }
  ],
  "Ariz.": [
    {
      "F": "Ariz."
    }
  ],
  "they'd've": [
    {
      "L": "-PRON-",
      "F": "they"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "f.": [
    {
      "F": "f."
    }
  ],
  "Co.": [
    {
      "F": "Co."
    }
  ],
  "Hadntve": [
    {
      "F": "Had",
      "L": "have",
      "pos": "VBD"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Weve": [
    {
      "F": "We"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "1a.m.": [
    {
      "F": "1"
    },
    {
      "F": "a.m."
    }
  ],
  "=3": [
    {
      "F": "=3"
    }
  ],
  "Mightnt": [
    {
      "F": "Might"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "1pm": [
    {
      "F": "1"
    },
    {
      "L": "p.m.",
      "F": "pm"
    }
  ],
  "youdve": [
    {
      "L": "-PRON-",
      "F": "you"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Shedve": [
    {
      "L": "-PRON-",
      "F": "She"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "theyd": [
    {
      "L": "-PRON-",
      "F": "they"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "Ill.": [
    {
      "F": "Ill."
    }
  ],
  "N.D.": [
    {
      "F": "N.D."
    }
  ],
  "Cannot": [
    {
      "F": "Can",
      "L": "can",
      "pos": "MD"
    },
    {
      "F": "not",
      "L": "not",
      "pos": "RB"
    }
  ],
  "s.": [
    {
      "F": "s."
    }
  ],
  "Hadn't": [
    {
      "F": "Had",
      "L": "have",
      "pos": "VBD"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "What're": [
    {
      "F": "What"
    },
    {
      "F": "'re"
    }
  ],
  "He'll": [
    {
      "L": "-PRON-",
      "F": "He"
    },
    {
      "F": "'ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "wholl": [
    {
      "F": "who"
    },
    {
      "F": "ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "They're": [
    {
      "L": "-PRON-",
      "F": "They"
    },
    {
      "F": "'re"
    }
  ],
  "Neb.": [
    {
      "F": "Neb."
    }
  ],
  "shouldnt": [
    {
      "F": "should"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "\n": [
    {
      "pos": "SP",
      "F": "\n"
    }
  ],
  "whered": [
    {
      "F": "where"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "7a.m.": [
    {
      "F": "7"
    },
    {
      "F": "a.m."
    }
  ],
  "youve": [
    {
      "L": "-PRON-",
      "F": "you"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "4am": [
    {
      "F": "4"
    },
    {
      "L": "a.m.",
      "F": "am"
    }
  ],
  "v.": [
    {
      "F": "v."
    }
  ],
  "notve": [
    {
      "F": "not",
      "L": "not",
      "pos": "RB"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "couldve": [
    {
      "pos": "MD",
      "F": "could"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "mustve": [
    {
      "F": "must"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Youve": [
    {
      "L": "-PRON-",
      "F": "You"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "therell": [
    {
      "F": "there"
    },
    {
      "F": "ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "might've": [
    {
      "F": "might"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Mustn't": [
    {
      "F": "Must"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "wheres": [
    {
      "F": "where"
    },
    {
      "F": "s"
    }
  ],
  "they're": [
    {
      "L": "-PRON-",
      "F": "they"
    },
    {
      "F": "'re"
    }
  ],
  "idve": [
    {
      "L": "-PRON-",
      "F": "i"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "hows": [
    {
      "F": "how"
    },
    {
      "F": "s"
    }
  ],
  "Fla.": [
    {
      "F": "Fla."
    }
  ],
  "N.M.": [
    {
      "F": "N.M."
    }
  ],
  "youre": [
    {
      "L": "-PRON-",
      "F": "you"
    },
    {
      "F": "re"
    }
  ],
  "Didn't": [
    {
      "F": "Did",
      "L": "do",
      "pos": "VBD"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Couldve": [
    {
      "pos": "MD",
      "F": "Could"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "10p.m.": [
    {
      "F": "10"
    },
    {
      "F": "p.m."
    }
  ],
  "Del.": [
    {
      "F": "Del."
    }
  ],
  "Oct.": [
    {
      "F": "Oct."
    }
  ],
  "Rep.": [
    {
      "F": "Rep."
    }
  ],
  "cannot": [
    {
      "F": "can",
      "L": "can",
      "pos": "MD"
    },
    {
      "F": "not",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Im": [
    {
      "L": "-PRON-",
      "F": "I"
    },
    {
      "pos": "VBP",
      "F": "m",
      "tenspect": 1,
      "number": 1,
      "L": "be"
    }
  ],
  "howd": [
    {
      "F": "how"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "Okla.": [
    {
      "F": "Okla."
    }
  ],
  "Feb.": [
    {
      "F": "Feb."
    }
  ],
  "you've": [
    {
      "L": "-PRON-",
      "F": "you"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "You're": [
    {
      "L": "-PRON-",
      "F": "You"
    },
    {
      "F": "'re"
    }
  ],
  "she'll": [
    {
      "L": "-PRON-",
      "F": "she"
    },
    {
      "F": "'ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "Theyll": [
    {
      "L": "-PRON-",
      "F": "They"
    },
    {
      "F": "ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "don't": [
    {
      "L": "do",
      "F": "do"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "itd": [
    {
      "L": "-PRON-",
      "F": "it"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    }
  ],
  ":-)": [
    {
      "F": ":-)"
    }
  ],
  "Hedve": [
    {
      "L": "-PRON-",
      "F": "He"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "isnt": [
    {
      "F": "is",
      "L": "be",
      "pos": "VBZ"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "won't": [
    {
      "F": "wo"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "We're": [
    {
      "F": "We"
    },
    {
      "F": "'re"
    }
  ],
  "3a.m.": [
    {
      "F": "3"
    },
    {
      "F": "a.m."
    }
  ],
  "^_^": [
    {
      "F": "^_^"
    }
  ],
  "\u2018S": [
    {
      "L": "'s",
      "F": "\u2018S"
    }
  ],
  "9p.m.": [
    {
      "F": "9"
    },
    {
      "F": "p.m."
    }
  ],
  "dont": [
    {
      "L": "do",
      "F": "do"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "ima": [
    {
      "L": "-PRON-",
      "F": "i"
    },
    {
      "F": "ma"
    }
  ],
  "Let's": [
    {
      "F": "Let"
    },
    {
      "L": "us",
      "F": "'s"
    }
  ],
  "he's": [
    {
      "L": "-PRON-",
      "F": "he"
    },
    {
      "F": "'s"
    }
  ],
  "we've": [
    {
      "F": "we"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "What's": [
    {
      "F": "What"
    },
    {
      "F": "'s"
    }
  ],
  "Who's": [
    {
      "F": "Who"
    },
    {
      "F": "'s"
    }
  ],
  "-__-": [
    {
      "F": "-__-"
    }
  ],
  "hedve": [
    {
      "L": "-PRON-",
      "F": "he"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "he'd": [
    {
      "L": "-PRON-",
      "F": "he"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "When's": [
    {
      "F": "When"
    },
    {
      "F": "'s"
    }
  ],
  "Mightn't've": [
    {
      "F": "Might"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "We've": [
    {
      "F": "We"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "\u2018s": [
    {
      "L": "'s",
      "F": "\u2018s"
    }
  ],
  "Couldntve": [
    {
      "pos": "MD",
      "F": "Could"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Who'd": [
    {
      "F": "Who"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    }
  ],
  ":-/": [
    {
      "F": ":-/"
    }
  ],
  "haven't": [
    {
      "pos": "VB",
      "F": "have"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Gen.": [
    {
      "F": "Gen."
    }
  ],
  "(:": [
    {
      "F": "(:"
    }
  ],
  "arent": [
    {
      "F": "are",
      "pos": "VBP",
      "number": 2,
      "L": "be"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "You'd've": [
    {
      "L": "-PRON-",
      "F": "You"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "c.": [
    {
      "F": "c."
    }
  ],
  "(=": [
    {
      "F": "(="
    }
  ],
  "Wouldn't": [
    {
      "F": "Would"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "who's": [
    {
      "F": "who"
    },
    {
      "F": "'s"
    }
  ],
  "12p.m.": [
    {
      "F": "12"
    },
    {
      "F": "p.m."
    }
  ],
  "5am": [
    {
      "F": "5"
    },
    {
      "L": "a.m.",
      "F": "am"
    }
  ],
  "Mightve": [
    {
      "F": "Might"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Theredve": [
    {
      "F": "There"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "theredve": [
    {
      "F": "there"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Messrs.": [
    {
      "F": "Messrs."
    }
  ],
  "who'd": [
    {
      "F": "who"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "Where's": [
    {
      "F": "Where"
    },
    {
      "F": "'s"
    }
  ],
  "wont": [
    {
      "F": "wo"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "she'd've": [
    {
      "L": "-PRON-",
      "F": "she"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "10pm": [
    {
      "F": "10"
    },
    {
      "L": "p.m.",
      "F": "pm"
    }
  ],
  "Corp.": [
    {
      "F": "Corp."
    }
  ],
  "Aug.": [
    {
      "F": "Aug."
    }
  ],
  "-_-": [
    {
      "F": "-_-"
    }
  ],
  "y.": [
    {
      "F": "y."
    }
  ],
  "Should've": [
    {
      "F": "Should"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "11pm": [
    {
      "F": "11"
    },
    {
      "L": "p.m.",
      "F": "pm"
    }
  ],
  "8am": [
    {
      "F": "8"
    },
    {
      "L": "a.m.",
      "F": "am"
    }
  ],
  "theyre": [
    {
      "L": "-PRON-",
      "F": "they"
    },
    {
      "F": "re"
    }
  ],
  "l.": [
    {
      "F": "l."
    }
  ],
  "Wouldntve": [
    {
      "F": "Would"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Ga.": [
    {
      "F": "Ga."
    }
  ],
  "1am": [
    {
      "F": "1"
    },
    {
      "L": "a.m.",
      "F": "am"
    }
  ],
  "Where've": [
    {
      "F": "Where"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "11a.m.": [
    {
      "F": "11"
    },
    {
      "F": "a.m."
    }
  ],
  "mustn't": [
    {
      "F": "must"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "isn't": [
    {
      "F": "is",
      "L": "be",
      "pos": "VBZ"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Bros.": [
    {
      "F": "Bros."
    }
  ],
  "Aint": [
    {
      "F": "Ai",
      "pos": "VBP",
      "number": 2,
      "L": "be"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "why's": [
    {
      "F": "why"
    },
    {
      "F": "'s"
    }
  ],
  "V_V": [
    {
      "F": "V_V"
    }
  ],
  ";p": [
    {
      "F": ";p"
    }
  ],
  "There'd": [
    {
      "F": "There"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "They'll": [
    {
      "L": "-PRON-",
      "F": "They"
    },
    {
      "F": "'ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "b.": [
    {
      "F": "b."
    }
  ],
  "how'll": [
    {
      "F": "how"
    },
    {
      "F": "'ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "Wedve": [
    {
      "F": "We"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "couldntve": [
    {
      "pos": "MD",
      "F": "could"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "12pm": [
    {
      "F": "12"
    },
    {
      "L": "p.m.",
      "F": "pm"
    }
  ],
  "There's": [
    {
      "F": "There"
    },
    {
      "F": "'s"
    }
  ],
  "we'd": [
    {
      "F": "we"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "Dr.": [
    {
      "F": "Dr."
    }
  ],
  "Whod": [
    {
      "F": "Who"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    }
  ],
  ":-P": [
    {
      "F": ":-P"
    }
  ],
  "whatve": [
    {
      "F": "what"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Wouldve": [
    {
      "F": "Would"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "o.": [
    {
      "F": "o."
    }
  ],
  "there'll": [
    {
      "F": "there"
    },
    {
      "F": "'ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  ":]": [
    {
      "F": ":]"
    }
  ],
  "needn't": [
    {
      "F": "need"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "shouldntve": [
    {
      "F": "should"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "why're": [
    {
      "F": "why"
    },
    {
      "F": "'re"
    }
  ],
  "p.m.": [
    {
      "F": "p.m."
    }
  ],
  "Doesnt": [
    {
      "F": "Does",
      "L": "do",
      "pos": "VBZ"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "whereve": [
    {
      "F": "where"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "they'll": [
    {
      "L": "-PRON-",
      "F": "they"
    },
    {
      "F": "'ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "I'd": [
    {
      "L": "-PRON-",
      "F": "I"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "Might've": [
    {
      "F": "Might"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "mightnt": [
    {
      "F": "might"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Kans.": [
    {
      "F": "Kans."
    }
  ],
  "Not've": [
    {
      "F": "Not",
      "L": "not",
      "pos": "RB"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "e.": [
    {
      "F": "e."
    }
  ],
  "mightn't": [
    {
      "F": "might"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "you're": [
    {
      "L": "-PRON-",
      "F": "you"
    },
    {
      "F": "'re"
    }
  ],
  "Mar.": [
    {
      "F": "Mar."
    }
  ],
  "They've": [
    {
      "L": "-PRON-",
      "F": "They"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "\")": [
    {
      "F": "\")"
    }
  ],
  "what'll": [
    {
      "F": "what"
    },
    {
      "F": "'ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "Calif.": [
    {
      "F": "Calif."
    }
  ],
  "Could've": [
    {
      "pos": "MD",
      "F": "Could"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Would've": [
    {
      "F": "Would"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  ";)": [
    {
      "F": ";)"
    }
  ],
  ";(": [
    {
      "F": ";("
    }
  ],
  "Isn't": [
    {
      "F": "Is",
      "L": "be",
      "pos": "VBZ"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "let's": [
    {
      "F": "let"
    },
    {
      "L": "us",
      "F": "'s"
    }
  ],
  "'em": [
    {
      "F": "'em"
    }
  ],
  "She'll": [
    {
      "L": "-PRON-",
      "F": "She"
    },
    {
      "F": "'ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "I.E.": [
    {
      "F": "I.E."
    }
  ],
  "You'd": [
    {
      "L": "-PRON-",
      "F": "You"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "wouldnt": [
    {
      "F": "would"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "6am": [
    {
      "F": "6"
    },
    {
      "L": "a.m.",
      "F": "am"
    }
  ],
  ":P": [
    {
      "F": ":P"
    }
  ],
  "Why'll": [
    {
      "F": "Why"
    },
    {
      "F": "'ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "Where'd": [
    {
      "F": "Where"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "Theyre": [
    {
      "L": "-PRON-",
      "F": "They"
    },
    {
      "F": "re"
    }
  ],
  "11p.m.": [
    {
      "F": "11"
    },
    {
      "F": "p.m."
    }
  ],
  "Won't": [
    {
      "F": "Wo"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Couldn't": [
    {
      "pos": "MD",
      "F": "Could"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "it's": [
    {
      "L": "-PRON-",
      "F": "it"
    },
    {
      "F": "'s"
    }
  ],
  "r.": [
    {
      "F": "r."
    }
  ],
  "it'll": [
    {
      "L": "-PRON-",
      "F": "it"
    },
    {
      "F": "'ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "They'd've": [
    {
      "L": "-PRON-",
      "F": "They"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Ima": [
    {
      "L": "-PRON-",
      "F": "I"
    },
    {
      "F": "ma"
    }
  ],
  "5pm": [
    {
      "F": "5"
    },
    {
      "L": "p.m.",
      "F": "pm"
    }
  ],
  "10am": [
    {
      "F": "10"
    },
    {
      "L": "a.m.",
      "F": "am"
    }
  ],
  "m.": [
    {
      "F": "m."
    }
  ],
  "whats": [
    {
      "F": "what"
    },
    {
      "F": "s"
    }
  ],
  "How's": [
    {
      "F": "How"
    },
    {
      "F": "'s"
    }
  ],
  "Sep.": [
    {
      "F": "Sep."
    }
  ],
  "Shouldntve": [
    {
      "F": "Should"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "youd": [
    {
      "L": "-PRON-",
      "F": "you"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "Whatll": [
    {
      "F": "What"
    },
    {
      "F": "ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "Wouldn't've": [
    {
      "F": "Would"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "How'd": [
    {
      "F": "How"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "doesnt": [
    {
      "F": "does",
      "L": "do",
      "pos": "VBZ"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "h.": [
    {
      "F": "h."
    }
  ],
  "Shouldn't": [
    {
      "F": "Should"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "He'd've": [
    {
      "L": "-PRON-",
      "F": "He"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Mightntve": [
    {
      "F": "Might"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "couldnt": [
    {
      "pos": "MD",
      "F": "could"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Haven't": [
    {
      "pos": "VB",
      "F": "Have"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "<333": [
    {
      "F": "<333"
    }
  ],
  "doesn't": [
    {
      "F": "does",
      "L": "do",
      "pos": "VBZ"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Hasn't": [
    {
      "F": "Has"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "how's": [
    {
      "F": "how"
    },
    {
      "F": "'s"
    }
  ],
  "hes": [
    {
      "L": "-PRON-",
      "F": "he"
    },
    {
      "F": "s"
    }
  ],
  "=[[": [
    {
      "F": "=[["
    }
  ],
  "xD": [
    {
      "F": "xD"
    }
  ],
  "he'll": [
    {
      "L": "-PRON-",
      "F": "he"
    },
    {
      "F": "'ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "hed": [
    {
      "L": "-PRON-",
      "F": "he"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "7p.m.": [
    {
      "F": "7"
    },
    {
      "F": "p.m."
    }
  ],
  "how'd": [
    {
      "F": "how"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "u.": [
    {
      "F": "u."
    }
  ],
  "we're": [
    {
      "F": "we"
    },
    {
      "F": "'re"
    }
  ],
  "vs.": [
    {
      "F": "vs."
    }
  ],
  "Hadnt": [
    {
      "F": "Had",
      "L": "have",
      "pos": "VBD"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Shant": [
    {
      "F": "Sha"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Theyve": [
    {
      "L": "-PRON-",
      "F": "They"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Hows": [
    {
      "F": "How"
    },
    {
      "F": "s"
    }
  ],
  "We'll": [
    {
      "F": "We"
    },
    {
      "F": "'ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "N.Y.": [
    {
      "F": "N.Y."
    }
  ],
  "x.": [
    {
      "F": "x."
    }
  ],
  "8p.m.": [
    {
      "F": "8"
    },
    {
      "F": "p.m."
    }
  ],
  "i've": [
    {
      "L": "-PRON-",
      "F": "i"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Whove": [
    {
      "F": "Who"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "2am": [
    {
      "F": "2"
    },
    {
      "L": "a.m.",
      "F": "am"
    }
  ],
  "La.": [
    {
      "F": "La."
    }
  ],
  "i'ma": [
    {
      "L": "-PRON-",
      "F": "i"
    },
    {
      "F": "'ma"
    }
  ],
  "N.J.": [
    {
      "F": "N.J."
    }
  ],
  "Nebr.": [
    {
      "F": "Nebr."
    }
  ],
  "Howd": [
    {
      "F": "How"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "hadnt": [
    {
      "F": "had",
      "L": "have",
      "pos": "VBD"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "shant": [
    {
      "F": "sha"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "There'd've": [
    {
      "F": "There"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Inc.": [
    {
      "F": "Inc."
    }
  ],
  "I'll": [
    {
      "L": "-PRON-",
      "F": "I"
    },
    {
      "F": "'ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "Why's": [
    {
      "F": "Why"
    },
    {
      "F": "'s"
    }
  ],
  "Adm.": [
    {
      "F": "Adm."
    }
  ],
  "Shouldn't've": [
    {
      "F": "Should"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "n.": [
    {
      "F": "n."
    }
  ],
  "Wasnt": [
    {
      "F": "Was"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "whove": [
    {
      "F": "who"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  ";-p": [
    {
      "F": ";-p"
    }
  ],
  "hasn't": [
    {
      "F": "has"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "wouldntve": [
    {
      "F": "would"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Wheres": [
    {
      "F": "Where"
    },
    {
      "F": "s"
    }
  ],
  "How'll": [
    {
      "F": "How"
    },
    {
      "F": "'ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "there'd've": [
    {
      "F": "there"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Whos": [
    {
      "F": "Who"
    },
    {
      "F": "s"
    }
  ],
  "shes": [
    {
      "L": "-PRON-",
      "F": "she"
    },
    {
      "F": "s"
    }
  ],
  "Doesn't": [
    {
      "F": "Does",
      "L": "do",
      "pos": "VBZ"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Arent": [
    {
      "F": "Are",
      "pos": "VBP",
      "number": 2,
      "L": "be"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Hasnt": [
    {
      "F": "Has"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "j.": [
    {
      "F": "j."
    }
  ],
  "He's": [
    {
      "L": "-PRON-",
      "F": "He"
    },
    {
      "F": "'s"
    }
  ],
  "wasnt": [
    {
      "F": "was"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "whyll": [
    {
      "F": "why"
    },
    {
      "F": "ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "co.": [
    {
      "F": "co."
    }
  ],
  "mustnt": [
    {
      "F": "must"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "He'd": [
    {
      "L": "-PRON-",
      "F": "He"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "I.e.": [
    {
      "F": "I.e."
    }
  ],
  "Shes": [
    {
      "L": "-PRON-",
      "F": "She"
    },
    {
      "F": "s"
    }
  ],
  "where've": [
    {
      "F": "where"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Youll": [
    {
      "L": "-PRON-",
      "F": "You"
    },
    {
      "F": "ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "Apr.": [
    {
      "F": "Apr."
    }
  ],
  ":')": [
    {
      "F": ":')"
    }
  ],
  "Conn.": [
    {
      "F": "Conn."
    }
  ],
  "8pm": [
    {
      "F": "8"
    },
    {
      "L": "p.m.",
      "F": "pm"
    }
  ],
  "9am": [
    {
      "F": "9"
    },
    {
      "L": "a.m.",
      "F": "am"
    }
  ],
  "hasnt": [
    {
      "F": "has"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "theyll": [
    {
      "L": "-PRON-",
      "F": "they"
    },
    {
      "F": "ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "it'd've": [
    {
      "L": "-PRON-",
      "F": "it"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "itdve": [
    {
      "L": "-PRON-",
      "F": "it"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Jr.": [
    {
      "F": "Jr."
    }
  ],
  "Rev.": [
    {
      "F": "Rev."
    }
  ],
  "k.": [
    {
      "F": "k."
    }
  ],
  "wedve": [
    {
      "F": "we"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "=)": [
    {
      "F": "=)"
    }
  ],
  "Colo.": [
    {
      "F": "Colo."
    }
  ],
  "Mr.": [
    {
      "F": "Mr."
    }
  ],
  "Werent": [
    {
      "F": "Were"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Therell": [
    {
      "F": "There"
    },
    {
      "F": "ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "shan't": [
    {
      "F": "sha"
    },
    {
      "F": "n't",
      "L": "not",
      "pos": "RB"
    }
  ],
  ";-)": [
    {
      "F": ";-)"
    }
  ],
  "Wont": [
    {
      "F": "Wo"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "hadntve": [
    {
      "F": "had",
      "L": "have",
      "pos": "VBD"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "who've": [
    {
      "F": "who"
    },
    {
      "F": "'ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "Whatre": [
    {
      "F": "What"
    },
    {
      "F": "re"
    }
  ],
  "'s": [
    {
      "L": "'s",
      "F": "'s"
    }
  ],
  "where'd": [
    {
      "F": "where"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "shouldve": [
    {
      "F": "should"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "a.": [
    {
      "F": "a."
    }
  ],
  "where's": [
    {
      "F": "where"
    },
    {
      "F": "'s"
    }
  ],
  "Ltd.": [
    {
      "F": "Ltd."
    }
  ],
  "Mass.": [
    {
      "F": "Mass."
    }
  ],
  "neednt": [
    {
      "F": "need"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Pa.": [
    {
      "F": "Pa."
    }
  ],
  "It'll": [
    {
      "L": "-PRON-",
      "F": "It"
    },
    {
      "F": "'ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "7am": [
    {
      "F": "7"
    },
    {
      "L": "a.m.",
      "F": "am"
    }
  ],
  "We'd": [
    {
      "F": "We"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "Whats": [
    {
      "F": "What"
    },
    {
      "F": "s"
    }
  ],
  "\u2014": [
    {
      "pos": ":",
      "L": "--",
      "F": "\u2014"
    }
  ],
  "E.g.": [
    {
      "F": "E.g."
    }
  ],
  "Ms.": [
    {
      "F": "Ms."
    }
  ],
  ":3": [
    {
      "F": ":3"
    }
  ],
  "5p.m.": [
    {
      "F": "5"
    },
    {
      "F": "p.m."
    }
  ],
  "Itd": [
    {
      "L": "-PRON-",
      "F": "It"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "May.": [
    {
      "F": "May."
    }
  ],
  "she'd": [
    {
      "L": "-PRON-",
      "F": "she"
    },
    {
      "F": "'d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "Mustnt": [
    {
      "F": "Must"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "Notve": [
    {
      "F": "Not",
      "L": "not",
      "pos": "RB"
    },
    {
      "F": "ve",
      "L": "have",
      "pos": "VB"
    }
  ],
  "you'll": [
    {
      "L": "-PRON-",
      "F": "you"
    },
    {
      "F": "'ll",
      "L": "will",
      "pos": "MD"
    }
  ],
  "Theyd": [
    {
      "L": "-PRON-",
      "F": "They"
    },
    {
      "F": "d",
      "L": "would",
      "pos": "MD"
    }
  ],
  "she's": [
    {
      "L": "-PRON-",
      "F": "she"
    },
    {
      "F": "'s"
    }
  ],
  "Couldnt": [
    {
      "pos": "MD",
      "F": "Could"
    },
    {
      "F": "nt",
      "L": "not",
      "pos": "RB"
    }
  ],
  "that's": [
    {
      "F": "that"
    },
    {
      "F": "'s"
    }
  ],
  "4pm": [
    {
      "F": "4"
    },
    {
      "L": "p.m.",
      "F": "pm"
    }
  ],
  ":))": [
    {
      "F": ":))"
    }
  ]
}
