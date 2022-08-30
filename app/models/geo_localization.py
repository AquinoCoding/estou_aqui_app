import geocoder
from geopy.geocoders import Nominatim
from pycep_correios import get_address_from_cep, WebService

def get_location(localization):
    
    local = geocoder.ip('me')
    loc = Nominatim(user_agent="GetLoc")
    
    local = local.address
    
    try:
        getLoc = loc.geocode(local)
        loc_name = loc.reverse(f"{getLoc.latitude}, {getLoc.longitude}")

        address_local = loc_name.address.split(',')

        address_tratament = address_local[-2][1:].replace('-', '')
        address = get_address_from_cep(address_tratament, webservice=WebService.APICEP)
        
        localization = str(address['cidade']) + ' ' + str(address['logradouro']) + ', ' + str(address['uf'])
        
    except:
        validation = localization == ''
        if validation:
            localization = 'Brasilia'
            
    
    return localization
