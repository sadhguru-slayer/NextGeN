from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
import requests
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import random
from .models  import *


# Create your views here.
def index(request):

    url = "https://linkedin-profiles-and-company-data.p.rapidapi.com/profile-details"

    payload = {
    	"profile_id": "farhan-ahmed-63324b242",
    	"profile_type": "personal",
    	"contact_info": False,
    	"recommendations": False,
    	"related_profiles": False
    }
    headers = {
    	"content-type": "application/json",
    	"X-RapidAPI-Key": "7f28671f87mshd4afb820346decbp1546c4jsn4950288ecf6a",
    	"X-RapidAPI-Host": "linkedin-profiles-and-company-data.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    json_data = response.json()


    git_username = "sadhguru-slayer"
    
    token = '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'

# GitHub API endpoint you want to access
    url = 'https://api.github.com/user/repos'  # You can change this URL to the endpoint you need

    # Set up headers with authentication using the token
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json'
    }

    # Make a GET request to the GitHub API
    responses = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if responses.status_code == 200:
        # Parse the JSON response
        data = responses.json()
        # print(data)
    else:
        # Print error message if the request was not successful
        print(f"Error: {response.status_code}, {response.text}")


    

    # tweet = "@MehranShakarami today's cold @ home 😒 https://mehranshakarami.com"
    tweet = 'Great content! subscribed 😉'

    # precprcess tweet
    tweet_words = []

    for word in tweet.split(' '):
        if word.startswith('@') and len(word) > 1:
            word = '@I'

        elif word.startswith('http'):
            word = "http"
        tweet_words.append(word)

    tweet_proc = " ".join(tweet_words)

    # load model and tokenizer
    roberta = "cardiffnlp/twitter-roberta-base-sentiment"

    model = AutoModelForSequenceClassification.from_pretrained(roberta)
    tokenizer = AutoTokenizer.from_pretrained(roberta)

    labels = ['Negative', 'Neutral', 'Positive']

    # sentiment analysis
    encoded_tweet = tokenizer(tweet_proc, return_tensors='pt')
    # output = model(encoded_tweet['input_ids'], encoded_tweet['attention_mask'])
    output = model(**encoded_tweet)

    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    for i in range(len(scores)):

        l = labels[i]
        s = scores[i]
        print(l,s)


# Generate two random float values between 0 and 100
    value1 = random.uniform(0, 100)
    value2 = random.uniform(0, 100)
    value3 = random.uniform(0, 100)
    
    # Calculate the sum of the values
    total = value1 + value2 + value3
    
    # If the total is greater than 100, adjust the values to make the sum exactly 100
    if total > 100:
        scale_factor = 100 / total
        value1 *= scale_factor
        value2 *= scale_factor
        value3 *= scale_factor
    
    # Print the generated values
    print(f"Value 1: {value1:.2f}")
    print(f"Value 2: {value2:.2f}")
    print(f"Value 3: {value3:.2f}")
    print(f"Sum: {value1 + value2 + value3:.2f}")

    params = {
        'json_data': json_data,
        'git_username':git_username
    }

    return render(request, 'index.html', context=params)

def home(request):
    return render(request,'../templates/home.html')

def apply(request):
    if request.method=="POST":
        First_Name=request.POST.get("fn")
        Second_Name=request.POST.get("ln")
        Email=request.POST.get("email")
        Linkedin_Profile=request.POST.get("lin")
        Github_Profile=request.POST.get("git")
        Twitter_Profile=request.POST.get("twit")

        applied = Applicant(
            First_Name=First_Name,
            Second_Name=Second_Name,
            Email=Email,
            Linkedin_Profile=Linkedin_Profile,
            Github_Profile=Github_Profile,
            Twitter_Profile=Twitter_Profile
        )
        applied.save()
    return render(request,'../templates/form.html')