import datetime

from django import forms
from django.conf import settings
from django.utils.translation import ugettext as _
from django.contrib.comments.forms import COMMENT_MAX_LENGTH

from userena.forms import EditProfileForm as BaseEditProfileForm

from .models import Post, Comment, User
from .widgets import DateMask

STATE_CHOICES = (('draft', _('Draft')),
                 ('published', _('Published')))


class PostForm(forms.ModelForm):
    state = forms.ChoiceField(widget=forms.Select, choices=STATE_CHOICES)

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        if 'date_published' not in self.initial:
            self.initial['date_published'] = datetime.date.today()

    class Meta:
        model = Post
        widgets = {'date_published': DateMask}


class CommentForm(forms.ModelForm):
    user_name = forms.CharField(label=_("Name"), max_length=50)
    user_email = forms.EmailField(label=_("Email address"))
    user_url = forms.URLField(label=_("URL"), required=False)
    comment = forms.CharField(label=_('Comment'), widget=forms.Textarea,
                                    max_length=COMMENT_MAX_LENGTH)

    def __init__(self, post=None, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        if not self.instance.pk:
            self.instance.content_object = post

        self.instance.site_id = settings.SITE_ID

    class Meta:
        model = Comment
        fields = ('user_name', 'user_email', 'user_url', 'comment')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        widgets = {'password': forms.PasswordInput}


class EditProfileForm(BaseEditProfileForm):
    """
    Extends EditProfileForm from userena excluding some
    fields: user and privacy (not used right now)

    """

    class Meta(BaseEditProfileForm.Meta):
        exclude = ('user', 'privacy')
