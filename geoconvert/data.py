# -*- coding: utf8 -*-

regions = {
    "42": "alsace",                         # old region (pre 2016)
    "72": "aquitaine",                      # old region (pre 2016)
    "83": "auvergne",                       # old region (pre 2016)
    "26": "bourgogne",                      # old region (pre 2016)
    "53": "bretagne",
    "24": "centre",
    "21": "champagne ardenne",              # old region (pre 2016)
    "94": "corse",
    "43": "franche comte",                  # old region (pre 2016)
    "01": "guadeloupe",
    "03": "guyane",
    "11": "ile de france",
    "91": "languedoc roussillon",           # old region (pre 2016)
    "74": "limousin",                       # old region (pre 2016)
    "41": "lorraine",                       # old region (pre 2016)
    "02": "martinique",
    "06": "mayotte",
    "73": "midi pyrenees",                  # old region (pre 2016)
    "31": "nord pas de calais",             # old region (pre 2016)
    "25": "basse normandie",                # old region (pre 2016)
    "23": "haute normandie",                # old region (pre 2016)
    "52": "pays de la loire",
    "22": "picardie",                       # old region (pre 2016)
    "54": "poitou charentes",               # old region (pre 2016)
    "93": "provence alpes cote d'azur",
    "04": "reunion",
    "82": "rhone alpes",                    # old region (pre 2016)
    # New regions (2018)
    "84": "auvergne rhone alpes",                   # chef lieu: Lyon
    "27": "bourgogne franche comte",                # chef lieu: Dijon
    "24": "centre val de loire",                    # chef lieu: Orleans
    "44": "grand est",                              # chef lieu: strasbourg
    "32": "hauts de france",                        # chef lieu: Lille
    "75": "nouvelle aquitaine",                     # chef lieu: Bordeaux
    "76": "occitanie",                              # chef lieu: Toulouse
    "28": "normandie",                              # chef lieu: Rouen
}

# Region ID => Dept chef lieu id, (List of region"s dept)
principal_places = {
    "42": ("67", ["67", "68"]),
    "72": ("33", ["24", "33", "40", "47", "64"]),
    "83": ("63", ["03", "15", "43", "63"]),
    "26": ("21", ["21", "58", "71", "89"]),
    "53": ("35", ["22", "29", "35", "56"]),
    "24": ("45", ["18", "28", "36", "37", "41", "45"]),
    "21": ("51", ["08", "10", "51", "52"]),
    "94": ("20A", ["20A", "20B"]),
    "43": ("25", ["25", "39", "70", "90"]),
    "01": ("971", ["971"]),
    "03": ("973", ["973"]),
    "11": ("75", ["75", "77", "78", "91", "92", "93", "94", "95"]),
    "91": ("34", ["11", "30", "34", "48", "66"]),
    "74": ("87", ["19", "23", "87"]),
    "41": ("57", ["54", "55", "57", "88"]),
    "02": ("972", ["972"]),
    "06": ("976", ["976"]),
    "73": ("31", ["09", "12", "31", "32", "46", "65", "81", "82"]),
    "31": ("59", ["59", "62"]),
    "25": ("14", ["14", "50", "61"]),
    "23": ("76", ["27", "76"]),
    "52": ("44", ["44", "49", "53", "72", "85"]),
    "22": ("80", ["02", "60", "80"]),
    "54": ("86", ["16", "17", "79", "86"]),
    "93": ("13", ["04", "05", "06", "13", "83", "84"]),
    "04": ("974", ["974"]),
    "82": ("69", ["01", "07", "26", "38", "42", "69", "73", "74"]),
    # New regions (2016)
    "44": # merges 41, 42, 21
        ("67", ["67", "68", "54", "55", "57", "88", "08", "10", "51", "52"]),
    "75": # merges 72, 54, 74
        ("33", ["24", "33", "40", "47", "64", "19", "23", "87", "16", "17", "79", "86"]),
    "84": # merges 82, 83
        ("69", ["03", "15", "43", "63", "01", "07", "26", "38", "42", "69", "73", "74"]),
    "27": # merges 26, 43
        ("21", ["21", "58", "71", "89", "25", "39", "70", "90"]),
    "76": # merges 73, 91
        ("31", ["11", "30", "34", "48", "66", "09", "12", "31", "32", "46", "65", "81", "82"]),
    "32": # merges 31, 22
        ("59", ["59", "62", "02", "60", "80"]),
    "28": # merges 23, 25
        ("76", ["27", "76", "14", "50", "61"]),
    "24":
        ("45", ["45", "18", "28", "36", "37", "41"]),
}

departments = {
    "01": "ain",
    "02": "aisne",
    "03": "allier",
    "04": "alpes-de-hautes-provence",
    "04": "alpes-de-haute-provence",
    "05": "hautes-alpes",
    "06": "alpes-maritimes",
    "07": "ardeche",
    "08": "ardennes",
    "09": "ariege",
    "10": "aube",
    "11": "aude",
    "12": "aveyron",
    "13": "bouches-du-rhone",
    "14": "calvados",
    "15": "cantal",
    "16": "charente",
    "17": "charente-maritime",
    "18": "cher",
    "19": "correze",
    "20A": "corse-du-sud",
    "20B": "haute-corse",
    "21": "cote-d'or",
    "22": "cotes-d'armor",
    "23": "creuse",
    "24": "dordogne",
    "25": "doubs",
    "26": "drome",
    "27": "eure",
    "28": "eure-et-loir",
    "29": "finistere",
    "30": "gard",
    "31": "haute-garonne",
    "32": "gers",
    "33": "gironde",
    "34": "herault",
    "35": "ille-et-vilaine",
    "36": "indre",
    "37": "indre-et-loire",
    "38": "isere",
    "39": "jura",
    "40": "landes",
    "41": "loir-et-cher",
    "42": "loire",
    "43": "haute-loire",
    "44": "loire-atlantique",
    "45": "loiret",
    "46": "lot",
    "47": "lot-et-garonne",
    "48": "lozere",
    "49": "maine-et-loire",
    "50": "manche",
    "51": "marne",
    "52": "haute-marne",
    "53": "mayenne",
    "54": "meurthe-et-moselle",
    "55": "meuse",
    "56": "morbihan",
    "57": "moselle",
    "58": "nievre",
    "59": "nord",
    "60": "oise",
    "61": "orne",
    "62": "pas-de-calais",
    "63": "puy-de-dome",
    "64": "pyrenees-atlantique",
    "64": "pyrenees-atlantiques",
    "65": "hautes-pyrenees",
    "66": "pyrenees-orientales",
    "67": "bas-rhin",
    "68": "haut-rhin",
    "69": "rhone",
    "70": "haute-saone",
    "71": "saone-et-loire",
    "72": "sarthe",
    "73": "savoie",
    "74": "haute-savoie",
    "75": "paris",
    "76": "seine-maritime",
    "77": "seine-et-marne",
    "78": "yvelines",
    "79": "deux-sevres",
    "80": "somme",
    "81": "tarn",
    "82": "tarn-et-garonne",
    "83": "var",
    "84": "vaucluse",
    "85": "vendee",
    "86": "vienne",
    "87": "haute-vienne",
    "88": "vosges",
    "89": "yonne",
    "90": "territoire-de-belfort",
    "91": "essonne",
    "92": "hauts-de-seine",
    "93": "seine-saint-denis",
    "94": "val-de-marne",
    "95": "val-d'oise",
    "971": "guadeloupe",
    "972": "martinique",
    "973": "guyane",
    "974": "la-reunion",
    "974": "ile-de-la-reunion",
    "975": "saint-pierre-et-miquelon",
    "976": "mayotte",
    "984": "terres-australes-et-antarctiques",
    "986": "wallis-et-futuna",
    "987": "polynesie-francaise",
    "988": "nouvelle-caledonie"
}


countries_fr = [
    ('afghanistan', 'AF'),
    ('afrique du sud', 'ZA'),
    ('aland', 'AX'),
    ('albanie', 'AL'),
    ('algerie', 'DZ'),
    ('allemagne', 'DE'),
    ('andorre', 'AD'),
    ('angola', 'AO'),
    ('anguilla', 'AI'),
    ('antarctique', 'AQ'),
    ('antigua et barbuda', 'AG'),
    ('antilles neerlandaises', 'AN'),
    ('arabie saoudite', 'SA'),
    ('argentine', 'AR'),
    ('armenie', 'AM'),
    ('aruba', 'AW'),
    ('australie', 'AU'),
    ('autriche', 'AT'),
    ('azerbaidjan', 'AZ'),
    ('bahamas', 'BS'),
    ('bahrein', 'BH'),
    ('bangladesh', 'BD'),
    ('barbade', 'BB'),
    ('belarus', 'BY'),
    ('belgique', 'BE'),
    ('belize', 'BZ'),
    ('benin', 'BJ'),
    ('bermudes', 'BM'),
    ('bhoutan', 'BT'),
    ('bolivie', 'BO'),
    ('bonaire, saint-eustache et saba', 'BQ'),
    ('bosnie-herzegovine', 'BA'),
    ('botswana', 'BW'),
    ('bouvet', 'BV'),
    ('bresil', 'BR'),
    ('brunei darussalam', 'BN'),
    ('bulgarie', 'BG'),
    ('burkina faso', 'BF'),
    ('burundi', 'BI'),
    ('caimanes', 'KY'),
    ('cambodge', 'KH'),
    ('cameroun', 'CM'),
    ('canada', 'CA'),
    ('cap vert', 'CV'),
    ('cap-vert', 'CV'),
    ('centrafricaine', 'CF'),
    ('chili', 'CL'),
    ('chine', 'CN'),
    ('christmas', 'CX'),
    ('chypre', 'CY'),
    ('cocos (keeling)', 'CC'),
    ('colombie', 'CO'),
    ('comores', 'KM'),
    ('rdc', 'CD'),
    ('rd congo', 'CD'),
    ('republique democratique du congo', 'CD'),
    ('kinshasa', 'CD'),
    ('brazzaville', 'CG'),
    ('congo', 'CG'),
    ('cook', 'CK'),
    ('coree', 'KR'),
    ('costa rica', 'CR'),
    ("cote d'ivoire", 'CI'),
    ('croatie', 'HR'),
    ('cuba', 'CU'),
    ('curacao', 'CW'),
    ('danemark', 'DK'),
    ('djibouti', 'DJ'),
    ('dominicaine', 'DO'),
    ('dominique', 'DM'),
    ('egypte', 'EG'),
    ('el salvador', 'SV'),
    ('emirats arabes unis', 'AE'),
    ('equateur', 'EC'),
    ('erythree', 'ER'),
    ('espagne', 'ES'),
    ('estonie', 'EE'),
    ('etats-unis', 'US'),
    ('ethiopie', 'ET'),
    ('falkland', 'FK'),
    ('feroe', 'FO'),
    ('fidji', 'FJ'),
    ('finlande', 'FI'),
    ('france', 'FR'),
    ('gabon', 'GA'),
    ('gambie', 'GM'),
    ('georgie', 'GE'),
    ('georgie du sud et les iles sandwich du sud', 'GS'),
    ('ghana', 'GH'),
    ('gibraltar', 'GI'),
    ('grece', 'GR'),
    ('grenade', 'GD'),
    ('groenland', 'GL'),
    ('guadeloupe', 'GP'),
    ('guam', 'GU'),
    ('guatemala', 'GT'),
    ('guernesey', 'GG'),
    ('guinee', 'GN'),
    ('guinee bissau', 'GW'),
    ('guinee equatoriale', 'GQ'),
    ('guinee-bissau', 'GW'),
    ('guyana', 'GY'),
    ('guyane francaise', 'GF'),
    ('haiti', 'HT'),
    ('heard', 'HM'),
    ('honduras', 'HN'),
    ('hong-kong', 'HK'),
    ('hongrie', 'HU'),
    ('ile de man', 'IM'),
    ('iles mineures eloignees des etats-unis', 'UM'),
    ('iles vierges britanniques', 'VG'),
    ('iles vierges des etats-unis', 'VI'),
    ('inde', 'IN'),
    ('indonesie', 'ID'),
    ('iran', 'IR'),
    ('iraq', 'IQ'),
    ('irlande', 'IE'),
    ('islande', 'IS'),
    ('israel', 'IL'),
    ('italie', 'IT'),
    ('jamaique', 'JM'),
    ('japon', 'JP'),
    ('jersey', 'JE'),
    ('jordanie', 'JO'),
    ('kazakhstan', 'KZ'),
    ('kenya', 'KE'),
    ('kirghizistan', 'KG'),
    ('kiribati', 'KI'),
    ('kosovo', 'KO'),
    ('koweit', 'KW'),
    ('lao', 'LA'),
    ('laos', 'LA'),
    ('lesotho', 'LS'),
    ('lettonie', 'LV'),
    ('liban', 'LB'),
    ('liberia', 'LR'),
    ('libye', 'LY'),
    ('libyenne', 'LY'),
    ('liechtenstein', 'LI'),
    ('lituanie', 'LT'),
    ('luxembourg', 'LU'),
    ('macao', 'MO'),
    ('macedoine', 'MK'),
    ('madagascar', 'MG'),
    ('malaisie', 'MY'),
    ('malawi', 'MW'),
    ('maldives', 'MV'),
    ('mali', 'ML'),
    ('malte', 'MT'),
    ('mariannes du nord', 'MP'),
    ('maroc', 'MA'),
    ('marshall', 'MH'),
    ('martinique', 'MQ'),
    ('maurice', 'MU'),
    ('mauritanie', 'MR'),
    ('mayotte', 'YT'),
    ('mexique', 'MX'),
    ('micronesie', 'FM'),
    ('moldova', 'MD'),
    ('monaco', 'MC'),
    ('mongolia', 'MN'),
    ('mongolie', 'MN'),
    ('montenegro', 'ME'),
    ('montserrat', 'MS'),
    ('mozambique', 'MZ'),
    ('myanmar', 'MM'),
    ('namibie', 'NA'),
    ('nauru', 'NR'),
    ('nepal', 'NP'),
    ('nicaragua', 'NI'),
    ('niger', 'NE'),
    ('nigeria', 'NG'),
    ('niue', 'NU'),
    ('norfolk', 'NF'),
    ('norvege', 'NO'),
    ('nouvelle-caledonie', 'NC'),
    ('nouvelle-zelande', 'NZ'),
    ('ocean indien', 'IO'),
    ('oman', 'OM'),
    ('ouganda', 'UG'),
    ('ouzbekistan', 'UZ'),
    ('pakistan', 'PK'),
    ('palaos', 'PW'),
    ('palestinien occupe', 'PS'),
    ('palestine', 'PS'),
    ('panama', 'PA'),
    ('papouasie-nouvelle-guinee', 'PG'),
    ('paraguay', 'PY'),
    ('pays-bas', 'NL'),
    ('perou', 'PE'),
    ('philippines', 'PH'),
    ('pitcairn', 'PN'),
    ('pologne', 'PL'),
    ('polynesie francaise', 'PF'),
    ('porto rico', 'PR'),
    ('portugal', 'PT'),
    ('qatar', 'QA'),
    ('reunion', 'RE'),
    ('roumanie', 'RO'),
    ('royaume-uni', 'GB'),
    ('russie', 'RU'),
    ('rwanda', 'RW'),
    ('sahara occidental', 'EH'),
    ('saint-barthelemy', 'BL'),
    ('saint-kitts-et-nevis', 'KN'),
    ('saint-marin', 'SM'),
    ('saint-martin', 'MF'),
    ('saint-pierre-et-miquelon', 'PM'),
    ('saint-vincent-et-les grenadines', 'VC'),
    ('sainte-helene', 'SH'),
    ('sainte-lucie', 'LC'),
    ('salomon', 'SB'),
    ('samoa', 'WS'),
    ('samoa americaines', 'AS'),
    ('sao tome et principe', 'ST'),
    ('sao tome-et-principe', 'ST'),
    ('sao tome & principe', 'ST'),
    ('sao tome-&-principe', 'ST'),
    ('senegal', 'SN'),
    ('serbie', 'RS'),
    ('seychelles', 'SC'),
    ('sierra leone', 'SL'),
    ('singapour', 'SG'),
    ('sint maarten', 'SX'),
    ('slovaquie', 'SK'),
    ('slovenie', 'SI'),
    ('somalie', 'SO'),
    ('soudan', 'SD'),
    ('soudan du sud', 'SS'),
    ('sri lanka', 'LK'),
    ('suede', 'SE'),
    ('suisse', 'CH'),
    ('suriname', 'SR'),
    ('surinam', 'SR'),
    ('svalbard et ile jan mayen', 'SJ'),
    ('swaziland', 'SZ'),
    ('syrienne', 'SY'),
    ('tadjikistan', 'TJ'),
    ('taiwan', 'TW'),
    ('tanzania', 'TZ'),
    ('tanzanie', 'TZ'),
    ('tchad', 'TD'),
    ('tcheque', 'CZ'),
    ('terres australes francaises', 'TF'),
    ('thailande', 'TH'),
    ('timor-leste', 'TL'),
    ('timor leste', 'TL'),
    ('togo', 'TG'),
    ('tokelau', 'TK'),
    ('tonga', 'TO'),
    ('trinite-et-tobago', 'TT'),
    ('tunisie', 'TN'),
    ('turkmenistan', 'TM'),
    ('turks et caiques', 'TC'),
    ('turquie', 'TR'),
    ('tuvalu', 'TV'),
    ('ukraine', 'UA'),
    ('uruguay', 'UY'),
    ('vanuatu', 'VU'),
    ('vatican', 'VA'),
    ('venezuela', 'VE'),
    ('viet nam', 'VN'),
    ('vietnam', 'VN'),
    ('wallis et futuna', 'WF'),
    ('yemen', 'YE'),
    ('zambie', 'ZM'),
    ('zimbabwe', 'ZW'),
]


countries_en = [
    ('afghanistan', 'AF'),
    ('albania', 'AL'),
    ('algeria', 'DZ'),
    ('american samoa', 'AS'),
    ('andorra', 'AD'),
    ('angola', 'AO'),
    ('anguilla', 'AI'),
    ('antarctica', 'AQ'),
    ('antigua and barbuda', 'AG'),
    ('argentina', 'AR'),
    ('armenia', 'AM'),
    ('aruba', 'AW'),
    ('australia', 'AU'),
    ('austria', 'AT'),
    ('azerbaijan', 'AZ'),
    ('bahamas', 'BS'),
    ('bahrain', 'BH'),
    ('bangladesh', 'BD'),
    ('barbados', 'BB'),
    ('belarus', 'BY'),
    ('belgium', 'BE'),
    ('belize', 'BZ'),
    ('benin', 'BJ'),
    ('bermuda', 'BM'),
    ('bhutan', 'BT'),
    ('bolivia', 'BO'),
    ('bolivia, plurinational state of', 'BO'),
    ('bonaire, saint eustatius and saba', 'BQ'),
    ('bosnia and herzegovina', 'BA'),
    ('botswana', 'BW'),
    ('bouvet island', 'BV'),
    ('brazil', 'BR'),
    ('british indian ocean territory', 'IO'),
    ('brunei darussalam', 'BN'),
    ('bulgaria', 'BG'),
    ('burkina faso', 'BF'),
    ('burundi', 'BI'),
    ('cambodia', 'KH'),
    ('cameroon', 'CM'),
    ('canada', 'CA'),
    ('cape verde', 'CV'),
    ('cayman islands', 'KY'),
    ('central african republic', 'CF'),
    ('chad', 'TD'),
    ('chile', 'CL'),
    ('china', 'CN'),
    ('christmas island', 'CX'),
    ('cocos (keeling) islands', 'CC'),
    ('colombia', 'CO'),
    ('comoros', 'KM'),
    ('rdc', 'CD'),
    ('rd congo', 'CD'),
    ('democratic republic of congo', 'CD'),
    ('democratic republic of the congo', 'CD'),
    ('congo, the democratic republic of the', 'CD'),
    ('congo, dem. republic', 'CD'),
    ('congo, democratic republic of', 'CD'),
    ('kinshasa', 'CD'),
    ('brazzaville', 'CG'),
    ('congo', 'CG'),
    ('cook islands', 'CK'),
    ('costa rica', 'CR'),
    ("cote d'ivoire", 'CI'),
    ("ivory coast", 'CI'),
    ('croatia', 'HR'),
    ('cuba', 'CU'),
    ('curacao', 'CW'),
    ('cyprus', 'CY'),
    ('czech republic', 'CZ'),
    ('czechia', 'CZ'),
    ('denmark', 'DK'),
    ('djibouti', 'DJ'),
    ('dominica', 'DM'),
    ('dominican republic', 'DO'),
    ('ecuador', 'EC'),
    ('egypt', 'EG'),
    ('el salvador', 'SV'),
    ('equatorial guinea', 'GQ'),
    ('eritrea', 'ER'),
    ('estonia', 'EE'),
    ('ethiopia', 'ET'),
    ('falkland islands (malvinas)', 'FK'),
    ('faroe islands', 'FO'),
    ('fiji', 'FJ'),
    ('finland', 'FI'),
    ('france', 'FR'),
    ('french guiana', 'GF'),
    ('french polynesia', 'PF'),
    ('french southern territories', 'TF'),
    ('gabon', 'GA'),
    ('gambia', 'GM'),
    ('georgia', 'GE'),
    ('germany', 'DE'),
    ('ghana', 'GH'),
    ('gibraltar', 'GI'),
    ('greece', 'GR'),
    ('greenland', 'GL'),
    ('grenada', 'GD'),
    ('guadeloupe', 'GP'),
    ('guam', 'GU'),
    ('guatemala', 'GT'),
    ('guernsey', 'GG'),
    ('guinea', 'GN'),
    ('guinea-bissau', 'GW'),
    ('guyana', 'GY'),
    ('haiti', 'HT'),
    ('heard island', 'HM'),
    ('holy see', 'VA'),
    ('honduras', 'HN'),
    ('hong kong', 'HK'),
    ('hungary', 'HU'),
    ('iceland', 'IS'),
    ('india', 'IN'),
    ('indonesia', 'ID'),
    ('iran', 'IR'),
    ('iraq', 'IQ'),
    ('ireland', 'IE'),
    ('isle of man', 'IM'),
    ('israel', 'IL'),
    ('italy', 'IT'),
    ('jamaica', 'JM'),
    ('japan', 'JP'),
    ('jersey', 'JE'),
    ('jordan', 'JO'),
    ('kazakhstan', 'KZ'),
    ('kenya', 'KE'),
    ('kiribati', 'KI'),
    ('kosovo', 'KO'),
    ('korea', 'KR'),
    ('kuwait', 'KW'),
    ('kyrgyz republic', 'KG'),
    ('kyrgyzstan', 'KG'),
    ("lao people's democratic republic", 'LA'),
    ("lao PDR", 'LA'),
    ("lao", 'LA'),
    ('laos', 'LA'),
    ('latvia', 'LV'),
    ('lebanon', 'LB'),
    ('lesotho', 'LS'),
    ('liberia', 'LR'),
    ('libya', 'LY'),
    ('libyan arab jamahiriya', 'LY'),
    ('liechtenstein', 'LI'),
    ('lithuania', 'LT'),
    ('luxembourg', 'LU'),
    ('macao', 'MO'),
    ('macedonia', 'MK'),
    ('madagascar', 'MG'),
    ('malawi', 'MW'),
    ('malaysia', 'MY'),
    ('maldives', 'MV'),
    ('mali', 'ML'),
    ('malta', 'MT'),
    ('marocco', 'MA'),
    ('marshall islands', 'MH'),
    ('martinique', 'MQ'),
    ('mauritania', 'MR'),
    ('mauritius', 'MU'),
    ('mayotte', 'YT'),
    ('mexico', 'MX'),
    ('micronesia', 'FM'),
    ('moldova', 'MD'),
    ('monaco', 'MC'),
    ('mongolia', 'MN'),
    ('montenegro', 'ME'),
    ('montserrat', 'MS'),
    ('morocco', 'MA'),
    ('mozambique', 'MZ'),
    ('myanmar', 'MM'),
    ('namibia', 'NA'),
    ('nauru', 'NR'),
    ('nepal', 'NP'),
    ('netherlands', 'NL'),
    ('netherlands antilles', 'AN'),
    ('new caledonia', 'NC'),
    ('new zealand', 'NZ'),
    ('nicaragua', 'NI'),
    ('niger', 'NE'),
    ('nigeria', 'NG'),
    ('niue', 'NU'),
    ('norfolk island', 'NF'),
    ('northern mariana islands', 'MP'),
    ('norway', 'NO'),
    ('oman', 'OM'),
    ('pakistan', 'PK'),
    ('palau', 'PW'),
    ('palestinian territory, occupied', 'PS'),
    ('state of palestine', 'PS'),
    ('palestine, state of', 'PS'),
    ('palestinian territories', 'PS'),
    ('panama', 'PA'),
    ('papua new guinea', 'PG'),
    ('paraguay', 'PY'),
    ('peru', 'PE'),
    ('philippines', 'PH'),
    ('pitcairn', 'PN'),
    ('poland', 'PL'),
    ('portugal', 'PT'),
    ('puerto rico', 'PR'),
    ('qatar', 'QA'),
    ('reunion', 'RE'),
    ('romania', 'RO'),
    ('russia', 'RU'),
    ('russian federation', 'RU'),
    ('rwanda', 'RW'),
    ('saint barthelemy', 'BL'),
    ('saint helena', 'SH'),
    ('saint kitts and nevis', 'KN'),
    ('saint lucia', 'LC'),
    ('saint martin', 'MF'),
    ('saint pierre and miquelon', 'PM'),
    ('saint vincent and the grenadines', 'VC'),
    ('samoa', 'WS'),
    ('san marino', 'SM'),
    ('sao tome and principe', 'ST'),
    ('sao tome & principe', 'ST'),
    ('saudi arabia', 'SA'),
    ('senegal', 'SN'),
    ('serbia', 'RS'),
    ('seychelles', 'SC'),
    ('sierra leone', 'SL'),
    ('singapore', 'SG'),
    ('sint maarten', 'SX'),
    ('slovakia', 'SK'),
    ('slovenia', 'SI'),
    ('solomon islands', 'SB'),
    ('somalia', 'SO'),
    ('south africa', 'ZA'),
    ('south georgia and the south sandwich islands', 'GS'),
    ('southern africa', 'ZA'),
    ('spain', 'ES'),
    ('sri lanka', 'LK'),
    ('sudan', 'SD'),
    ('south sudan', 'SS'),
    ('suriname', 'SR'),
    ('svalbard and jan mayen', 'SJ'),
    ('swaziland', 'SZ'),
    ('sweden', 'SE'),
    ('switzerland', 'CH'),
    ('syria', 'SY'),
    ('syrian arab republic', 'SY'),
    ('taiwan', 'TW'),
    ('taiwan, province of china', 'TW'),
    ('tajikistan', 'TJ'),
    ('tanzania', 'TZ'),
    ('tanzania, united republic of', 'TZ'),
    ('thailand', 'TH'),
    ('timor-leste', 'TL'),
    ('timor leste', 'TL'),
    ('togo', 'TG'),
    ('tokelau', 'TK'),
    ('tonga', 'TO'),
    ('trinidad and tobago', 'TT'),
    ('tunisia', 'TN'),
    ('turkey', 'TR'),
    ('turkmenistan', 'TM'),
    ('turks and caicos islands', 'TC'),
    ('tuvalu', 'TV'),
    ('uganda', 'UG'),
    ('ukraine', 'UA'),
    ('united arab emirates', 'AE'),
    ('united kingdom', 'GB'),
    ('usa', 'US'),
    ('united states', 'US'),
    ('united states minor outlying islands', 'UM'),
    ('uruguay', 'UY'),
    ('uzbekistan', 'UZ'),
    ('vanuatu', 'VU'),
    ('venezuela', 'VE'),
    ('venezuela, bolivarian republic of', 'VE'),
    ('viet nam', 'VN'),
    ('vietnam', 'VN'),
    ('virgin islands, british', 'VG'),
    ('virgin islands, u.s.', 'VI'),
    ('wallis and futuna', 'WF'),
    ('western sahara', 'EH'),
    ('yemen', 'YE'),
    ('zambia', 'ZM'),
    ('zimbabwe', 'ZW'),
    ('aland islands', 'AX'),
]

"""An association from country to other country depending (in some way) on them
"""
country_territories = {
    'NO': frozenset(['BV', 'SJ']),
    'NZ': frozenset(['TK']),
    'NL': frozenset(['SX', 'BQ', 'CW']),
    'UK': frozenset(['SH', 'FK', 'GS', 'IO']),
    'US': frozenset(['UM']),
    'FR': frozenset(['RE', 'TF', 'BL', 'YT', 'WF', 'NC', 'PF', 'PM', 'MQ', 'GF', 'MF', 'GP'])}
"""country_territories reciprocal"""
territory_to_country = dict(
    (t, c) for c, territories in country_territories.items() for t in territories)

capitals_fr = [
    ('abidjan', 'CI'),
    ('abou dabi', 'AE'),
    ('abuja', 'NG'),
    ('accra', 'GH'),
    ('addis abeba', 'ET'),
    ('alger', 'DZ'),
    ('amman', 'JO'),
    ('andorre', 'AD'),
    ('ankara', 'TR'),
    ('antananarivo', 'MG'),
    ('apia', 'WS'),
    ('achgabat', 'TM'),
    ('asmara', 'ER'),
    ('astana', 'KZ'),
    ('asuncion', 'PY'),
    ('athenes', 'GR'),
    ('bagdad', 'IQ'),
    ('bakou', 'AZ'),
    ('bamako', 'ML'),
    ('bandar seri begawan', 'BN'),
    ('bangkok', 'TH'),
    ('bangui', 'CF'),
    ('banjul', 'GM'),
    ('basseterre', 'KN'),
    ('beyrouth', 'LB'),
    ('belgrade', 'RS'),
    ('belmopan', 'BZ'),
    ('berlin', 'DE'),
    ('berne', 'CH'),
    ('bichkek', 'KG'),
    ('bissau', 'GW'),
    ('bogota', 'CO'),
    ('brasilia', 'BR'),
    ('bratislava', 'SK'),
    ('brazzaville', 'CG'),
    ('bridgetown', 'BB'),
    ('bruxelles', 'BE'),
    ('bucarest', 'RO'),
    ('budapest', 'HU'),
    ('buenos aires', 'AR'),
    ('bujumbura', 'BI'),
    ('le caire', 'EG'),
    ('canberra', 'AU'),
    ('caracas', 'VE'),
    ('castries', 'LC'),
    ('chisinau', 'MD'),
    ('conakry', 'GN'),
    ('copenhague', 'DK'),
    ('dakar', 'SN'),
    ('damas', 'SY'),
    ('dacca', 'BD'),
    ('dili', 'TL'),
    ('djibouti', 'DJ'),
    ('doha', 'QA'),
    ('dublin', 'IE'),
    ('freetown', 'SL'),
    ('funafuti', 'TV'),
    ('gaborone', 'BW'),
    ('georgetown', 'GY'),
    ('guatemala', 'GT'),
    ('hanoi', 'VN'),
    ('harare', 'ZW'),
    ('la havane', 'CU'),
    ('helsinki', 'FI'),
    ('honiara', 'SB'),
    ('islamabad', 'PK'),
    ('jakarta', 'ID'),
    ('djouba', 'SS'),
    ('kaboul', 'AF'),
    ('kampala', 'UG'),
    ('katmandu', 'NP'),
    ('khartoum', 'SD'),
    ('kiev', 'UA'),
    ('kigali', 'RW'),
    ('kingston', 'JM'),
    ('kingstown', 'VC'),
    ('kinshasa', 'CD'),
    ('kuala lumpur', 'MY'),
    ('koweit', 'KW'),
    ('libreville', 'GA'),
    ('lilongwe', 'MW'),
    ('lisbonne', 'PT'),
    ('ljubljana', 'SI'),
    ('lome', 'TG'),
    ('luanda', 'AO'),
    ('lusaka', 'ZM'),
    ('luxembourg', 'LU'),
    ('madrid', 'ES'),
    ('malabo', 'GQ'),
    ('male', 'MV'),
    ('managua', 'NI'),
    ('manama', 'BH'),
    ('manille', 'PH'),
    ('maputo', 'MZ'),
    ('maseru', 'LS'),
    ('mbabane', 'SZ'),
    ('lobamba', 'SZ'),
    ('londres', 'GB'),
    ('mascate', 'OM'),
    ('mexico', 'MX'),
    ('minsk', 'BY'),
    ('mogadiscio', 'SO'),
    ('monrovia', 'LR'),
    ('montevideo', 'UY'),
    ('moroni', 'KM'),
    ('moscou', 'RU'),
    ('nairobi', 'KE'),
    ('nassau', 'BS'),
    ('naypyidaw', 'MM'),
    ("n'djamena", 'TD'),
    ('new delhi', 'IN'),
    ('niamey', 'NE'),
    ('nicosie', 'CY'),
    ('nouakchott', 'MR'),
    ("nuku'alofa", 'TO'),
    ('oslo', 'NO'),
    ('ottawa', 'CA'),
    ('ouagadougou', 'BF'),
    ('olan-bator', 'MN'),
    ('panama', 'PA'),
    ('paramaribo', 'SR'),
    ('paris', 'FR'),
    ('phnom penh', 'KH'),
    ('podgorica', 'ME'),
    ('cetinje', 'ME'),
    ('port louis', 'MU'),
    ('port moresby', 'PG'),
    ('port-vila', 'VU'),
    ('port-au-prince', 'HT'),
    ("port-d'espagne", 'TT'),
    ('porto-novo', 'BJ'),
    ('cotonou', 'BJ'),
    ('prague', 'CZ'),
    ('praia', 'CV'),
    ('pretoria', 'ZA'),
    ('bloemfontein', 'ZA'),
    ('cape town', 'ZA'),
    ('rabat', 'MA'),
    ('reykjavik', 'IS'),
    ('riga', 'LV'),
    ('riyad', 'SA'),
    ('rome', 'IT'),
    ('roseau', 'DM'),
    ('san jose', 'CR'),
    ('san-marin', 'SM'),
    ('san salvador', 'SV'),
    ("sanaa", 'YE'),
    ('saint-domingue', 'DO'),
    ('sarajevo', 'BA'),
    ('skopje', 'MK'),
    ('sofia', 'BG'),
    ("saint-georges", 'GD'),
    ("saint john's", 'AG'),
    ('stockholm', 'SE'),
    ('suva', 'FJ'),
    ('tallinn', 'EE'),
    ('tarawa-sud', 'KI'),
    ('tachkent', 'UZ'),
    ('tbilisi', 'GE'),
    ('kutaisi', 'GE'),
    ('tegucigalpa', 'HN'),
    ('teheran', 'IR'),
    ('thimphou', 'BT'),
    ('tirana', 'AL'),
    ('tokyo', 'JP'),
    ('tripoli', 'LY'),
    ('tunis', 'TN'),
    ('vaduz', 'LI'),
    ('la valette', 'MT'),
    ('varsovie', 'PL'),
    ('victoria', 'SC'),
    ('vienne', 'AT'),
    ('vientiane', 'LA'),
    ('vilnius', 'LT'),
    ('washington', 'US'),
    ('wellington', 'NZ'),
    ('windhoek', 'NA'),
    ('yaounde', 'CM'),
    ('yerevan', 'AM'),
    ('zagreb', 'HR'),
    ('lima', 'PE')
]

capitals_en = [
    ('abu dhabi', 'AE'),
    ('accra', 'GH'),
    ('addis ababa', 'ET'),
    ('algiers', 'DZ'),
    ('amman', 'JO'),
    ('andorra la vella', 'AD'),
    ('ankara', 'TR'),
    ('antananarivo', 'MG'),
    ('apia', 'WS'),
    ('ashgabat', 'TM'),
    ('asmara', 'ER'),
    ('astana', 'KZ'),
    ('asuncion', 'PY'),
    ('athens', 'GR'),
    ('baghdad', 'IQ'),
    ('baku', 'AZ'),
    ('bamako', 'ML'),
    ('bandar seri begawan', 'BN'),
    ('bangkok', 'TH'),
    ('bangui', 'CF'),
    ('banjul', 'GM'),
    ('basseterre', 'KN'),
    ('beirut', 'LB'),
    ('belgrade', 'RS'),
    ('belmopan', 'BZ'),
    ('berlin', 'DE'),
    ('bern', 'CH'),
    ('bishkek', 'KG'),
    ('bissau', 'GW'),
    ('bogota', 'CO'),
    ('brasilia', 'BR'),
    ('bratislava', 'SK'),
    ('brazzaville', 'CG'),
    ('bridgetown', 'BB'),
    ('bucharest', 'RO'),
    ('budapest', 'HU'),
    ('buenos aires', 'AR'),
    ('bujumbura', 'BI'),
    ('cairo', 'EG'),
    ('canberra', 'AU'),
    ('caracas', 'VE'),
    ('castries', 'LC'),
    ('chisinau', 'MD'),
    ('conakry', 'GN'),
    ('copenhagen', 'DK'),
    ('dakar', 'SN'),
    ('damascus', 'SY'),
    ('dhaka', 'BD'),
    ('dili', 'TL'),
    ('djibouti', 'DJ'),
    ('doha', 'QA'),
    ('dublin', 'IE'),
    ('dushanbe', 'TJ'),
    ('freetown', 'SL'),
    ('funafuti', 'TV'),
    ('gaborone', 'BW'),
    ('georgetown', 'GY'),
    ('guatemala city', 'GT'),
    ('hanoi', 'VN'),
    ('harare', 'ZW'),
    ('havana', 'CU'),
    ('helsinki', 'FI'),
    ('honiara', 'SB'),
    ('islamabad', 'PK'),
    ('jakarta', 'ID'),
    ('juba', 'SS'),
    ('kabul', 'AF'),
    ('kampala', 'UG'),
    ('kathmandu', 'NP'),
    ('khartoum', 'SD'),
    ('kiev', 'UA'),
    ('kigali', 'RW'),
    ('kingston', 'JM'),
    ('kingstown', 'VC'),
    ('kinshasa', 'CD'),
    ('kuala lumpur', 'MY'),
    ('kuwait city', 'KW'),
    ('libreville', 'GA'),
    ('lilongwe', 'MW'),
    ('lisbon', 'PT'),
    ('ljubljana', 'SI'),
    ('lome', 'TG'),
    ('luanda', 'AO'),
    ('lusaka', 'ZM'),
    ('luxembourg', 'LU'),
    ('london', 'GB'),
    ('madrid', 'ES'),
    ('malabo', 'GQ'),
    ('male', 'MV'),
    ('managua', 'NI'),
    ('manama', 'BH'),
    ('manila', 'PH'),
    ('maputo', 'MZ'),
    ('maseru', 'LS'),
    ('mbabane', 'SZ'),
    ('lobamba', 'SZ'),
    ('mexico city', 'MX'),
    ('minsk', 'BY'),
    ('mogadishu', 'SO'),
    ('monrovia', 'LR'),
    ('montevideo', 'UY'),
    ('moroni', 'KM'),
    ('moscow', 'RU'),
    ('muscat', 'OM'),
    ('nairobi', 'KE'),
    ('nassau', 'BS'),
    ('naypyidaw', 'MM'),
    ("n'djamena", 'TD'),
    ('new delhi', 'IN'),
    ('niamey', 'NE'),
    ('nicosia', 'CY'),
    ('nouakchott', 'MR'),
    ("nuku'alofa", 'TO'),
    ('oslo', 'NO'),
    ('ottawa', 'CA'),
    ('ouagadougou', 'BF'),
    ('panama city', 'PA'),
    ('paramaribo', 'SR'),
    ('paris', 'FR'),
    ('phnom penh', 'KH'),
    ('podgorica', 'ME'),
    ('cetinje', 'ME'),
    ('port louis', 'MU'),
    ('port moresby', 'PG'),
    ('port vila', 'VU'),
    ('port-au-prince', 'HT'),
    ('port of spain', 'TT'),
    ('porto-novo', 'BJ'),
    ('cotonou', 'BJ'),
    ('prague', 'CZ'),
    ('praia', 'CV'),
    ('pretoria', 'ZA'),
    ('bloemfontein', 'ZA'),
    ('cape town', 'ZA'),
    ('rabat', 'MA'),
    ('reykjavik', 'IS'),
    ('riga', 'LV'),
    ('riyadh', 'SA'),
    ('rome', 'IT'),
    ('roseau', 'DM'),
    ('san jose', 'CR'),
    ('san marino', 'SM'),
    ('san salvador', 'SV'),
    ("sana'a", 'YE'),
    ('santo domingo', 'DO'),
    ('sarajevo', 'BA'),
    ('skopje', 'MK'),
    ('sofia', 'BG'),
    ("st. george's", 'GD'),
    ("st. john's", 'AG'),
    ('stockholm', 'SE'),
    ('suva', 'FJ'),
    ('tallinn', 'EE'),
    ('tarawa atoll', 'KI'),
    ('tashkent', 'UZ'),
    ('tbilisi', 'GE'),
    ('kutaisi', 'GE'),
    ('tegucigalpa', 'HN'),
    ('tehran', 'IR'),
    ('thimphu', 'BT'),
    ('tirana', 'AL'),
    ('tokyo', 'JP'),
    ('tripoli', 'LY'),
    ('tunis', 'TN'),
    ('ulaanbaatar', 'MN'),
    ('vaduz', 'LI'),
    ('valletta', 'MT'),
    ('victoria', 'SC'),
    ('vienna', 'AT'),
    ('vientiane', 'LA'),
    ('vilnius', 'LT'),
    ('warsaw', 'PL'),
    ('washington', 'US'),
    ('wellington', 'NZ'),
    ('windhoek', 'NA'),
    ('abidjan', 'CI'),
    ('yaounde', 'CM'),
    ('yerevan', 'AM'),
    ('zagreb', 'HR'),
    ('lima', 'PE')
]
