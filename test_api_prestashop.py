import requests

ENDPOINT = 'http://164.92.218.36:8080/api'

with open('keys.txt', 'r') as file:
    lines = file.readlines()
    key = lines[0].strip()

with open('keys.txt', 'r') as file:
    lines = file.readlines()
    password = lines[1].strip()

new_address = '''<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <address>
        <id_customer></id_customer>
        <id_manufacturer></id_manufacturer>
        <id_supplier></id_supplier>
        <id_warehouse></id_warehouse>
        <id_country xlink:href="http://164.92.218.36:8080/api/countries/1">1</id_country>
        <id_state></id_state>
        <alias>0</alias>
        <company></company>
        <lastname>Group number two new</lastname>
        <firstname>Maks Mariia Ola</firstname>
        <vat_number></vat_number>
        <address1>123</address1>
        <address2>321</address2>
        <postcode>60000</postcode>
        <city>Morshin</city>
        <other></other>
        <phone></phone>
        <phone_mobile></phone_mobile>
        <dni></dni>
        <deleted></deleted>
        <date_add></date_add>
        <date_upd></date_upd>
    </address>
</prestashop>'''


def test_can_call_endpoint():
    response = requests.get(ENDPOINT, auth=(key, password))
    assert response.status_code == 200


def test_can_get_addresses():
    response = requests.get(ENDPOINT + '/addresses', auth=(key, password))
    assert response.status_code == 200


def test_can_create_new_address():
    response = requests.post(ENDPOINT + '/addresses',
                             auth=(key, password), data=new_address)
    assert response.status_code == 201
    get_id(response)
    print(f'The id that was created is ' + get_id(response))


def test_can_update_the_address():
    response = requests.post(ENDPOINT + '/addresses',
                             auth=(key, password), data=new_address)
    get_id(response)
    change_address = f'''<?xml version="1.0" encoding="UTF-8"?>
        <prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
            <address>
                <id>{get_id(response)}</id>
                <id_customer></id_customer>
                <id_manufacturer></id_manufacturer>
                <id_supplier></id_supplier>
                <id_warehouse></id_warehouse>
                <id_country xlink:href="http://164.92.218.36:8080/api/countries/1">1</id_country>
                <id_state>1</id_state>
                <alias>0</alias>
                <company></company>
                <lastname>Group two Updated</lastname>
                <firstname>Mariia Ola</firstname>
                <vat_number></vat_number>
                <address1>New address</address1>
                <address2>New address2</address2>
                <postcode>70000</postcode>
                <city>Morshin</city>
                <other></other>
                <phone></phone>
                <phone_mobile></phone_mobile>
                <dni></dni>
                <deleted></deleted>
                <date_add></date_add>
                <date_upd></date_upd>
            </address>
        </prestashop>'''
    update_new_address = requests.put(
        ENDPOINT + f'/addresses/{get_id(response)}', auth=(key, password), data=change_address)
    assert update_new_address.status_code == 200
    new_lastname = str(update_new_address.text)
    new_lastname = new_lastname.split('lastname')
    new_lastname[1] = new_lastname[1].strip('>/<!]CDAT[')
    assert new_lastname[1] == 'Group two Updated'
    print(f'The id that was created and updated is ' + get_id(response))


def test_can_delete_the_address():
    response = requests.post(ENDPOINT + '/addresses',
                             auth=(key, password), data=new_address)
    get_id(response)
    new_address_delete = requests.delete(
        ENDPOINT + f'/addresses/{get_id(response)}', auth=(key, password))
    assert new_address_delete.status_code == 200
    print(f'The id that was deleted is ' + get_id(response))
    new_address_delete_sc = requests.get(
        ENDPOINT + f'/addresses/{get_id(response)}', auth=(key, password))
    assert new_address_delete_sc.status_code == 404
    print('The status code of deleted page is ' +
          str(new_address_delete_sc.status_code))


def get_id(to_get_id):
    new_id = str(to_get_id.text)
    new_id = new_id.split('id')
    new_id[1] = new_id[1].strip('>/<!]CDAT[')
    return new_id[1]


new_category = """<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <category>
        <active>0</active>
        <position>
        <![CDATA[ 0 ]]>
        </position>
        <name>
        <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">
        <![CDATA[ korenevij-katalog ]]>
        </language>
        </name>
        <link_rewrite>
        <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">
        <![CDATA[ korenevij-katalog ]]>
        </language>
        </link_rewrite>
        <description>
        <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">
        <![CDATA[ ]]>
        </language>
        </description>
        <meta_title>
        <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">
        <![CDATA[ ]]>
        </language>
        </meta_title>
        <meta_description>
        <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">
        <![CDATA[ ]]>
        </language>
        </meta_description>
        <meta_keywords>
        <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">
        <![CDATA[ ]]>
        </language>
        </meta_keywords>
        <associations>
        <categories nodeType="category" api="categories">
        <category xlink:href="http://164.92.218.36:8080/api/categories/2">
        <id>
        <![CDATA[ 2 ]]>
        </id>
        </category>
        </categories>
        <products nodeType="product" api="products"/>
        </associations>
    </category>
</prestashop>"""


def test_can_get_categories():
    response = requests.get(ENDPOINT + '/categories', auth=(key, ""))
    assert response.status_code == 200


def test_can_create_new_categories():
    response = requests.post(ENDPOINT + '/categories',
                             auth=(key, ""), data=new_category)
    assert response.status_code == 201
    get_id(response)
    print(f'The id that was created is ' + get_id(response))


def test_cannot_update_the_category():
    response = requests.post(ENDPOINT + '/categories',
                             auth=(key, ''), data=new_category)
    get_id(response)
    change_category_info = f'''<?xml version="1.0" encoding="UTF-8"?>
    <prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <category>
        <id>{get_id(response)}<id>
        <id_parent></id_parent>
        <active>1</active>
        <id_shop_default>1</id_shop_default>
        <is_root_category>0</is_root_category>
        <position>22</position>
        <date_add></date_add>
        <date_upd></date_upd>
        <name>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"> Group two update 
            </language>
        </name>
        <link_rewrite>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">
               t-shitless
            </language>
        </link_rewrite>
        <description>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">
            </language>
        </description>
        <meta_title>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">  
            </language>
        </meta_title>
        <meta_description>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">
            </language>
        </meta_description>
        <meta_keywords>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">
            </language>
        </meta_keywords>
        <associations>
            <categories nodeType="category" api="categories"/>
            <products nodeType="product" api="products"/>
        </associations>
    </category>
    </prestashop>'''
    update_new_category = requests.put(ENDPOINT + f'/categories/{get_id(response)}',
                                       auth=(key, ''), data=change_category_info)
    assert update_new_category.status_code == 405
    print(f'The id that was not updated is ' + get_id(response))


def test_cannot_delete_the_category():
    response = requests.post(ENDPOINT + '/categories',
                             auth=(key, ''), data=new_category)
    get_id(response)
    delete_new_category = requests.delete(ENDPOINT + f'/categories/{get_id(response)}',
                                          auth=(key, ''))
    assert delete_new_category.status_code == 405
    print(f'The id that was not deleted is ' + get_id(response))


def get_id(to_get_id):
    new_id = str(to_get_id.text)
    new_id = new_id.split('id')
    new_id[1] = new_id[1].strip('>/<!]CDAT[')
    return new_id[1]
