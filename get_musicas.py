import requests

def get_musicas(headers, album_id):

    url = f'https://api-partner.spotify.com/pathfinder/v1/query?operationName=queryAlbumTracks&variables=%7B%22uri%22%3A%22spotify%3Aalbum%3A{album_id}%22%2C%22offset%22%3A0%2C%22limit%22%3A300%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%223ea563e1d68f486d8df30f69de9dcedae74c77e684b889ba7408c589d30f7f2e%22%7D%7D' 

    response = requests.get(url, headers=headers)
    data = response.json()
    items = data['data']['album']['tracks']['items']
    tracks = [item['track'] for item in items]
    musicas = [{'name': track['name'], 'count': track['playcount']} for track in tracks]
    return musicas

