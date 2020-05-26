#### request object: 
+ It is the extension of HttpRequest object.It's main role is request.data attribut.It is just like forms.POST in django.
+ It provides more flexible request parsing from one type data into another type of data

####response object:

+ It is the extension of HttpResponse object.This object easily identify the content type to be displayed to the client or on the browser.
+ This is just like the TemplateResponse in django.

####Status code:
+ status=status.HTTP_200_OK : success 
+ status=status.HTTP_201_CREATED : New record/Update
+ status=status.HTTP_204_NO_CONTENT :Record deleted
+ status=status.HTTP_400_BAD_REQUEST : Invalid fields given
+ status=status.HTTP_404_NOT_FOUND : Record not available
 

