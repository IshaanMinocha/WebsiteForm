from django.shortcuts import redirect, render
from .models import Document,start_id
from .forms import DocumentForm


# starting_id=0
# def send_id_to_model():
#     return (starting_id+1)

# Create your views here.

start_id_duplicate = start_id
def my_view(request):
    print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            name = request.POST.get('name')
            global start_id_duplicate
            unique_id = start_id_duplicate+2
            newdoc = Document(docfile=request.FILES['docfile'], name=name, unique_id=unique_id)
            newdoc.save()
            # global start_id_duplicate
            start_id_duplicate+=1
            # Redirect to the document list after POST
            return redirect('my-view')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form
    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'list.html', context)