import pymysql


def connectMysql():
    connMysql = pymysql.connect(
        host='34.89.114.242',
        port=3306,
        user='root',
        password='!ttds2021',
        db='TTDS_group7',
        charset='utf8mb4'
    )
    return connMysql

def get_data():
    conn = connectMysql()
    cursor = conn.cursor()
    sentence = 'select id,content from news where country is null '
    cursor.execute(sentence)
    text = dict(cursor.fetchall())
    id = list(text.keys())
    conn.close()

def execute(sentence, commitlist):
    conn = connectMysql()
    cursor = conn.cursor()
    cursor.executemany(sentence, commitlist)
    conn.commit()
    conn.close()

convert_dict = {
    "People's Republic of China": 'China',
    'The Gambia': 'Gambia',
    'Guinea-Bissau': 'Guinea Bissau',
    'North Macedonia': 'Macedonia',
    'Serbia': 'Republic of Serbia',
    'Eswatini': 'Swaziland',
    'Tanzania': 'United Republic of Tanzania'
}
sqlnation = set('''
Afghanistan
Africa
Albania
Algeria
Angola
Antarctica
Argentina
Armenia
Asia
Australia
Austria
Azerbaijan
Bangladesh
Belarus
Belgium
Belize
Benin
Bermuda
Bhutan
Bolivia
Bosnia and Herzegovina
Botswana
Brazil
Brunei
Bulgaria
Burkina Faso
Burundi
Cambodia
Cameroon
Canada
Central African Republic
Chad
Chile
China
Colombia
Costa Rica
Croatia
Cuba
Cyprus
Czech Republic
Democratic Republic of the Congo
Denmark
Djibouti
Dominican Republic
East Timor
Ecuador
Egypt
El Salvador
Equatorial Guinea
Eritrea
Estonia
Ethiopia
Europe
Falkland Islands
Fiji
Finland
France
French Guiana
French Southern and Antarctic Lands
Gabon
Gambia
Georgia
Germany
Ghana
Greece
Greenland
Guatemala
Guinea
Guinea Bissau
Guyana
Haiti
Honduras
Hungary
Iceland
India
Indonesia
Iran
Iraq
Ireland
Israel
Italy
Ivory Coast
Jamaica
Japan
Jordan
Kazakhstan
Kenya
Kosovo
Kuwait
Kyrgyzstan
Laos
Latin America
Latvia
Lebanon
Lesotho
Liberia
Libya
Lithuania
Luxembourg
Macedonia
Madagascar
Malawi
Malaysia
Mali
Malta
Mauritania
Mexico
Middle East
Moldova
Mongolia
Montenegro
Morocco
Mozambique
Myanmar
Namibia
Nepal
Netherlands
New Caledonia
New Zealand
Nicaragua
Niger
Nigeria
None
North Korea
Northern Cyprus
Norway
Oman
Pakistan
Panama
Papua New Guinea
Paraguay
Peru
Philippines
Poland
Portugal
Puerto Rico
Qatar
Republic of Serbia
Republic of the Congo
Romania
Russia
Rwanda
Saudi Arabia
Senegal
Sierra Leone
Slovakia
Slovenia
Solomon Islands
Somalia
Somaliland
South Africa
South Korea
South Sudan
Spain
Sri Lanka
Sudan
Suriname
Swaziland
Sweden
Switzerland
Syria
Taiwan
Tajikistan
Thailand
The Bahamas
Togo
Trinidad and Tobago
Tunisia
Turkey
Turkmenistan
Uganda
Ukraine
United Arab Emirates
United Kingdom
United Republic of Tanzania
United States of America
Uruguay
US&Canada
Uzbekistan
Vanuatu
Venezuela
Vietnam
West Bank
Western Sahara
Yemen
Zambia
Zimbabwe
'''.strip().split('\n'))
allnation =set('''
Andorra
United Arab Emirates
Afghanistan
Antigua and Barbuda
Albania
Armenia
Angola
Argentina
American Samoa
Austria
Australia
Aruba
Azerbaijan
Bosnia and Herzegovina
Barbados
Bangladesh
Belgium
Burkina Faso
Bulgaria
Bahrain
Burundi
Benin
Brunei
Bolivia
Brazil
The Bahamas
Bhutan
Botswana
Belarus
Belize
Canada
Democratic Republic of the Congo
Central African Republic
Republic of the Congo
Switzerland
Ivory Coast
Cook Islands
Chile
Cameroon
People's Republic of China
Colombia
Costa Rica
Cuba
Cape Verde
Cyprus
Czech Republic
Germany
Djibouti
Denmark
Dominica
Dominican Republic
Algeria
Ecuador
Estonia
Egypt
Eritrea
Spain
Ethiopia
Finland
Fiji
Federated States of Micronesia
Faroe Islands
France
Gabon
United Kingdom
Grenada
Georgia
Ghana
Greenland
The Gambia
Guinea
Equatorial Guinea
Greece
Guatemala
Guinea-Bissau
Guyana
Honduras
Croatia
Haiti
Hungary
Indonesia
Ireland
Israel
India
Iraq
Iran
Iceland
Italy
Jamaica
Jordan
Japan
Kenya
Kyrgyzstan
Cambodia
Kiribati
Comoros
Saint Kitts and Nevis
North Korea
South Korea
Kuwait
Kazakhstan
Laos
Lebanon
Saint Lucia
Liechtenstein
Sri Lanka
Liberia
Lesotho
Lithuania
Luxembourg
Latvia
Libya
Morocco
Monaco
Moldova
Montenegro
Madagascar
Marshall Islands
North Macedonia
Mali
Myanmar
Mongolia
Northern Mariana Islands
Mauritania
Malta
Mauritius
Maldives
Malawi
Mexico
Malaysia
Mozambique
Namibia
Niger
Nigeria
Nicaragua
Kingdom of the Netherlands
Netherlands
Norway
Nepal
Nauru
Niue
New Zealand
Oman
Panama
Peru
Papua New Guinea
Philippines
Pakistan
Poland
Portugal
Palau
Paraguay
Qatar
Romania
Serbia
Russia
Rwanda
Saudi Arabia
Solomon Islands
Seychelles
Sudan
Sweden
Singapore
Slovenia
Slovakia
Sierra Leone
San Marino
Senegal
Somalia
Suriname
South Sudan
São Tomé and Príncipe
El Salvador
Sint Maarten
Syria
Eswatini
Chad
Togo
Thailand
Tajikistan
East Timor
Turkmenistan
Tunisia
Tonga
Turkey
Trinidad and Tobago
Tuvalu
Taiwan
Tanzania
Ukraine
Uganda
United States of America
Uruguay
Uzbekistan
Vatican City
Saint Vincent and the Grenadines
Venezuela
Vietnam
Vanuatu
Samoa
Yemen
South Africa
Zambia
Zimbabwe
'''.strip().split('\n'))
uni = set()

for i in sqlnation:
    if i in allnation:
        uni.add(i)

sqlnation1 = list(sqlnation-uni)
allnation1 = list(allnation-uni-set(convert_dict.keys()))
sqlnation1.sort()
allnation1.sort()
print(sqlnation1)
for i in allnation1:
    print(i)
print(allnation1)

get_data()

# sentence = 'insert into countryList(countryname) values((%s))'
# execute(sentence,allnation1)


