import http.client
import requests
import json



Json_Request = requests.get("https://api.themoviedb.org/3/tv/top_rated?api_key=db668c594bf0c7de0ef6c1af5c5c2ddd&language=en-US&page=1").json()


class TopRatedShows:



    def compile_image(Imageurl):

        Api_Key = 'db668c594bf0c7de0ef6c1af5c5c2ddd'
        response = requests.get("https://api.themoviedb.org/3/configuration?api_key=db668c594bf0c7de0ef6c1af5c5c2ddd").json()
        baseUrl = response['images']['base_url']
        Size = 'w185'

        makeImage = baseUrl + Size + Imageurl

        return makeImage


    Name = Json_Request['results'][0]['name']
    Overview = Json_Request['results'][0]['overview']
    Popularity = Json_Request['results'][0]['popularity']
    Image = Json_Request['results'][0]['poster_path']
 
    Shows_0 = [Name, Overview, Popularity, Image]
    CompiledImage_0 = compile_image(Shows_0[3])
    
    Name = Json_Request['results'][1]['name']
    Overview = Json_Request['results'][1]['overview']
    Popularity = Json_Request['results'][1]['popularity']
    Image = Json_Request['results'][1]['poster_path']

    Shows_1 = [Name, Overview, Popularity, Image]
    CompiledImage_1 = compile_image(Shows_1[3])

    Name = Json_Request['results'][2]['name']
    Overview = Json_Request['results'][2]['overview']
    Popularity = Json_Request['results'][2]['popularity']
    Image = Json_Request['results'][2]['poster_path']

    Shows_2 = [Name, Overview, Popularity, Image]
    CompiledImage_2 = compile_image(Shows_2[3])

    Name = Json_Request['results'][3]['name']
    Overview = Json_Request['results'][3]['overview']
    Popularity = Json_Request['results'][3]['popularity']
    Image = Json_Request['results'][3]['poster_path']

    Shows_3 = [Name, Overview, Popularity,Image]
    CompiledImage_3 = compile_image(Shows_3[3])

    Name = Json_Request['results'][4]['name']
    Overview = Json_Request['results'][4]['overview']
    Popularity = Json_Request['results'][4]['popularity']
    Image = Json_Request['results'][4]['poster_path']

    Shows_4 = [Name, Overview, Popularity, Image]
    CompiledImage_4 = compile_image(Shows_4[3])
 
    Name = Json_Request['results'][5]['name']
    Overview = Json_Request['results'][5]['overview']
    Popularity = Json_Request['results'][5]['popularity']
    Image = Json_Request['results'][5]['poster_path']

    Shows_5 = [Name, Overview, Popularity, Image]
    CompiledImage_5 = compile_image(Shows_5[3])

    Name = Json_Request['results'][6]['name']
    Overview = Json_Request['results'][6]['overview']
    Popularity = Json_Request['results'][6]['popularity']
    Image = Json_Request['results'][6]['poster_path']

    Shows_6 = [Name, Overview, Popularity, Image]
    CompiledImage_6 = compile_image(Shows_6[3])
    

   


    
