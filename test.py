import re
def get_network_name_from_phone(phonenumber):
    phone_regexes_dict = {
            '^\+225(05|07|04|55|56|54|47|44|46|84|85|86|95|96)\d{6}': 'MTN CI',
            '^\+225(08|09|48|49|57|58|59|77|78|87|88|89|98)\d{6}':'ORANGECI',
            '^\+237(650|651|652|653|654|670|671|672|673|674|675|676|677|678|679|680)\d{6}': 'MTN CAMEROON',
            '^\+237((69)\d{7}|(655|656|657|658|659)\d{6})': 'ORANGECM',
            '^\+224(662|661|666)\d{6}': 'MTNGN',
            '^\+224(622)\d{6}': 'ORANGEGN',
            '^\+245\d{9}': 'GUINEA BISSAU',
            '^\+226\d{8}': 'BURKINA FASO',
            '^\+221(77|78)\d{7}': 'ORANGESN',
            '^\+221(76)\d{7}': 'TIGOSN',
            '^\+221(70)\d{7}': 'EXPRESSOSN',
            '\+233(26|27|56|57)\d{7}$': 'AIRTEL TIGO',
        }
    phone_regexes_list = list(phone_regexes_dict.keys())
    for key in range(len(phone_regexes_dict)):
        phone_regexes_key = phone_regexes_list[key]
        result = re.match(phone_regexes_key, phonenumber)
        if result:
            return phone_regexes_dict[phone_regexes_key]
a=get_network_name_from_phone('+22598522611')
print(a)