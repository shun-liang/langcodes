"""
These are the 300 languages that have the most entries on the English
Wiktionary (which defines words of all languages in English). Wiktionary
only consistently identifies languages by their name, making it important
to be able to recognize the names.

Here, we test that we can at least associate a language code with each name,
and that all the language codes are different. Languages that don't have an
identifiable language code are commented out here.
"""
from langcodes import find_name

LANGUAGE_NAMES = [
    "Spanish",
    "French",
    "Latvian",
    "Latin",
    "English",
    "Mandarin",
    "Italian",
    "Portuguese",
    "Cantonese",
    "Japanese",
    "German",
    "Swedish",
    "Korean",
    "Serbo-Croatian",
    "Finnish",
    "Vietnamese",
    "Dutch",
    "Galician",
    "Catalan",
    "Polish",
    "Danish",
    "Norwegian Nynorsk",
    "Turkish",
    "Romanian",
    "Lithuanian",
    "Ido",
    "Old French",
    "Czech",
    "Norwegian",
    # Jèrriais
    "Esperanto",
    "Icelandic",
    # Old Armenian
    "Norwegian Bokmål",
    "Asturian",
    "Hungarian",
    "Proto-Germanic",
    "Russian",
    "Slovene",
    "Min Nan",
    "Scottish Gaelic",
    "Greek",
    "Irish",
    "Lojban",
    "Middle French",
    "Malay",
    "Luxembourgish",
    "Slovak",
    "Estonian",
    "Persian",
    "Venetian",
    "Old English",
    "Volapük",
    "Ladin",
    "Faroese",
    "Scots",
    "Interlingua",
    "Romansch",
    "Urdu",
    # Middle Chinese
    "Indonesian",
    "Swahili",
    "Middle English",
    "Occitan",
    "Welsh",
    "Old Norse",
    "Albanian",
    "Old Irish",
    "Old Saxon",
    "Lower Sorbian",
    "Afrikaans",
    "Ukrainian",
    "Proto-Slavic",
    "Ancient Greek",
    "Gothic",
    "Hawaiian",
    "Kurdish",
    "Tagalog",
    "Old High German",
    "Crimean Tatar",
    "Manx",
    "Sanskrit",
    "Hiligaynon",
    "West Frisian",
    "Hebrew",
    "Tok Pisin",
    "Proto-Indo-European",
    "Macedonian",
    "Novial",
    "Armenian",
    "Arabic",
    "Maltese",
    "Hakka",
    "Sicilian",
    "Ladino",
    "Basque",
    "Breton",
    # Guernésiais
    "Vai",
    "Navajo",
    "Azeri",
    "Vilamovian",
    # Tarantino
    "Maori",
    "Friulian",
    "Hausa",
    "Haitian Creole",
    "Yiddish",
    "Tatar",
    "Proto-Malayo-Polynesian",
    "Aromanian",
    "Ottoman Turkish",
    "Old Provençal",
    "Northern Sami",
    "Dalmatian",
    "Bulgarian",
    "Neapolitan",
    "Cornish",
    "Middle Dutch",
    "Rapa Nui",
    # Old Portuguese
    "Egyptian Arabic",
    "Romani",
    "Tahitian",
    "Thai",
    "Limburgish",
    "Karelian",
    "Tajik",
    "Turkmen",
    "Kabardian",
    "Uzbek",
    "Samoan",
    "Mongolian",
    "Zulu",
    "Upper Sorbian",
    "Walloon",
    # Proto-Finnic
    "Frankish",
    "Mapudungun",
    "Pashto",
    "Low German",
    "Bashkir",
    "Kashubian",
    "Sranan Tongo",
    "Proto-Sino-Tibetan",
    # Norman
    "Proto-Austronesian",
    "Marathi",
    "Rohingya",
    "Classical Nahuatl",
    # Proto-Malayic
    # German Low German
    "Fijian",
    "Zazaki",
    "Proto-Italic",
    "Old Dutch",
    "Egyptian",
    "Old Frisian",
    "Greenlandic",
    "Burmese",
    "Votic",
    "Ewe",
    "Cherokee",
    "Old Church Slavonic",
    "Quechua",
    "Mirandese",
    "Livonian",
    "Bengali",
    "Skolt Sami",
    # Proto-Balto-Slavic
    "Pitjantjatjara",
    "Georgian",
    "North Frisian",
    "Tetum",
    "Tongan",
    # Mauritian Creole
    "Torres Strait Creole",
    "Papiamentu",
    "Lao",
    "Malagasy",
    "Interlingue",
    "Aragonese",
    "Istriot",
    "Sumerian",
    "Proto-Celtic",
    "Võro",
    # Proto-Polynesian
    "Nepali",
    "Chickasaw",
    "Akkadian",
    "Middle Armenian",
    "Cimbrian",
    "Somali",
    "Sardinian",
    "Tocharian B",
    "Telugu",
    "Javanese",
    "Taos",
    "Proto-Semitic",
    # Old Prussian
    "Kyrgyz",
    "Corsican",
    "Veps",
    "Baluchi",
    "Middle Low German",
    "Middle High German",
    "Uyghur",
    # Dutch Low Saxon
    "Belarusian",
    "Guaraní",
    "Undetermined",
    "Inuktitut",
    "Tocharian A",
    "Nigerian Pidgin",
    # Gallo
    # Saterland Frisian
    "Punjabi",
    "Proto-Algonquian",
    # Istro-Romanian
    "Wiradhuri",
    "Sichuan Yi",
    "Wu",
    # White Hmong
    "Ugaritic",
    "Sundanese",
    # Old East Slavic
    "Fala",
    # Elfdalian
    "Tamil",
    "Pijin",
    "Okinawan",
    "Kazakh",
    "Hindi",
    "Tuvan",
    "Polabian",
    "Aramaic",
    "Malayalam",
    "Kumyk",
    "Inari Sami",
    "Ilocano",
    "Tswana",
    "Libyan Arabic",
    "Latgalian",
    "Yakut",
    "Sindhi",
    "Khmer",
    "Gamilaraay",
    "Ojibwe",
    "Choctaw",
    "Chinese",
    "Chamorro",
    "Yucatec Maya",
    "Picard",
    "Ngarrindjeri",
    "Kott",
    "Ingrian",
    # Crimean Gothic
    "Chamicuro",
    "Rajasthani",
    # Old Tupi
    "Old Spanish",
    "Gagauz",
    "Extremaduran",
    "Chinook Jargon",
    "Cahuilla",
    "Kannada",
    "Iban",
    "American Sign Language",
    "Adyghe",
    "Warlpiri",
    "Tibetan",
    "Ossetian",
    "Meriam",
    "Marshallese",
    "Khakas",
    "Balinese",
    "Zhuang",
    "Tuvaluan",
    "Niuean",
    "Martuthunira",
    "Guugu Yimidhirr",
    "Chechen",
    "Campidanese Sardinian",
    "Tolai",
    # Old Javanese
    "Nahuatl",
    "Lombard",
    "West Coast Bajau",
    "Romagnol",
    "Middle Irish",
    "Yoruba",
    "Wangaaybuwan-Ngiyambaa",
    # Old Swedish
    "Lingala",
    "Fiji Hindi",
    "Shabo",
    "Sasak",
    "Judeo-Arabic",
    "Central Kurdish",
    "Bislama",
]

def test_wiktionary_languages():
    seen_codes = {}
    for lang_name in LANGUAGE_NAMES:
        if lang_name.startswith('Proto-'):
            lang_name = lang_name[6:]
        code = str(find_name('language', lang_name, 'en'))
        assert code not in seen_codes, \
            "%r and %r have the same code" % (seen_codes[code], lang_name)
        seen_codes[code] = lang_name
