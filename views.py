"""
Routes and views for the flask application.
"""
from datetime import datetime
from Entertainment_Hub.Data.Content import ApiData
from flask import render_template
from flask import send_file


from Entertainment_Hub import app
from newsapi import NewsApiClient
import requests

from Entertainment_Hub.Data.Content import ApiData
from Entertainment_Hub.Data.Content import Tech
from Entertainment_Hub.Data.Content import Sports

from Entertainment_Hub.Data.Content import Entertainment
from Entertainment_Hub.Data.Content import Business
from Entertainment_Hub.Data.Content import Mtv
from Entertainment_Hub.Data.Content import BuzzFeed
from Entertainment_Hub.Data.Content import Reddit

@app.route('/')
def home():
    """Renders the home page."""   

    return render_template('index.html',getheadlineTitle= ApiData.Headline_Title,getheadlinePublishedAt = ApiData.Headline_PublishedAt, 
                           getheadlineDescription = ApiData.Headline_Description, getheadlinetoImage = ApiData.Headline_ToImage,

                           gettechTitle = Tech.Tech_Title, gettechPublishedAt = Tech.Tech_PublishedAt, gettechDescription = Tech.Tech_Description,
                           gettechImg = Tech.Tech_ToImage,
                           
                           getsportsTitle = Sports.Sport_Title, getsportsPublishedAt = Sports.Sport_PublishedAt, getsportsDescription = Sports.Sport_Description,
                           getsportsImg = Sports.Sport_ToImage,
                           
                           getentTitle = Entertainment.Entertainment_Title, getentPublishedAt = Entertainment.Entertainment_PublishedAt, getentDescription = Entertainment.Entertainment_Description,
                           getentImg = Entertainment.Entertainment_ToImage,
                           
                           getbusinessTitle = Business.Business_Title, getbusinessPublishedAt = Business.Business_Title, getbusinessDescription = Business.Business_Description,
                           getbusinessImg = Business.Business_ToImage,
                           
                           getmtvTitle = Mtv.Mtv_Title, getmtvPublishedAt = Mtv.Mtv_PublishedAt, getmtvDescription = Mtv.Mtv_Description, getmtvImg = Mtv.Mtv_ToImage,

                           getBuzzfeedTitle = BuzzFeed.BuzzFeed_Title, getbuzzfeedDescription = BuzzFeed.BuzzFeed_Description, getbuzzfeedPublished = BuzzFeed.BuzzFeed_PublishedAt,
                           getbuzfeedImg = BuzzFeed.BuzzFeed_ToImage, getbuzzfeedContent = BuzzFeed.BuzzFeed_Content,
                           
                           geredditTitle = Reddit.Reddit_Title, getredditPublishedAt = Reddit.Reddit_PublishedAt, getredditDescrip = Reddit.Reddit_Description, getredditImg = Reddit.Reddit_ToImage,
                           getredditContent = Reddit.Reddit_Content)
                          
                           
@app.route('/login')
def hello():
    """Renders the home page."""   

    return render_template('loginpage.html')

@app.route('/world')
def world():
    """Renders the expanded word page."""   

    

    return render_template('worldExpand.html', worldexpandeContent =ApiData.Headline_Content, wordldexpandTitle = ApiData.Headline_Title, worldexpandImg = ApiData.Headline_ToImage,
                           worldexpandDesc = ApiData.Headline_Description)

@app.route('/tech')
def tech():
    """Renders the expanded tech page."""   

    return render_template('techExpand.html', techexpandContent = Tech.Tech_Content, techexpandTitle = Tech.Tech_Title, techexpandDescripion = Tech.Tech_Description, expandtechImg = Tech.Tech_ToImage)

@app.route('/sports')
def sports():
    """Renders the expanded sports page."""   

    return render_template('sportsExpand.html', sportsexpandContent = Sports.Sport_Content, sportsexpandTitle = Sports.Sport_Title, expandsportsDescripion = Sports.Sport_Description, expandtechImg = Sports.Sport_ToImage)

@app.route('/entertainment')
def entertainment():
    """Renders the expanded entertainment page."""   

    return render_template('entertainmentExpand.html', entexpandContent = Entertainment.Entertainment_Content, entexpndTitle = Entertainment.Entertainment_Title, expandentDescription = Entertainment.Entertainment_Description,
                           expandentImg = Entertainment.Entertainment_ToImage)
                           

@app.route('/business')
def business():
    """Renders the expanded business page."""   

    return render_template('businessExpand.html', businessexpandContent = Business.Business_Content, businessexpandTitle = Business.Business_Title, businessexpandDescription = Business.Business_Description,
                           businessexpandImg = Business.Business_ToImage)

@app.route('/mtv')
def mtv():
    """Renders the expanded mtv page."""   

    return render_template('mtvExpand.html', mtvexpandContent = Mtv.Mtv_Content, mtvexpadTitle = Mtv.Mtv_Title, mtexpandDescription = Mtv.Mtv_Description, mtvexpandImg = Mtv.Mtv_ToImage)

@app.route('/more1')
def lowerCard_1():

    """Renders the expandeds more detail in first lower card"""   

    return render_template('lowerCard1.html',buzzfeedLowerCardContent = BuzzFeed.BuzzFeed_Content, buzzfeedLowerCardTitle = BuzzFeed.BuzzFeed_Title, buzzfeedLowerCardImg = BuzzFeed.BuzzFeed_ToImage,
                           buzzfeedlowerCardDes = BuzzFeed.BuzzFeed_Description)

@app.route('/more2')
def lowerCard_2():

    """Renders the expandeds more detail in first second card"""   

    return render_template('lowerCard2.html', redditLowerCardContent = Reddit.Reddit_Content, redditLowerCardTitle = Reddit.Reddit_Title, redditLowerCardImg = Reddit.Reddit_ToImage,
                           redditLowerCardDes = Reddit.Reddit_Description)
