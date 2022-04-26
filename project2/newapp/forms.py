from django.forms import ModelForm
from .models import Post, SubsUser
from django.contrib.auth.models import User

# Создаём модельную форму
class PostForm(ModelForm):

    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Post
        fields = ['author', 'categoryType', 'title', 'text', 'postCategory']


# Создаём модельную форму для пользователя
class UserForm(ModelForm):

    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class SubscribeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SubscribeForm, self, ).__init__(*args, **kwargs)
        self.fields['userThrough'].queryset = User.objects.filter(id=2)

    class Meta:
        model = SubsUser
        fields = ['subsThrough', 'userThrough']