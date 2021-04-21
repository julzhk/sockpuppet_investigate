import json
import random
from django.shortcuts import render

def vue(request):
    names = ("bob", "dan", "jack", "lizzy", "susan")

    items = []
    for i in range(100):
        items.append({
            "name": random.choice(names),
            "age": random.randint(20,80),
            "url": "https://example.com",
        })

    context = {}
    context["items"] = items
    context["items_json"] = json.dumps(items)
    return render(request, 'vue_list.html', context)
