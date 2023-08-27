from django.shortcuts import render
import pickle
from .forms import classiy_form
# Create your views here.




def simple_model(request):
    result = None
    form = classiy_form(request.POST)
    if request.method == 'POST' and form.is_valid():
        cv = pickle.load(open('modelcv.pkl', 'rb'))
        model = pickle.load(open('model.pkl', 'rb'))
        msg = [form.cleaned_data.get("message")]
        msg_count = cv.transform(msg)
        result = model.predict(msg_count)
        
        ctx = {
            'form':classiy_form,
            'result':result,
        }

        return render(request, 'indexx.html', ctx)
    else:
        ctx={'form':classiy_form, 'result':None}
        return render(request, 'indexx.html', ctx)