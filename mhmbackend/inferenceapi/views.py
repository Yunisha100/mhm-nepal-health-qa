from django.shortcuts import render
# Use a pipeline as a high-level helper
from transformers import pipeline
from django.http import JsonResponse
from .models import GeneratedText


# Create your views here.
def generate_text(request):
    input_text = request.GET.get('input_text','')
    pipe = pipeline("text2text-generation", model="Chhabi/mt5-small-finetuned-Nepali-Health-50k-2", max_new_tokens=128)
    result = pipe(input_text)
    generated_text = result[0]['generated_text']
    
    # Save input text and generated text in the database
    GeneratedText.objects.create(input_text=input_text, generated_text=generated_text)
    
    return JsonResponse({'generated_text': result[0]['generated_text']})