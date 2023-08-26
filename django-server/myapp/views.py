from django.shortcuts import render
from django.http import HttpResponse
import openai
# Create your views here.
def api(request):
    response = openai.Image.create(
        prompt="a white siamese cat",
        n=1,
        size="256x256",
        api_key='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',
        
    )
    image_url = response['data'][0]['url']
    return image_url