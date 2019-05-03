import request

if __name__ == '__main__':
    url = 'http://localhost:8000/libro/'

    response = request.get(url)
    if response.status_code == 200:

        payload = response.json()
        results = payload.get('results', [])

        if results:
            for libro in results:
                libroList = libro['libroList']
                print(libroList)

