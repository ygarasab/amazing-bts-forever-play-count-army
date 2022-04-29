import requests

def get_discos(headers):

    url  = 'https://api-partner.spotify.com/pathfinder/v1/query?operationName=queryArtistDiscographyAlbums&variables=%7B%22uri%22%3A%22spotify%3Aartist%3A3Nrfpe0tUJi4K4DXYWgMUX%22%2C%22offset%22%3A0%2C%22limit%22%3A20%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22e38c23e4e8aa873903ab47c2c84ab9f1175e645cf03a34eafdeea07454e5c3da%22%7D%7D'

    
    response = requests.get(url, headers=headers)
    data = response.json()
    items = data['data']['artist']['discography']['albums']['items']
    ids = [ item['releases']['items'][0]['id'] for item in items] 
    return ids
