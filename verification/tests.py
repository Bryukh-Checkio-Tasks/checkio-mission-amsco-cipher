"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": ['oruoreemdstmioitlpslam', 4123],
            "answer": "loremipsumdolorsitamet",
            "explanation": [['l', 'or', 'e', 'mi'], ['ps', 'u', 'md', 'o'], ['l', 'or', 's', 'it'], ['am', 'e', 't']]
        },
        {
            "input": ['kicheco', 23415],
            "answer": "checkio",
            "explanation": [['c', 'he', 'c', 'ki', 'o']]
        },
        {
            "input": ['hreulhemooowywiotorwaolmmr', 123],
            "answer": "howareyouwillhometommorrow",
            "explanation": [['h', 'ow', 'a'], ['re', 'y', 'o'], ['u', 'wi', 'l'], ['lh', 'o', 'm'], ['e', 'to', 'm'],
                            ['mo', 'r', 'r'], ['o', 'w']]
        },
    ],
    "Extra": [
        {
            "input": [
                'itohdeindiiwaoutdtagrrhedpprkelfbpechowealrstenoeloeoofsetsiuurlroerexowtenasioivethetusxpterusnsvoeserthtrsrcoqreainorpsnpfpaslycicihipplaakosunrneteexpaoflrubmaodiiitieboknuatuueeinineuirabeieoceshncmlemuyisangpnwiconemhcheofmeriejseaeleaodtaslcohmerrevsobitibeomsiancgrsoumofpraallmtoaeaiattasoneeorscaausoopuyenatlagaesrtasticnatnwduretehisdleisbgplfndcngehetfhsctaurusuenourenseaypanyodeielsaulanhpaeatbailenureganyacsoulthothunhosldsetutsoweionncxfuswhresicanccioctansasutnltincapadoucysnteeretilaneisplisbewhplnteetrlthosutnoubuarccoipomu',
                78145623],
            "answer": "butimustexplaintoyouhowallthismistakenideaofdenouncingpleasureandpraisingpainwasbornandiwillgiveyouacompleteaccountofthesystemandexpoundtheactualteachingsofthegreatexplorerofthetruththemasterbuilderofhumanhappinessnoonerejectsdislikesoravoidspleasureitselfbecauseitispleasurebutbecausethosewhodonotknowhowtopursuepleasurerationallyencounterconsequencesthatareextremelypainfulnoragainisthereanyonewholovesorpursuesordesirestoobtainpainofitselfbecauseitispainbutbecauseoccasionallycircumstancesoccurinwhichtoilandpaincanprocurehimsomegreatpleasure",
            "explanation": [['b', 'ut', 'i', 'mu', 's', 'te', 'x', 'pl'], ['ai', 'n', 'to', 'y', 'ou', 'h', 'ow', 'a'],
                            ['l', 'lt', 'h', 'is', 'm', 'is', 't', 'ak'], ['en', 'i', 'de', 'a', 'of', 'd', 'en', 'o'],
                            ['u', 'nc', 'i', 'ng', 'p', 'le', 'a', 'su'], ['re', 'a', 'nd', 'p', 'ra', 'i', 'si', 'n'],
                            ['g', 'pa', 'i', 'nw', 'a', 'sb', 'o', 'rn'], ['an', 'd', 'iw', 'i', 'll', 'g', 'iv', 'e'],
                            ['y', 'ou', 'a', 'co', 'm', 'pl', 'e', 'te'], ['ac', 'c', 'ou', 'n', 'to', 'f', 'th', 'e'],
                            ['s', 'ys', 't', 'em', 'a', 'nd', 'e', 'xp'], ['ou', 'n', 'dt', 'h', 'ea', 'c', 'tu', 'a'],
                            ['l', 'te', 'a', 'ch', 'i', 'ng', 's', 'of'], ['th', 'e', 'gr', 'e', 'at', 'e', 'xp', 'l'],
                            ['o', 're', 'r', 'of', 't', 'he', 't', 'ru'], ['th', 't', 'he', 'm', 'as', 't', 'er', 'b'],
                            ['u', 'il', 'd', 'er', 'o', 'fh', 'u', 'ma'], ['nh', 'a', 'pp', 'i', 'ne', 's', 'sn', 'o'],
                            ['o', 'ne', 'r', 'ej', 'e', 'ct', 's', 'di'], ['sl', 'i', 'ke', 's', 'or', 'a', 'vo', 'i'],
                            ['d', 'sp', 'l', 'ea', 's', 'ur', 'e', 'it'], ['se', 'l', 'fb', 'e', 'ca', 'u', 'se', 'i'],
                            ['t', 'is', 'p', 'le', 'a', 'su', 'r', 'eb'], ['ut', 'b', 'ec', 'a', 'us', 'e', 'th', 'o'],
                            ['s', 'ew', 'h', 'od', 'o', 'no', 't', 'kn'], ['ow', 'h', 'ow', 't', 'op', 'u', 'rs', 'u'],
                            ['e', 'pl', 'e', 'as', 'u', 're', 'r', 'at'], ['io', 'n', 'al', 'l', 'ye', 'n', 'co', 'u'],
                            ['n', 'te', 'r', 'co', 'n', 'se', 'q', 'ue'], ['nc', 'e', 'st', 'h', 'at', 'a', 're', 'e'],
                            ['x', 'tr', 'e', 'me', 'l', 'yp', 'a', 'in'], ['fu', 'l', 'no', 'r', 'ag', 'a', 'in', 'i'],
                            ['s', 'th', 'e', 're', 'a', 'ny', 'o', 'ne'], ['wh', 'o', 'lo', 'v', 'es', 'o', 'rp', 'u'],
                            ['r', 'su', 'e', 'so', 'r', 'de', 's', 'ir'], ['es', 't', 'oo', 'b', 'ta', 'i', 'np', 'a'],
                            ['i', 'no', 'f', 'it', 's', 'el', 'f', 'be'], ['ca', 'u', 'se', 'i', 'ti', 's', 'pa', 'i'],
                            ['n', 'bu', 't', 'be', 'c', 'au', 's', 'eo'], ['cc', 'a', 'si', 'o', 'na', 'l', 'ly', 'c'],
                            ['i', 'rc', 'u', 'ms', 't', 'an', 'c', 'es'], ['oc', 'c', 'ur', 'i', 'nw', 'h', 'ic', 'h'],
                            ['t', 'oi', 'l', 'an', 'd', 'pa', 'i', 'nc'], ['an', 'p', 'ro', 'c', 'ur', 'e', 'hi', 'm'],
                            ['s', 'om', 'e', 'gr', 'e', 'at', 'p', 'le'], ['as', 'u', 're']]
        },
        {
            "input": [
                'arewoiomrlioheexteverrichesanaridwslupiceetisouwahunfoukcoavetarlokvttfnteeolamleidsinyraracfhirnstieanarblsdtiksgoasalgnavudbacpthslisemnfybetarntansttheatimaeheticlceledorpstweegidicadtoarcvodtiindpeyoroatoarggmannfhaneherliatiyarndmfhesannelisehnbghtsemauasereytelitsaaapatr',
                413652],
            "answer": "farfarawaybehindthewordmountainsfarfromthecountriesvokaliaandconsonantiatherelivetheblindtextsseparatedtheyliveinbookmarksgroverightatthecoastofthesemanticsalargelanguageoceanasmallrivernameddudenflowsbytheirplaceandsuppliesitwiththenecessaryregelialiaitisaparadisematiccountry",
            "explanation": [['f', 'ar', 'f', 'ar', 'a', 'wa'], ['yb', 'e', 'hi', 'n', 'dt', 'h'],
                            ['e', 'wo', 'r', 'dm', 'o', 'un'], ['ta', 'i', 'ns', 'f', 'ar', 'f'],
                            ['r', 'om', 't', 'he', 'c', 'ou'], ['nt', 'r', 'ie', 's', 'vo', 'k'],
                            ['a', 'li', 'a', 'an', 'd', 'co'], ['ns', 'o', 'na', 'n', 'ti', 'a'],
                            ['t', 'he', 'r', 'el', 'i', 've'], ['th', 'e', 'bl', 'i', 'nd', 't'],
                            ['e', 'xt', 's', 'se', 'p', 'ar'], ['at', 'e', 'dt', 'h', 'ey', 'l'],
                            ['i', 've', 'i', 'nb', 'o', 'ok'], ['ma', 'r', 'ks', 'g', 'ro', 'v'],
                            ['e', 'ri', 'g', 'ht', 'a', 'tt'], ['he', 'c', 'oa', 's', 'to', 'f'],
                            ['t', 'he', 's', 'em', 'a', 'nt'], ['ic', 's', 'al', 'a', 'rg', 'e'],
                            ['l', 'an', 'g', 'ua', 'g', 'eo'], ['ce', 'a', 'na', 's', 'ma', 'l'],
                            ['l', 'ri', 'v', 'er', 'n', 'am'], ['ed', 'd', 'ud', 'e', 'nf', 'l'],
                            ['o', 'ws', 'b', 'yt', 'h', 'ei'], ['rp', 'l', 'ac', 'e', 'an', 'd'],
                            ['s', 'up', 'p', 'li', 'e', 'si'], ['tw', 'i', 'th', 't', 'he', 'n'],
                            ['e', 'ce', 's', 'sa', 'r', 'yr'], ['eg', 'e', 'li', 'a', 'li', 'a'],
                            ['i', 'ti', 's', 'ap', 'a', 'ra'], ['di', 's', 'em', 'a', 'ti', 'c'],
                            ['c', 'ou', 'n', 'tr', 'y']]
        },
        {
            "input": [
                'woeassfmoheofscwiemaeareishtelulepprbshitmqunneahoadrnkesntenertiwleyeepndmsutsuhtrareaygaeitnretesyulsrnphithelelmncswadissiayieoeeeericegleupaaglaenaelveaswhtvamoumernhereiageefellinuaalshosoesttmohiyoladfhsthicaeboinarfantsofnteiytsncfsioreeifiagrnoieltvauhenesrftelitutatehncfuynpnireeesgwowhiancxitwhethsemheaodiiseaisttmieiogarepmettasaanhovythodtaikeeonfoydbrsstsadenaksenlesiriehmaontofeposfoslimmynrbxseeletlenldbwietttndtertttehelswreaistufamblosaweannerriteiotikwngnnjyrteheeintcrrofksoddsequntrxhactsblensthmoyhawerhnwlleiarndirppcpeefmnstmtory',
                312564],
            "answer": "awonderfulserenityhastakenpossessionofmyentiresoullikethesesweetmorningsofspringwhichienjoywithmywholeheartiamaloneandfeelthecharmofexistenceinthisspotwhichwascreatedfortheblissofsoulslikemineiamsohappymydearfriendsoabsorbedintheexquisitesenseofmeretranquilexistencethatineglectmytalentsishouldbeincapableofdrawingasinglestrokeatthepresentmomentandyetifeelthatineverwasagreaterartistthannowwhenwhilethelovelyvalleyteemswithvapouraroundmeandthemeridiansunstrikestheuppersurfaceoftheimpenetrablefoliageofmytreesandbutafewstraygleamsstealintotheinnersanctuary",
            "explanation": [['a', 'wo', 'n', 'de', 'r', 'fu'], ['ls', 'e', 're', 'n', 'it', 'y'],
                            ['h', 'as', 't', 'ak', 'e', 'np'], ['os', 's', 'es', 's', 'io', 'n'],
                            ['o', 'fm', 'y', 'en', 't', 'ir'], ['es', 'o', 'ul', 'l', 'ik', 'e'],
                            ['t', 'he', 's', 'es', 'w', 'ee'], ['tm', 'o', 'rn', 'i', 'ng', 's'],
                            ['o', 'fs', 'p', 'ri', 'n', 'gw'], ['hi', 'c', 'hi', 'e', 'nj', 'o'],
                            ['y', 'wi', 't', 'hm', 'y', 'wh'], ['ol', 'e', 'he', 'a', 'rt', 'i'],
                            ['a', 'ma', 'l', 'on', 'e', 'an'], ['df', 'e', 'el', 't', 'he', 'c'],
                            ['h', 'ar', 'm', 'of', 'e', 'xi'], ['st', 'e', 'nc', 'e', 'in', 't'],
                            ['h', 'is', 's', 'po', 't', 'wh'], ['ic', 'h', 'wa', 's', 'cr', 'e'],
                            ['a', 'te', 'd', 'fo', 'r', 'th'], ['eb', 'l', 'is', 's', 'of', 's'],
                            ['o', 'ul', 's', 'li', 'k', 'em'], ['in', 'e', 'ia', 'm', 'so', 'h'],
                            ['a', 'pp', 'y', 'my', 'd', 'ea'], ['rf', 'r', 'ie', 'n', 'ds', 'o'],
                            ['a', 'bs', 'o', 'rb', 'e', 'di'], ['nt', 'h', 'ee', 'x', 'qu', 'i'],
                            ['s', 'it', 'e', 'se', 'n', 'se'], ['of', 'm', 'er', 'e', 'tr', 'a'],
                            ['n', 'qu', 'i', 'le', 'x', 'is'], ['te', 'n', 'ce', 't', 'ha', 't'],
                            ['i', 'ne', 'g', 'le', 'c', 'tm'], ['yt', 'a', 'le', 'n', 'ts', 'i'],
                            ['s', 'ho', 'u', 'ld', 'b', 'ei'], ['nc', 'a', 'pa', 'b', 'le', 'o'],
                            ['f', 'dr', 'a', 'wi', 'n', 'ga'], ['si', 'n', 'gl', 'e', 'st', 'r'],
                            ['o', 'ke', 'a', 'tt', 'h', 'ep'], ['re', 's', 'en', 't', 'mo', 'm'],
                            ['e', 'nt', 'a', 'nd', 'y', 'et'], ['if', 'e', 'el', 't', 'ha', 't'],
                            ['i', 'ne', 'v', 'er', 'w', 'as'], ['ag', 'r', 'ea', 't', 'er', 'a'],
                            ['r', 'ti', 's', 'tt', 'h', 'an'], ['no', 'w', 'wh', 'e', 'nw', 'h'],
                            ['i', 'le', 't', 'he', 'l', 'ov'], ['el', 'y', 'va', 'l', 'le', 'y'],
                            ['t', 'ee', 'm', 'sw', 'i', 'th'], ['va', 'p', 'ou', 'r', 'ar', 'o'],
                            ['u', 'nd', 'm', 'ea', 'n', 'dt'], ['he', 'm', 'er', 'i', 'di', 'a'],
                            ['n', 'su', 'n', 'st', 'r', 'ik'], ['es', 't', 'he', 'u', 'pp', 'e'],
                            ['r', 'su', 'r', 'fa', 'c', 'eo'], ['ft', 'h', 'ei', 'm', 'pe', 'n'],
                            ['e', 'tr', 'a', 'bl', 'e', 'fo'], ['li', 'a', 'ge', 'o', 'fm', 'y'],
                            ['t', 're', 'e', 'sa', 'n', 'db'], ['ut', 'a', 'fe', 'w', 'st', 'r'],
                            ['a', 'yg', 'l', 'ea', 'm', 'ss'], ['te', 'a', 'li', 'n', 'to', 't'],
                            ['h', 'ei', 'n', 'ne', 'r', 'sa'], ['nc', 't', 'ua', 'r', 'y']]
        },
        {
            "input": ['donipnigapmeeliodoseitengogenmiatuemmtmalsieuelorescalanorsctinceeasutratdolsamcodaelor',
                      673428915],
            "answer": "loremipsumdolorsitametconsectetueradipiscingelitaeneancommodoligulaegetdoloraeneanmassa",
            "explanation": [['l', 'or', 'e', 'mi', 'p', 'su', 'm', 'do', 'l'],
                            ['or', 's', 'it', 'a', 'me', 't', 'co', 'n', 's'],
                            ['e', 'ct', 'e', 'tu', 'e', 'ra', 'd', 'ip', 'i'],
                            ['sc', 'i', 'ng', 'e', 'li', 't', 'ae', 'n', 'e'],
                            ['a', 'nc', 'o', 'mm', 'o', 'do', 'l', 'ig', 'u'],
                            ['la', 'e', 'ge', 't', 'do', 'l', 'or', 'a', 'e'], ['n', 'ea', 'n', 'ma', 's', 'sa']]
        },
        {
            "input": ['qjuyrvetfoluimdoowrhexazcpsgnakbo', 361479258],
            "answer": "thequickbrownfoxjumpsoveralazydog",
            "explanation": [['t', 'he', 'q', 'ui', 'c', 'kb', 'r', 'ow', 'n'],
                            ['fo', 'x', 'ju', 'm', 'ps', 'o', 've', 'r', 'a'], ['l', 'az', 'y', 'do', 'g']]
        },
        {
            "input": ['llonipaolossesicscegurorrseieniloasueueeomgeadooadtoddmapamtngcaenmitteianlaemtcrlimetn',
                      13276485],
            "answer": "loremipsumdolorsitametconsectetueradipiscingelitaeneancommodoligulaegetdoloraeneanmassa",
            "explanation": [['l', 'or', 'e', 'mi', 'p', 'su', 'm', 'do'], ['lo', 'r', 'si', 't', 'am', 'e', 'tc', 'o'],
                            ['n', 'se', 'c', 'te', 't', 'ue', 'r', 'ad'], ['ip', 'i', 'sc', 'i', 'ng', 'e', 'li', 't'],
                            ['a', 'en', 'e', 'an', 'c', 'om', 'm', 'od'], ['ol', 'i', 'gu', 'l', 'ae', 'g', 'et', 'd'],
                            ['o', 'lo', 'r', 'ae', 'n', 'ea', 'n', 'ma'], ['ss', 'a']]
        },
        {
            "input": ['pmeeliodoslorescalanorsctinceeamcodaelorsutratdolsaeitengogenlsieuedonipnigamiatuemmtma',
                      236915487],
            "answer": "loremipsumdolorsitametconsectetueradipiscingelitaeneancommodoligulaegetdoloraeneanmassa",
            "explanation": [['l', 'or', 'e', 'mi', 'p', 'su', 'm', 'do', 'l'],
                            ['or', 's', 'it', 'a', 'me', 't', 'co', 'n', 's'],
                            ['e', 'ct', 'e', 'tu', 'e', 'ra', 'd', 'ip', 'i'],
                            ['sc', 'i', 'ng', 'e', 'li', 't', 'ae', 'n', 'e'],
                            ['a', 'nc', 'o', 'mm', 'o', 'do', 'l', 'ig', 'u'],
                            ['la', 'e', 'ge', 't', 'do', 'l', 'or', 'a', 'e'], ['n', 'ea', 'n', 'ma', 's', 'sa']]
        },
        {
            "input": ['owekbsoguiuzyqxjacmpdrovheoaltnfr', 87435261],
            "answer": "thequickbrownfoxjumpsoveralazydog",
            "explanation": [['t', 'he', 'q', 'ui', 'c', 'kb', 'r', 'ow'], ['nf', 'o', 'xj', 'u', 'mp', 's', 'ov', 'e'],
                            ['r', 'al', 'a', 'zy', 'd', 'og']]
        },
        {
            "input": ['kbsogoweheoalrovqxjacmpdtnfruiuzy', 73586142],
            "answer": "thequickbrownfoxjumpsoveralazydog",
            "explanation": [['t', 'he', 'q', 'ui', 'c', 'kb', 'r', 'ow'], ['nf', 'o', 'xj', 'u', 'mp', 's', 'ov', 'e'],
                            ['r', 'al', 'a', 'zy', 'd', 'og']]
        },
        {
            "input": ['herxjeydqowuraotkboovzuinmplgcfsa', 31245],
            "answer": "thequickbrownfoxjumpsoveralazydog",
            "explanation": [['t', 'he', 'q', 'ui', 'c'], ['kb', 'r', 'ow', 'n', 'f'], ['o', 'xj', 'u', 'mp', 's'],
                            ['ov', 'e', 'ra', 'l', 'a'], ['z', 'yd', 'o', 'g']]
        },
    ]
}
