#! /usr/bin/env python 
# -*- coding: utf-8 -*-

language_id=34
language_sub_id=6
language_eng_id=18
import sys
import os

# PyDev sets PYTHONPATH, use it
try:
    for p in os.environ['PYTHONPATH'].split(':'):
        if not p in sys.path:
            sys.path.append(p)
except:
   pass

try:
    sys.path.append(os.path.join(os.environ['ANDROID_VIEW_CLIENT_HOME'], 'src'))
except:
    pass

# This must be imported before MonkeyRunner and MonkeyDevice,
# otherwise the import fails.
from com.dtmilano.android.viewclient import ViewClient, View, UiDevice
import re
#from com.android.monkeyrunner import ViewClient, MonkeyDevice, MonkeyView
RegexType = type(re.compile(''))

class ViewNotFoundException(Exception):
    '''
    ViewNotFoundException is raised when a View is not found.
    '''

    def __init__(self, attr, value, root):
        if isinstance(value, RegexType):
            msg = "Couldn't find View with %s that matches '%s' in tree with root=%s" % (attr, value.pattern, root)
        else:
            msg = "Couldn't find View with %s='%s' in tree with root=%s" % (attr, value, root)
        super(Exception, self).__init__(msg)

def changeLanguage(self, languageTo):
    LANGUAGE_SETTINGS = {
        "en":    u"Language & input",
        "af":    u"Taal en invoer",
        "am":    u"ቋንቋ እና ግቤት",
        "ar":    u"اللغة والإدخال",
        "az":    u"Dil və daxiletmə",
        "az-rAZ":    u"Dil və daxiletmə",
        "be":    u"Мова і ўвод",
        "bg":    u"Език и въвеждане",
        "ca":    u"Idioma i introducció de text",
        "cs":    u"Jazyk a zadávání",
        "da":    u"Sprog og input",
        "de":    u"Sprache & Eingabe",
        "el":    u"Γλώσσα και εισαγωγή",
        "en-rGB":    u"Language & input",
        "en-rIN":    u"Language & input",
        "es":    u"Idioma e introducción de texto",
        "es-rUS":    u"Teclado e idioma",
        "et":    u"Keeled ja sisestamine",
        "et-rEE":    u"Keeled ja sisestamine",
        "fa":    u"زبان و ورود اطلاعات",
        "fi":    u"Kieli ja syöttötapa",
        "fr":    u"Langue et saisie",
        "fr-rCA":    u"Langue et saisie",
        "hi":    u"भाषा और अक्षर",
        "hr":    u"Jezik i ulaz",
        "hu":    u"Nyelv és bevitel",
        "hy":    u"Լեզվի & ներմուծում",
        "hy-rAM":    u"Լեզու և ներմուծում",
        "in":    u"Bahasa & masukan",
        "it":    u"Lingua e immissione",
        "iw":    u"שפה וקלט",
        "ja":    u"言語と入力",
        "ka":    u"ენისა და შეყვანის პარამეტრები",
        "ka-rGE":    u"ენისა და შეყვანის პარამეტრები",
        "km":    u"ភាសា & ការ​បញ្ចូល",
        "km-rKH":    u"ភាសា & ការ​បញ្ចូល",
        "ko":    u"언어 및 키보드",
        "lo":    u"ພາສາ & ການປ້ອນຂໍ້ມູນ",
        "lo-rLA":    u"ພາສາ & ການປ້ອນຂໍ້ມູນ",
        "lt":    u"Kalba ir įvestis",
        "lv":    u"Valodas ievade",
        "mn":    u"Хэл & оруулах",
        "mn-rMN":    u"Хэл & оруулах",
        "ms":    u"Bahasa & input",
        "ms-rMY":    u"Bahasa & input",
        "nb":    u"Språk og inndata",
        "ne":    u"भाषा र इनपुट",
        "ne-rNP":    u"भाषा र इनपुट",
        "nl":    u"Taal en invoer",
        "pl":    u"Język, klawiatura, głos",
        "pt":    u"Idioma e entrada",
        "pt-rPT":    u"Idioma e entrada",
        "ro":    u"Limbă și introducere de text",
        "ru":    u"Язык и ввод",
        "si":    u"භාෂාව සහ ආදානය",
        "si-rLK":    u"භාෂාව සහ ආදානය",
        "sk":    u"Jazyk & vstup",
        "sl":    u"Jezik in vnos",
        "sr":    u"Језик и унос",
        "sv":    u"Språk och inmatning",
        "sw":    u"Lugha, Kibodi na Sauti",
        "th":    u"ภาษาและการป้อนข้อมูล",
        "tl":    u"Wika at input",
        "tr":    u"Dil ve giriş",
        "uk":    u"Мова та введення",
        "vi":    u"Ngôn ngữ & phương thức nhập",
        "zh-rCN":    u"语言和输入法",
        "zh-rHK":    u"語言與輸入裝置",
        "zh-rTW":    u"語言與輸入設定",
        "zu":    u"Ulimi & ukufakwa",
    }

    PHONE_LANGUAGE = {
        "en":    u"Language",
        "af":    u"Taal",
        "am":    u"ቋንቋ",
        "ar":    u"اللغة",
        "az":    u"Dil",
        "az-rAZ":    u"Dil",
        "be":    u"Мова",
        "bg":    u"Език",
        "ca":    u"Idioma",
        "cs":    u"Jazyk",
        "da":    u"Sprog",
        "de":    u"Sprache",
        "el":    u"Γλώσσα",
        "en-rGB":    u"Language",
        "en-rIN":    u"Language",
        "es":    u"Idioma",
        "es-rUS":    u"Idioma",
        "et":    u"Keel",
        "et-rEE":    u"Keel",
        "fa":    u"زبان",
        "fi":    u"Kieli",
        "fr":    u"Langue",
        "fr-rCA":    u"Langue",
        "hi":    u"भाषा",
        "hr":    u"Jezik",
        "hu":    u"Nyelv",
        "hy":    u"Lեզուն",
        "hy-rAM":    u"Lեզուն",
        "in":    u"Bahasa",
        "it":    u"Lingua",
        "iw":    u"שפה",
        "ja":    u"言語",
        "ka":    u"ენა",
        "ka-rGE":    u"ენა",
        "km":    u"ភាសា",
        "km-rKH":    u"ភាសា",
        "ko":    u"언어",
        "lo":    u"ພາສາ",
        "lo-rLA":    u"ພາສາ",
        "lt":    u"Kalba",
        "lv":    u"Valoda",
        "mn":    u"Хэл",
        "mn-rMN":    u"Хэл",
        "ms":    u"Bahasa",
        "ms-rMY":    u"Bahasa",
        "nb":    u"Språk",
        "ne":    u"भाषा",
        "nl":    u"Taal",
        "pl":    u"Język",
        "pt":    u"Idioma",
        "pt-rPT":    u"Idioma",
        "ro":    u"Limba",
        "ru":    u"Язык",
        "si":    u"භාෂාව",
        "si-rLK":    u"භාෂාව",
        "sk":    u"Jazyk",
        "sl":    u"Jezik",
        "sr":    u"Језик",
        "sv":    u"Språk",
        "sw":    u"Lugha",
        "th":    u"ภาษา",
        "tl":    u"Wika",
        "tr":    u"Dil",
        "uk":    u"Мова",
        "vi":    u"Ngôn ngữ",
        "zh-rCN":    u"语言",
        "zh-rHK":    u"語言",
        "zh-rTW":    u"語言",
        "zu":    u"Ulimi",
    }

    LANGUAGES = {
        "en": u"English (United States)",
        "es-rUS": u"Español (Estados Unidos)",
        "af": u"Afrikaans", # Afrikaans
        "af-rNA": u"Afrikaans (Namibië)", # Afrikaans (Namibia)
        "af-rZA": u"Afrikaans (Suid-Afrika)", # Afrikaans (South Africa)
        "agq": u"Aghem", # Aghem
        "agq-rCM": u"Aghem (Kàmàlûŋ)", # Aghem (Cameroon)
        "ak": u"Akan", # Akan
        "ak-rGH": u"Akan (Gaana)", # Akan (Ghana)
        "am": u"አማርኛ", # Amharic
        "am-rET": u"አማርኛ (ኢትዮጵያ)", # Amharic (Ethiopia)
        "ar": u"العربية", # Arabic
        "ar_001": u"العربية (العالم)", # Arabic (World)
        "ar-rAE": u"العربية (الإمارات العربية المتحدة)", # Arabic (United Arab Emirates)
        "ar-rBH": u"العربية (البحرين)", # Arabic (Bahrain)
        "ar-rDJ": u"العربية (جيبوتي)", # Arabic (Djibouti)
        "ar-rDZ": u"العربية (الجزائر)", # Arabic (Algeria)
        "ar-rEG": u"العربية (مصر)", # Arabic (Egypt)
        "ar-rEH": u"العربية (الصحراء الغربية)", # Arabic (Western Sahara)
        "ar-rER": u"العربية (أريتريا)", # Arabic (Eritrea)
        "ar-rIL": u"العربية (إسرائيل)", # Arabic (Israel)
        "ar-rIQ": u"العربية (العراق)", # Arabic (Iraq)
        "ar-rJO": u"العربية (الأردن)", # Arabic (Jordan)
        "ar-rKM": u"العربية (جزر القمر)", # Arabic (Comoros)
        "ar-rKW": u"العربية (الكويت)", # Arabic (Kuwait)
        "ar-rLB": u"العربية (لبنان)", # Arabic (Lebanon)
        "ar-rLY": u"العربية (ليبيا)", # Arabic (Libya)
        "ar-rMA": u"العربية (المغرب)", # Arabic (Morocco)
        "ar-rMR": u"العربية (موريتانيا)", # Arabic (Mauritania)
        "ar-rOM": u"العربية (عُمان)", # Arabic (Oman)
        "ar-rPS": u"العربية (فلسطين)", # Arabic (Palestine)
        "ar-rQA": u"العربية (قطر)", # Arabic (Qatar)
        "ar-rSA": u"العربية (المملكة العربية السعودية)", # Arabic (Saudi Arabia)
        "ar-rSD": u"العربية (السودان)", # Arabic (Sudan)
        "ar-rSO": u"العربية (الصومال)", # Arabic (Somalia)
        "ar-rSY": u"العربية (سوريا)", # Arabic (Syria)
        "ar-rTD": u"العربية (تشاد)", # Arabic (Chad)
        "ar-rTN": u"العربية (تونس)", # Arabic (Tunisia)
        "ar-rYE": u"العربية (اليمن)", # Arabic (Yemen)
        "as": u"অসমীয়া", # Assamese
        "as-rIN": u"অসমীয়া (ভাৰত)", # Assamese (India)
        "asa": u"Kipare", # Asu
        "asa-rTZ": u"Kipare (Tadhania)", # Asu (Tanzania)
        "az": u"Azərbaycanca", # Azerbaijani
        "az-rCYRL": u"Азәрбајҹан (CYRL)", # Azerbaijani (CYRL)
        "az-rCYRL_AZ": u"Азәрбајҹан (Азәрбајҹан,AZ)", # Azerbaijani (Azerbaijan,AZ)
        "az-rLATN": u"Azərbaycanca (LATN)", # Azerbaijani (LATN)
        "az-rLATN_AZ": u"Azərbaycanca (Azərbaycan,AZ)", # Azerbaijani (Azerbaijan,AZ)
        "bas": u"Ɓàsàa", # Basaa
        "bas-rCM": u"Ɓàsàa (Kàmɛ̀rûn)", # Basaa (Cameroon)
        "be": u"беларуская", # Belarusian
        "be-rBY": u"беларуская (Беларусь)", # Belarusian (Belarus)
        "bem": u"Ichibemba", # Bemba
        "bem-rZM": u"Ichibemba (Zambia)", # Bemba (Zambia)
        "bez": u"Hibena", # Bena
        "bez-rTZ": u"Hibena (Hutanzania)", # Bena (Tanzania)
        "bg": u"български", # Bulgarian
        "bg-rBG": u"български (България)", # Bulgarian (Bulgaria)
        "bm": u"Bamanakan", # Bambara
        "bm-rML": u"Bamanakan (Mali)", # Bambara (Mali)
        "bn": u"বাংলা", # Bengali
        "bn-rBD": u"বাংলা (বাংলাদেশ)", # Bengali (Bangladesh)
        "bn-rIN": u"বাংলা (ভারত)", # Bengali (India)
        "bo": u"པོད་སྐད་", # Tibetan
        "bo-rCN": u"པོད་སྐད་ (རྒྱ་ནག)", # Tibetan (China)
        "bo-rIN": u"པོད་སྐད་ (རྒྱ་གར་)", # Tibetan (India)
        "br": u"Brezhoneg", # Breton
        "br-rFR": u"Brezhoneg (Frañs)", # Breton (France)
        "brx": u"बड़ो", # Bodo
        "brx-rIN": u"बड़ो (भारत)", # Bodo (India)
        "bs": u"Bosanski", # Bosnian
        "bs-rCYRL": u"босански (CYRL)", # Bosnian (CYRL)
        "bs-rCYRL_BA": u"босански (Босна и Херцеговина,BA)", # Bosnian (Bosnia and Herzegovina,BA)
        "bs-rLATN": u"Bosanski (LATN)", # Bosnian (LATN)
        "bs-rLATN_BA": u"Bosanski (Bosna i Hercegovina,BA)", # Bosnian (Bosnia and Herzegovina,BA)
        "ca": u"Català", # Catalan
        "ca-rAD": u"Català (Andorra)", # Catalan (Andorra)
        "ca-rES": u"Català (Espanya)", # Catalan (Spain)
        "cgg": u"Rukiga", # Chiga
        "cgg-rUG": u"Rukiga (Uganda)", # Chiga (Uganda)
        "chr": u"ᏣᎳᎩ", # Cherokee
        "chr-rUS": u"ᏣᎳᎩ (ᎠᎹᏰᏟ)", # Cherokee (United States)
        "cs": u"čeština", # Czech
        "cs-rCZ": u"čeština (Česká republika)", # Czech (Czech Republic)
        "cy": u"Cymraeg", # Welsh
        "cy-rGB": u"Cymraeg (y Deyrnas Unedig)", # Welsh (United Kingdom)
        "da": u"Dansk", # Danish
        "da-rDK": u"Dansk (Danmark)", # Danish (Denmark)
        "dav": u"Kitaita", # Taita
        "dav-rKE": u"Kitaita (Kenya)", # Taita (Kenya)
        "de": u"Deutsch", # German
        "de-rAT": u"Deutsch (Österreich)", # German (Austria)
        "de-rBE": u"Deutsch (Belgien)", # German (Belgium)
        "de-rCH": u"Deutsch (Schweiz)", # German (Switzerland)
        "de-rDE": u"Deutsch (Deutschland)", # German (Germany)
        "de-rLI": u"Deutsch (Liechtenstein)", # German (Liechtenstein)
        "de-rLU": u"Deutsch (Luxemburg)", # German (Luxembourg)
        "dje": u"Zarmaciine", # Zarma
        "dje-rNE": u"Zarmaciine (Nižer)", # Zarma (Niger)
        "dua": u"Duálá", # Duala
        "dua-rCM": u"Duálá (Cameroun)", # Duala (Cameroon)
        "dyo": u"Joola", # Jola-Fonyi
        "dyo-rSN": u"Joola (Senegal)", # Jola-Fonyi (Senegal)
        "dz": u"རྫོང་ཁ", # Dzongkha
        "dz-rBT": u"རྫོང་ཁ (འབྲུག)", # Dzongkha (Bhutan)
        "ebu": u"Kĩembu", # Embu
        "ebu-rKE": u"Kĩembu (Kenya)", # Embu (Kenya)
        "ee": u"Eʋegbe", # Ewe
        "ee-rGH": u"Eʋegbe (Ghana nutome)", # Ewe (Ghana)
        "ee-rTG": u"Eʋegbe (Togo nutome)", # Ewe (Togo)
        "el": u"Ελληνικά", # Greek
        "el-rCY": u"Ελληνικά (Κύπρος)", # Greek (Cyprus)
        "el-rGR": u"Ελληνικά (Ελλάδα)", # Greek (Greece)
        "en": u"English", # English
        "en_150": u"English (Europe)", # English (Europe)
        "en-rAG": u"English (Antigua and Barbuda)", # English (Antigua and Barbuda)
        "en-rAS": u"English (American Samoa)", # English (American Samoa)
        "en-rAU": u"English (Australia)", # English (Australia)
        "en-rBB": u"English (Barbados)", # English (Barbados)
        "en-rBE": u"English (Belgium)", # English (Belgium)
        "en-rBM": u"English (Bermuda)", # English (Bermuda)
        "en-rBS": u"English (Bahamas)", # English (Bahamas)
        "en-rBW": u"English (Botswana)", # English (Botswana)
        "en-rBZ": u"English (Belize)", # English (Belize)
        "en-rCA": u"English (Canada)", # English (Canada)
        "en-rCM": u"English (Cameroon)", # English (Cameroon)
        "en-rDM": u"English (Dominica)", # English (Dominica)
        "en-rFJ": u"English (Fiji)", # English (Fiji)
        "en-rFM": u"English (Micronesia)", # English (Micronesia)
        "en-rGB": u"English (United Kingdom)", # English (United Kingdom)
        "en-rGD": u"English (Grenada)", # English (Grenada)
        "en-rGG": u"English (Guernsey)", # English (Guernsey)
        "en-rGH": u"English (Ghana)", # English (Ghana)
        "en-rGI": u"English (Gibraltar)", # English (Gibraltar)
        "en-rGM": u"English (Gambia)", # English (Gambia)
        "en-rGU": u"English (Guam)", # English (Guam)
        "en-rGY": u"English (Guyana)", # English (Guyana)
        "en-rHK": u"English (Hong Kong)", # English (Hong Kong)
        "en-rIE": u"English (Ireland)", # English (Ireland)
        "en-rIM": u"English (Isle of Man)", # English (Isle of Man)
        "en-rIN": u"English (India)", # English (India)
        "en-rJE": u"English (Jersey)", # English (Jersey)
        "en-rJM": u"English (Jamaica)", # English (Jamaica)
        "en-rKE": u"English (Kenya)", # English (Kenya)
        "en-rKI": u"English (Kiribati)", # English (Kiribati)
        "en-rKN": u"English (Saint Kitts and Nevis)", # English (Saint Kitts and Nevis)
        "en-rKY": u"English (Cayman Islands)", # English (Cayman Islands)
        "en-rLC": u"English (Saint Lucia)", # English (Saint Lucia)
        "en-rLR": u"English (Liberia)", # English (Liberia)
        "en-rLS": u"English (Lesotho)", # English (Lesotho)
        "en-rMG": u"English (Madagascar)", # English (Madagascar)
        "en-rMH": u"English (Marshall Islands)", # English (Marshall Islands)
        "en-rMP": u"English (Northern Mariana Islands)", # English (Northern Mariana Islands)
        "en-rMT": u"English (Malta)", # English (Malta)
        "en-rMU": u"English (Mauritius)", # English (Mauritius)
        "en-rMW": u"English (Malawi)", # English (Malawi)
        "en-rNA": u"English (Namibia)", # English (Namibia)
        "en-rNG": u"English (Nigeria)", # English (Nigeria)
        "en-rNZ": u"English (New Zealand)", # English (New Zealand)
        "en-rPG": u"English (Papua New Guinea)", # English (Papua New Guinea)
        "en-rPH": u"English (Philippines)", # English (Philippines)
        "en-rPK": u"English (Pakistan)", # English (Pakistan)
        "en-rPR": u"English (Puerto Rico)", # English (Puerto Rico)
        "en-rPW": u"English (Palau)", # English (Palau)
        "en-rSB": u"English (Solomon Islands)", # English (Solomon Islands)
        "en-rSC": u"English (Seychelles)", # English (Seychelles)
        "en-rSG": u"English (Singapore)", # English (Singapore)
        "en-rSL": u"English (Sierra Leone)", # English (Sierra Leone)
        "en-rSS": u"English (South Sudan)", # English (South Sudan)
        "en-rSZ": u"English (Swaziland)", # English (Swaziland)
        "en-rTC": u"English (Turks and Caicos Islands)", # English (Turks and Caicos Islands)
        "en-rTO": u"English (Tonga)", # English (Tonga)
        "en-rTT": u"English (Trinidad and Tobago)", # English (Trinidad and Tobago)
        "en-rTZ": u"English (Tanzania)", # English (Tanzania)
        "en-rUG": u"English (Uganda)", # English (Uganda)
        "en-rUM": u"English (U.S. Outlying Islands)", # English (U.S. Outlying Islands)
        "en-rUS": u"English (United States)", # English (United States)
        "en-rUS_POSIX": u"English (United States,Computer)", # English (United States,Computer)
        "en-rVC": u"English (Saint Vincent and the Grenadines)", # English (Saint Vincent and the Grenadines)
        "en-rVG": u"English (British Virgin Islands)", # English (British Virgin Islands)
        "en-rVI": u"English (U.S. Virgin Islands)", # English (U.S. Virgin Islands)
        "en-rVU": u"English (Vanuatu)", # English (Vanuatu)
        "en-rWS": u"English (Samoa)", # English (Samoa)
        "en-rZA": u"English (South Africa)", # English (South Africa)
        "en-rZM": u"English (Zambia)", # English (Zambia)
        "en-rZW": u"English (Zimbabwe)", # English (Zimbabwe)
        "eo": u"Esperanto", # Esperanto
        "es": u"Español", # Spanish
        "es_419": u"Español (Latinoamérica)", # Spanish (Latin America)
        "es-rAR": u"Español (Argentina)", # Spanish (Argentina)
        "es-rBO": u"Español (Bolivia)", # Spanish (Bolivia)
        "es-rCL": u"Español (Chile)", # Spanish (Chile)
        "es-rCO": u"Español (Colombia)", # Spanish (Colombia)
        "es-rCR": u"Español (Costa Rica)", # Spanish (Costa Rica)
        "es-rCU": u"Español (Cuba)", # Spanish (Cuba)
        "es-rDO": u"Español (República Dominicana)", # Spanish (Dominican Republic)
        "es-rEA": u"Español (Ceuta y Melilla)", # Spanish (Ceuta and Melilla)
        "es-rEC": u"Español (Ecuador)", # Spanish (Ecuador)
        "es-rES": u"Español (España)", # Spanish (Spain)
        "es-rGQ": u"Español (Guinea Ecuatorial)", # Spanish (Equatorial Guinea)
        "es-rGT": u"Español (Guatemala)", # Spanish (Guatemala)
        "es-rHN": u"Español (Honduras)", # Spanish (Honduras)
        "es-rIC": u"Español (Islas Canarias)", # Spanish (Canary Islands)
        "es-rMX": u"Español (México)", # Spanish (Mexico)
        "es-rNI": u"Español (Nicaragua)", # Spanish (Nicaragua)
        "es-rPA": u"Español (Panamá)", # Spanish (Panama)
        "es-rPE": u"Español (Perú)", # Spanish (Peru)
        "es-rPH": u"Español (Filipinas)", # Spanish (Philippines)
        "es-rPR": u"Español (Puerto Rico)", # Spanish (Puerto Rico)
        "es-rPY": u"Español (Paraguay)", # Spanish (Paraguay)
        "es-rSV": u"Español (El Salvador)", # Spanish (El Salvador)
        "es-rUS": u"Español (Estados Unidos)", # Spanish (United States)
        "es-rUY": u"Español (Uruguay)", # Spanish (Uruguay)
        "es-rVE": u"Español (Venezuela)", # Spanish (Venezuela)
        "et": u"Eesti", # Estonian
        "et-rEE": u"Eesti (Eesti)", # Estonian (Estonia)
        "eu": u"Euskara", # Basque
        "eu-rES": u"Euskara (Espainia)", # Basque (Spain)
        "ewo": u"Ewondo", # Ewondo
        "ewo-rCM": u"Ewondo (Kamərún)", # Ewondo (Cameroon)
        "fa": u"فارسی", # Persian
        "fa-rAF": u"دری (افغانستان)", # Persian (Afghanistan)
        "fa-rIR": u"فارسی (ایران)", # Persian (Iran)
        "ff": u"Pulaar", # Fulah
        "ff-rSN": u"Pulaar (Senegaal)", # Fulah (Senegal)
        "fi": u"Suomi", # Finnish
        "fi-rFI": u"Suomi (Suomi)", # Finnish (Finland)
        "fil": u"Filipino", # Filipino
        "fil-rPH": u"Filipino (Pilipinas)", # Filipino (Philippines)
        "fo": u"Føroyskt", # Faroese
        "fo-rFO": u"Føroyskt (Føroyar)", # Faroese (Faroe Islands)
        "fr": u"Français", # French
        "fr-rBE": u"Français (Belgique)", # French (Belgium)
        "fr-rBF": u"Français (Burkina Faso)", # French (Burkina Faso)
        "fr-rBI": u"Français (Burundi)", # French (Burundi)
        "fr-rBJ": u"Français (Bénin)", # French (Benin)
        "fr-rBL": u"Français (Saint-Barthélémy)", # French (Saint Barthélemy)
        "fr-rCA": u"Français (Canada)", # French (Canada)
        "fr-rCD": u"Français (République démocratique du Congo)", # French (Congo [DRC])
        "fr-rCF": u"Français (République centrafricaine)", # French (Central African Republic)
        "fr-rCG": u"Français (Congo-Brazzaville)", # French (Congo [Republic])
        "fr-rCH": u"Français (Suisse)", # French (Switzerland)
        "fr-rCI": u"Français (Côte d’Ivoire)", # French (Côte d’Ivoire)
        "fr-rCM": u"Français (Cameroun)", # French (Cameroon)
        "fr-rDJ": u"Français (Djibouti)", # French (Djibouti)
        "fr-rDZ": u"Français (Algérie)", # French (Algeria)
        "fr-rFR": u"Français (France)", # French (France)
        "fr-rGA": u"Français (Gabon)", # French (Gabon)
        "fr-rGF": u"Français (Guyane française)", # French (French Guiana)
        "fr-rGN": u"Français (Guinée)", # French (Guinea)
        "fr-rGP": u"Français (Guadeloupe)", # French (Guadeloupe)
        "fr-rGQ": u"Français (Guinée équatoriale)", # French (Equatorial Guinea)
        "fr-rHT": u"Français (Haïti)", # French (Haiti)
        "fr-rKM": u"Français (Comores)", # French (Comoros)
        "fr-rLU": u"Français (Luxembourg)", # French (Luxembourg)
        "fr-rMA": u"Français (Maroc)", # French (Morocco)
        "fr-rMC": u"Français (Monaco)", # French (Monaco)
        "fr-rMF": u"Français (Saint-Martin [partie française])", # French (Saint Martin)
        "fr-rMG": u"Français (Madagascar)", # French (Madagascar)
        "fr-rML": u"Français (Mali)", # French (Mali)
        "fr-rMQ": u"Français (Martinique)", # French (Martinique)
        "fr-rMR": u"Français (Mauritanie)", # French (Mauritania)
        "fr-rMU": u"Français (Maurice)", # French (Mauritius)
        "fr-rNC": u"Français (Nouvelle-Calédonie)", # French (New Caledonia)
        "fr-rNE": u"Français (Niger)", # French (Niger)
        "fr-rPF": u"Français (Polynésie française)", # French (French Polynesia)
        "fr-rRE": u"Français (Réunion)", # French (Réunion)
        "fr-rRW": u"Français (Rwanda)", # French (Rwanda)
        "fr-rSC": u"Français (Seychelles)", # French (Seychelles)
        "fr-rSN": u"Français (Sénégal)", # French (Senegal)
        "fr-rSY": u"Français (Syrie)", # French (Syria)
        "fr-rTD": u"Français (Tchad)", # French (Chad)
        "fr-rTG": u"Français (Togo)", # French (Togo)
        "fr-rTN": u"Français (Tunisie)", # French (Tunisia)
        "fr-rVU": u"Français (Vanuatu)", # French (Vanuatu)
        "fr-rYT": u"Français (Mayotte)", # French (Mayotte)
        "ga": u"Gaeilge", # Irish
        "ga-rIE": u"Gaeilge (Éire)", # Irish (Ireland)
        "gl": u"Galego", # Galician
        "gl-rES": u"Galego (España)", # Galician (Spain)
        "gsw": u"Schwiizertüütsch", # Swiss German
        "gsw-rCH": u"Schwiizertüütsch (Schwiiz)", # Swiss German (Switzerland)
        "gu": u"ગુજરાતી", # Gujarati
        "gu-rIN": u"ગુજરાતી (ભારત)", # Gujarati (India)
        "guz": u"Ekegusii", # Gusii
        "guz-rKE": u"Ekegusii (Kenya)", # Gusii (Kenya)
        "gv": u"Gaelg", # Manx
        "gv-rGB": u"Gaelg (Rywvaneth Unys)", # Manx (United Kingdom)
        "ha": u"Hausa", # Hausa
        "ha-rLATN": u"Hausa (LATN)", # Hausa (LATN)
        "ha-rLATN_GH": u"Hausa (Gana,GH)", # Hausa (Ghana,GH)
        "ha-rLATN_NE": u"Hausa (Nijar,NE)", # Hausa (Niger,NE)
        "ha-rLATN_NG": u"Hausa (Najeriya,NG)", # Hausa (Nigeria,NG)
        "haw": u"ʻŌlelo Hawaiʻi", # Hawaiian
        "haw-rUS": u"ʻŌlelo Hawaiʻi (ʻAmelika Hui Pū ʻIa)", # Hawaiian (United States)
        "iw": u"עברית", # Hebrew
        "iw-rIL": u"עברית (ישראל)", # Hebrew (Israel)
        "hi": u"हिन्दी", # Hindi
        "hi-rIN": u"हिन्दी (भारत)", # Hindi (India)
        "hr": u"Hrvatski", # Croatian
        "hr-rBA": u"Hrvatski (Bosna i Hercegovina)", # Croatian (Bosnia and Herzegovina)
        "hr-rHR": u"Hrvatski (Hrvatska)", # Croatian (Croatia)
        "hu": u"Magyar", # Hungarian
        "hu-rHU": u"Magyar (Magyarország)", # Hungarian (Hungary)
        "hy": u"հայերեն", # Armenian
        "hy-rAM": u"հայերեն (Հայաստան)", # Armenian (Armenia)
        "in": u"Bahasa Indonesia", # Indonesian
        "in-rID": u"Bahasa Indonesia (Indonesia)", # Indonesian (Indonesia)
        "ig": u"Igbo", # Igbo
        "ig-rNG": u"Igbo (Nigeria)", # Igbo (Nigeria)
        "ii": u"ꆈꌠꉙ", # Sichuan Yi
        "ii-rCN": u"ꆈꌠꉙ (ꍏꇩ)", # Sichuan Yi (China)
        "is": u"íslenska", # Icelandic
        "is-rIS": u"íslenska (Ísland)", # Icelandic (Iceland)
        "it": u"Italiano", # Italian
        "it-rCH": u"Italiano (Svizzera)", # Italian (Switzerland)
        "it-rIT": u"Italiano (Italia)", # Italian (Italy)
        "it-rSM": u"Italiano (San Marino)", # Italian (San Marino)
        "ja": u"日本語", # Japanese
        "ja-rJP": u"日本語 (日本)", # Japanese (Japan)
        "jgo": u"Ndaꞌa", # Ngomba
        "jgo-rCM": u"Ndaꞌa (Kamɛlûn)", # Ngomba (Cameroon)
        "jmc": u"Kimachame", # Machame
        "jmc-rTZ": u"Kimachame (Tanzania)", # Machame (Tanzania)
        "ka": u"ქართული", # Georgian
        "ka-rGE": u"ქართული (საქართველო)", # Georgian (Georgia)
        "kab": u"Taqbaylit", # Kabyle
        "kab-rDZ": u"Taqbaylit (Lezzayer)", # Kabyle (Algeria)
        "kam": u"Kikamba", # Kamba
        "kam-rKE": u"Kikamba (Kenya)", # Kamba (Kenya)
        "kde": u"Chimakonde", # Makonde
        "kde-rTZ": u"Chimakonde (Tanzania)", # Makonde (Tanzania)
        "kea": u"Kabuverdianu", # Kabuverdianu
        "kea-rCV": u"Kabuverdianu (Kabu Verdi)", # Kabuverdianu (Cape Verde)
        "khq": u"Koyra ciini", # Koyra Chiini
        "khq-rML": u"Koyra ciini (Maali)", # Koyra Chiini (Mali)
        "ki": u"Gikuyu", # Kikuyu
        "ki-rKE": u"Gikuyu (Kenya)", # Kikuyu (Kenya)
        "kk": u"қазақ тілі", # Kazakh
        "kk-rCYRL": u"қазақ тілі (CYRL)", # Kazakh (CYRL)
        "kk-rCYRL_KZ": u"қазақ тілі (Қазақстан,KZ)", # Kazakh (Kazakhstan,KZ)
        "kl": u"Kalaallisut", # Kalaallisut
        "kl-rGL": u"Kalaallisut (Kalaallit Nunaat)", # Kalaallisut (Greenland)
        "kln": u"Kalenjin", # Kalenjin
        "kln-rKE": u"Kalenjin (Emetab Kenya)", # Kalenjin (Kenya)
        "km": u"ខ្មែរ", # Khmer
        "km-rKH": u"ខ្មែរ (កម្ពុជា)", # Khmer (Cambodia)
        "kn": u"ಕನ್ನಡ", # Kannada
        "kn-rIN": u"ಕನ್ನಡ (ಭಾರತ)", # Kannada (India)
        "ko": u"한국어", # Korean
        "ko-rKP": u"한국어 (조선 민주주의 인민 공화국)", # Korean (North Korea)
        "ko-rKR": u"한국어 (대한민국)", # Korean (South Korea)
        "kok": u"कोंकणी", # Konkani
        "kok-rIN": u"कोंकणी (भारत)", # Konkani (India)
        "ks": u"کٲشُر", # Kashmiri
        "ks-rARAB": u"کٲشُر (ARAB)", # Kashmiri (ARAB)
        "ks-rARAB_IN": u"کٲشُر (ہِنٛدوستان,IN)", # Kashmiri (India,IN)
        "ksb": u"Kishambaa", # Shambala
        "ksb-rTZ": u"Kishambaa (Tanzania)", # Shambala (Tanzania)
        "ksf": u"Rikpa", # Bafia
        "ksf-rCM": u"Rikpa (kamɛrún)", # Bafia (Cameroon)
        "kw": u"Kernewek", # Cornish
        "kw-rGB": u"Kernewek (Rywvaneth Unys)", # Cornish (United Kingdom)
        "lag": u"Kɨlaangi", # Langi
        "lag-rTZ": u"Kɨlaangi (Taansanía)", # Langi (Tanzania)
        "lg": u"Luganda", # Ganda
        "lg-rUG": u"Luganda (Yuganda)", # Ganda (Uganda)
        "ln": u"Lingála", # Lingala
        "ln-rAO": u"Lingála (Angóla)", # Lingala (Angola)
        "ln-rCD": u"Lingála (Repibiki demokratiki ya Kongó)", # Lingala (Congo [DRC])
        "ln-rCF": u"Lingála (Repibiki ya Afríka ya Káti)", # Lingala (Central African Republic)
        "ln-rCG": u"Lingála (Kongo)", # Lingala (Congo [Republic])
        "lo": u"ລາວ", # Lao
        "lo-rLA": u"ລາວ (ສ.ປ.ປ ລາວ)", # Lao (Laos)
        "lt": u"Lietuvių", # Lithuanian
        "lt-rLT": u"Lietuvių (Lietuva)", # Lithuanian (Lithuania)
        "lu": u"Tshiluba", # Luba-Katanga
        "lu-rCD": u"Tshiluba (Ditunga wa Kongu)", # Luba-Katanga (Congo [DRC])
        "luo": u"Dholuo", # Luo
        "luo-rKE": u"Dholuo (Kenya)", # Luo (Kenya)
        "luy": u"Luluhia", # Luyia
        "luy-rKE": u"Luluhia (Kenya)", # Luyia (Kenya)
        "lv": u"Latviešu", # Latvian
        "lv-rLV": u"Latviešu (Latvija)", # Latvian (Latvia)
        "mas": u"Maa", # Masai
        "mas-rKE": u"Maa (Kenya)", # Masai (Kenya)
        "mas-rTZ": u"Maa (Tansania)", # Masai (Tanzania)
        "mer": u"Kĩmĩrũ", # Meru
        "mer-rKE": u"Kĩmĩrũ (Kenya)", # Meru (Kenya)
        "mfe": u"Kreol morisien", # Morisyen
        "mfe-rMU": u"Kreol morisien (Moris)", # Morisyen (Mauritius)
        "mg": u"Malagasy", # Malagasy
        "mg-rMG": u"Malagasy (Madagasikara)", # Malagasy (Madagascar)
        "mgh": u"Makua", # Makhuwa-Meetto
        "mgh-rMZ": u"Makua (Umozambiki)", # Makhuwa-Meetto (Mozambique)
        "mgo": u"Metaʼ", # Meta'
        "mgo-rCM": u"Metaʼ (Kamalun)", # Meta' (Cameroon)
        "mk": u"македонски", # Macedonian
        "mk-rMK": u"македонски (Македонија)", # Macedonian (Macedonia [FYROM])
        "ml": u"മലയാളം", # Malayalam
        "ml-rIN": u"മലയാളം (ഇന്ത്യ)", # Malayalam (India)
        "mn": u"монгол", # Mongolian
        "mn-rCYRL": u"монгол (CYRL)", # Mongolian (CYRL)
        "mn-rCYRL_MN": u"монгол (Монгол,MN)", # Mongolian (Mongolia,MN)
        "mr": u"मराठी", # Marathi
        "mr-rIN": u"मराठी (भारत)", # Marathi (India)
        "ms": u"Bahasa Melayu", # Malay
        "ms-rLATN": u"Bahasa Melayu (LATN)", # Malay (LATN)
        "ms-rLATN_BN": u"Bahasa Melayu (Brunei,BN)", # Malay (Brunei,BN)
        "ms-rLATN_MY": u"Bahasa Melayu (Malaysia,MY)", # Malay (Malaysia,MY)
        "ms-rLATN_SG": u"Bahasa Melayu (Singapura,SG)", # Malay (Singapore,SG)
        "mt": u"Malti", # Maltese
        "mt-rMT": u"Malti (Malta)", # Maltese (Malta)
        "mua": u"MUNDAŊ", # Mundang
        "mua-rCM": u"MUNDAŊ (kameruŋ)", # Mundang (Cameroon)
        "my": u"ဗမာ", # Burmese
        "my-rMM": u"ဗမာ (မြန်မာ)", # Burmese (Myanmar [Burma])
        "naq": u"Khoekhoegowab", # Nama
        "naq-rNA": u"Khoekhoegowab (Namibiab)", # Nama (Namibia)
        "nb": u"Norsk bokmål", # Norwegian Bokmål
        "nb-rNO": u"Norsk bokmål (Norge)", # Norwegian Bokmål (Norway)
        "nd": u"IsiNdebele", # North Ndebele
        "nd-rZW": u"IsiNdebele (Zimbabwe)", # North Ndebele (Zimbabwe)
        "ne": u"नेपाली", # Nepali
        "ne-rIN": u"नेपाली (भारत)", # Nepali (India)
        "ne-rNP": u"नेपाली (नेपाल)", # Nepali (Nepal)
        "nl": u"Nederlands", # Dutch
        "nl-rAW": u"Nederlands (Aruba)", # Dutch (Aruba)
        "nl-rBE": u"Nederlands (België)", # Dutch (Belgium)
        "nl-rCW": u"Nederlands (Curaçao)", # Dutch (Curaçao)
        "nl-rNL": u"Nederlands (Nederland)", # Dutch (Netherlands)
        "nl-rSR": u"Nederlands (Suriname)", # Dutch (Suriname)
        "nl-rSX": u"Nederlands (Sint-Maarten)", # Dutch (Sint Maarten)
        "nmg": u"Nmg", # Kwasio
        "nmg-rCM": u"Nmg (Kamerun)", # Kwasio (Cameroon)
        "nn": u"Nynorsk", # Norwegian Nynorsk
        "nn-rNO": u"Nynorsk (Noreg)", # Norwegian Nynorsk (Norway)
        "nus": u"Thok Nath", # Nuer
        "nus-rSD": u"Thok Nath (Sudan)", # Nuer (Sudan)
        "nyn": u"Runyankore", # Nyankole
        "nyn-rUG": u"Runyankore (Uganda)", # Nyankole (Uganda)
        "om": u"Oromoo", # Oromo
        "om-rET": u"Oromoo (Itoophiyaa)", # Oromo (Ethiopia)
        "om-rKE": u"Oromoo (Keeniyaa)", # Oromo (Kenya)
        "or": u"ଓଡ଼ିଆ", # Oriya
        "or-rIN": u"ଓଡ଼ିଆ (ଭାରତ)", # Oriya (India)
        "pa": u"ਪੰਜਾਬੀ", # Punjabi
        "pa-rARAB": u"پنجاب (ARAB)", # Punjabi (ARAB)
        "pa-rARAB_PK": u"پنجاب (پکستان,PK)", # Punjabi (Pakistan,PK)
        "pa-rGURU": u"ਪੰਜਾਬੀ (GURU)", # Punjabi (GURU)
        "pa-rGURU_IN": u"ਪੰਜਾਬੀ (ਭਾਰਤ,IN)", # Punjabi (India,IN)
        "pl": u"Polski", # Polish
        "pl-rPL": u"Polski (Polska)", # Polish (Poland)
        "ps": u"پښتو", # Pashto
        "ps-rAF": u"پښتو (افغانستان)", # Pashto (Afghanistan)
        "pt": u"Português", # Portuguese
        "pt-rAO": u"Português (Angola)", # Portuguese (Angola)
        "pt-rBR": u"Português (Brasil)", # Portuguese (Brazil)
        "pt-rCV": u"Português (Cabo Verde)", # Portuguese (Cape Verde)
        "pt-rGW": u"Português (Guiné Bissau)", # Portuguese (Guinea-Bissau)
        "pt-rMO": u"Português (Macau)", # Portuguese (Macau)
        "pt-rMZ": u"Português (Moçambique)", # Portuguese (Mozambique)
        "pt-rPT": u"Português (Portugal)", # Portuguese (Portugal)
        "pt-rST": u"Português (São Tomé e Príncipe)", # Portuguese (São Tomé and Príncipe)
        "pt-rTL": u"Português (Timor-Leste)", # Portuguese (Timor-Leste)
        "rm": u"Rumantsch", # Romansh
        "rm-rCH": u"Rumantsch (Svizra)", # Romansh (Switzerland)
        "rn": u"Ikirundi", # Rundi
        "rn-rBI": u"Ikirundi (Uburundi)", # Rundi (Burundi)
        "ro": u"Română", # Romanian
        "ro-rMD": u"Română (Republica Moldova)", # Romanian (Moldova)
        "ro-rRO": u"Română (România)", # Romanian (Romania)
        "rof": u"Kihorombo", # Rombo
        "rof-rTZ": u"Kihorombo (Tanzania)", # Rombo (Tanzania)
        "ru": u"русский", # Russian
        "ru-rBY": u"русский (Беларусь)", # Russian (Belarus)
        "ru-rKG": u"русский (Киргизия)", # Russian (Kyrgyzstan)
        "ru-rKZ": u"русский (Казахстан)", # Russian (Kazakhstan)
        "ru-rMD": u"русский (Молдова)", # Russian (Moldova)
        "ru-rRU": u"русский (Россия)", # Russian (Russia)
        "ru-rUA": u"русский (Украина)", # Russian (Ukraine)
        "rw": u"Kinyarwanda", # Kinyarwanda
        "rw-rRW": u"Kinyarwanda (Rwanda)", # Kinyarwanda (Rwanda)
        "rwk": u"Kiruwa", # Rwa
        "rwk-rTZ": u"Kiruwa (Tanzania)", # Rwa (Tanzania)
        "saq": u"Kisampur", # Samburu
        "saq-rKE": u"Kisampur (Kenya)", # Samburu (Kenya)
        "sbp": u"Ishisangu", # Sangu
        "sbp-rTZ": u"Ishisangu (Tansaniya)", # Sangu (Tanzania)
        "seh": u"Sena", # Sena
        "seh-rMZ": u"Sena (Moçambique)", # Sena (Mozambique)
        "ses": u"Koyraboro senni", # Koyraboro Senni
        "ses-rML": u"Koyraboro senni (Maali)", # Koyraboro Senni (Mali)
        "sg": u"Sängö", # Sango
        "sg-rCF": u"Sängö (Ködörösêse tî Bêafrîka)", # Sango (Central African Republic)
        "shi": u"ⵜⴰⵎⴰⵣⵉⵖⵜ", # Tachelhit
        "shi-rLATN": u"Tamazight (LATN)", # Tachelhit (LATN)
        "shi-rLATN_MA": u"Tamazight (lmɣrib,MA)", # Tachelhit (Morocco,MA)
        "shi-rTFNG": u"ⵜⴰⵎⴰⵣⵉⵖⵜ (TFNG)", # Tachelhit (TFNG)
        "shi-rTFNG_MA": u"ⵜⴰⵎⴰⵣⵉⵖⵜ (ⵍⵎⵖⵔⵉⴱ,MA)", # Tachelhit (Morocco,MA)
        "si": u"සිංහල", # Sinhala
        "si-rLK": u"සිංහල (ශ්‍රී ලංකාව)", # Sinhala (Sri Lanka)
        "sk": u"Slovenčina", # Slovak
        "sk-rSK": u"Slovenčina (Slovensko)", # Slovak (Slovakia)
        "sl": u"Slovenščina", # Slovenian
        "sl-rSI": u"Slovenščina (Slovenija)", # Slovenian (Slovenia)
        "sn": u"ChiShona", # Shona
        "sn-rZW": u"ChiShona (Zimbabwe)", # Shona (Zimbabwe)
        "so": u"Soomaali", # Somali
        "so-rDJ": u"Soomaali (Jabuuti)", # Somali (Djibouti)
        "so-rET": u"Soomaali (Itoobiya)", # Somali (Ethiopia)
        "so-rKE": u"Soomaali (Kiiniya)", # Somali (Kenya)
        "so-rSO": u"Soomaali (Soomaaliya)", # Somali (Somalia)
        "sq": u"Shqip", # Albanian
        "sq-rAL": u"Shqip (Shqipëria)", # Albanian (Albania)
        "sq-rMK": u"Shqip (Maqedoni)", # Albanian (Macedonia [FYROM])
        "sr": u"Српски", # Serbian
        "sr-rCYRL": u"Српски (CYRL)", # Serbian (CYRL)
        "sr-rCYRL_BA": u"Српски (Босна и Херцеговина,BA)", # Serbian (Bosnia and Herzegovina,BA)
        "sr-rCYRL_ME": u"Српски (Црна Гора,ME)", # Serbian (Montenegro,ME)
        "sr-rCYRL_RS": u"Српски (Србија,RS)", # Serbian (Serbia,RS)
        "sr-rLATN": u"Srpski (LATN)", # Serbian (LATN)
        "sr-rLATN_BA": u"Srpski (Bosna i Hercegovina,BA)", # Serbian (Bosnia and Herzegovina,BA)
        "sr-rLATN_ME": u"Srpski (Crna Gora,ME)", # Serbian (Montenegro,ME)
        "sr-rLATN_RS": u"Srpski (Srbija,RS)", # Serbian (Serbia,RS)
        "sv": u"Svenska", # Swedish
        "sv-rAX": u"Svenska (Åland)", # Swedish (Åland Islands)
        "sv-rFI": u"Svenska (Finland)", # Swedish (Finland)
        "sv-rSE": u"Svenska (Sverige)", # Swedish (Sweden)
        "sw": u"Kiswahili", # Swahili
        "sw-rKE": u"Kiswahili (Kenya)", # Swahili (Kenya)
        "sw-rTZ": u"Kiswahili (Tanzania)", # Swahili (Tanzania)
        "sw-rUG": u"Kiswahili (Uganda)", # Swahili (Uganda)
        "swc": u"Kiswahili ya Kongo", # Congo Swahili
        "swc-rCD": u"Kiswahili ya Kongo (Jamhuri ya Kidemokrasia ya Kongo)", # Congo Swahili (Congo [DRC])
        "ta": u"தமிழ்", # Tamil
        "ta-rIN": u"தமிழ் (இந்தியா)", # Tamil (India)
        "ta-rLK": u"தமிழ் (இலங்கை)", # Tamil (Sri Lanka)
        "ta-rMY": u"தமிழ் (மலேஷியா)", # Tamil (Malaysia)
        "ta-rSG": u"தமிழ் (சிங்கப்பூர்)", # Tamil (Singapore)
        "te": u"తెలుగు", # Telugu
        "te-rIN": u"తెలుగు (భారత దేశం)", # Telugu (India)
        "teo": u"Kiteso", # Teso
        "teo-rKE": u"Kiteso (Kenia)", # Teso (Kenya)
        "teo-rUG": u"Kiteso (Uganda)", # Teso (Uganda)
        "th": u"ไทย", # Thai
        "th-rTH": u"ไทย (ไทย)", # Thai (Thailand)
        "ti": u"ትግርኛ", # Tigrinya
        "ti-rER": u"ትግርኛ (ER)", # Tigrinya (Eritrea)
        "ti-rET": u"ትግርኛ (ET)", # Tigrinya (Ethiopia)
        "to": u"Lea fakatonga", # Tongan
        "to-rTO": u"Lea fakatonga (Tonga)", # Tongan (Tonga)
        "tr": u"Türkçe", # Turkish
        "tr-rCY": u"Türkçe (Güney Kıbrıs Rum Kesimi)", # Turkish (Cyprus)
        "tr-rTR": u"Türkçe (Türkiye)", # Turkish (Turkey)
        "twq": u"Tasawaq senni", # Tasawaq
        "twq-rNE": u"Tasawaq senni (Nižer)", # Tasawaq (Niger)
        "tzm": u"Tamaziɣt", # Central Atlas Tamazight
        "tzm-rLATN": u"Tamaziɣt (LATN)", # Central Atlas Tamazight (LATN)
        "tzm-rLATN_MA": u"Tamaziɣt (Meṛṛuk,MA)", # Central Atlas Tamazight (Morocco,MA)
        "uk": u"українська", # Ukrainian
        "uk-rUA": u"українська (Україна)", # Ukrainian (Ukraine)
        "ur": u"اردو", # Urdu
        "ur-rIN": u"اردو (بھارت)", # Urdu (India)
        "ur-rPK": u"اردو (پاکستان)", # Urdu (Pakistan)
        "uz": u"Ўзбек", # Uzbek
        "uz-rARAB": u"اوزبیک (ARAB)", # Uzbek (ARAB)
        "uz-rARAB_AF": u"اوزبیک (افغانستان,AF)", # Uzbek (Afghanistan,AF)
        "uz-rCYRL": u"Ўзбек (CYRL)", # Uzbek (CYRL)
        "uz-rCYRL_UZ": u"Ўзбек (Ўзбекистон,UZ)", # Uzbek (Uzbekistan,UZ)
        "uz-rLATN": u"Oʻzbekcha (LATN)", # Uzbek (LATN)
        "uz-rLATN_UZ": u"Oʻzbekcha (Oʻzbekiston,UZ)", # Uzbek (Uzbekistan,UZ)
        "vai": u"ꕙꔤ", # Vai
        "vai-rLATN": u"Vai (LATN)", # Vai (LATN)
        "vai-rLATN_LR": u"Vai (Laibhiya,LR)", # Vai (Liberia,LR)
        "vai-rVAII": u"ꕙꔤ (VAII)", # Vai (VAII)
        "vai-rVAII_LR": u"ꕙꔤ (ꕞꔤꔫꕩ,LR)", # Vai (Liberia,LR)
        "vi": u"Tiếng Việt", # Vietnamese
        "vi-rVN": u"Tiếng Việt (Việt Nam)", # Vietnamese (Vietnam)
        "vun": u"Kyivunjo", # Vunjo
        "vun-rTZ": u"Kyivunjo (Tanzania)", # Vunjo (Tanzania)
        "xog": u"Olusoga", # Soga
        "xog-rUG": u"Olusoga (Yuganda)", # Soga (Uganda)
        "yav": u"Nuasue", # Yangben
        "yav-rCM": u"Nuasue (Kemelún)", # Yangben (Cameroon)
        "yo": u"Èdè Yorùbá", # Yoruba
        "yo-rNG": u"Èdè Yorùbá (Orílẹ́ède Nàìjíríà)", # Yoruba (Nigeria)
        # This was the obtained from Locale, but it seems it's different in Settings
        #"zh": u"中文", # Chinese
        "zh": u"中文 (简体)", # Chinese
        "zh-rHANS": u"中文 (HANS)", # Chinese (HANS)
        "zh-rHANS_CN": u"中文 (中国,CN)", # Chinese (China,CN)
        "zh-rHANS_HK": u"中文 (香港,HK)", # Chinese (Hong Kong,HK)
        "zh-rHANS_MO": u"中文 (澳门,MO)", # Chinese (Macau,MO)
        "zh-rHANS_SG": u"中文 (新加坡,SG)", # Chinese (Singapore,SG)
        "zh-rHANT": u"中文 (HANT)", # Chinese (HANT)
        "zh-rHANT_HK": u"中文 (香港,HK)", # Chinese (Hong Kong,HK)
        "zh-rHANT_MO": u"中文 (澳門,MO)", # Chinese (Macau,MO)
        "zh-rHANT_TW": u"中文 (台灣,TW)", # Chinese (Taiwan,TW)
        "zu": u"IsiZulu", # Zulu
        "zu-rZA": u"IsiZulu (iNingizimu Afrika)", # Zulu (South Africa)
    }

    package = 'com.android.settings'
    activity = '.Settings'
    component_name = package + '/' + activity
    if not languageTo in LANGUAGES.keys():
        raise RuntimeError("%s is not a supported language by AndroidViewClient" % languageTo)
    self.device.startActivity(component=component_name)
    self.vc.dump(-1)
    view = None
    currentLanguage = None
    ATTEMPTS = 10
    for _ in range(ATTEMPTS):
        android___id_list = self.vc.findViewByIdOrRaise("android:id/list")
        for k, v in LANGUAGE_SETTINGS.iteritems():
            view = self.vc.findViewWithText(v, root=android___id_list)
            #self.vc.dump()
            #view = self.vc.findViewWithText(v)
            if view:
                currentLanguage = k
                break
        if view:
            break
        android___id_list.uiScrollable.flingForward()
        self.vc.sleep(1)
        self.vc.dump(-1)
	if view is None:
		raise ViewNotFoundException("text", "'Language & input' (any language)", "ROOT")
    view.touch()
    self.vc.sleep(1)
    self.vc.dump(-1)
    self.vc.findViewWithTextOrRaise(PHONE_LANGUAGE[currentLanguage]).touch()
    self.vc.sleep(1)
    self.vc.dump(-1)

    android___id_list = self.vc.findViewByIdOrRaise("android:id/list")
    android___id_list.uiScrollable.setViewClient(self.vc)
    view = android___id_list.uiScrollable.scrollTextIntoView(u"English (United States)")
    if view is not None:
        view.touch()
    else:
        #raise RuntimeError(u"Couldn't change language to %s (%s)" % (LANGUAGES[languageTo], languageTo))
        raise RuntimeError("Couldn't change language to %s" % languageTo)

if __name__ == '__main__':
        # Connect to device with the IP received as a parameter
        device, serialno = ViewClient.connectToDeviceOrExit()
        # Connect to device with the IP received as a parameter
        device, serialno = ViewClient.connectToDeviceOrExit()
        vc = ViewClient(device=device, serialno=serialno)
        ud = UiDevice(vc=vc)
        
        device.press('KEYCODE_HOME','DOWN_AND_UP')
        #Change language to English (United States)
        ud.changeLanguage('en-rUS')
        
        # Press the HOME button to start the test from the home screen
        device.press('KEYCODE_HOME','DOWN_AND_UP')
