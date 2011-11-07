import datetime

from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.contrib.comments.models import Comment as BaseComment
from django.contrib.auth.models import User as BaseUser

from userena.models import (UserenaBaseProfile,
                            UserenaSignup)

from django_fsm.db.fields import (FSMField,
                                  transition)


class User(BaseUser):
    def get_absolute_url(self):
        return reverse('userena_profile_edit', args=(self.username,))

    def save(self):
        return UserenaSignup.objects.create_user(self.username,
                                                 self.email,
                                                 self.password,
                                                 active=True,
                                                 send_email=False)

    class Meta:
        proxy = True
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class Profile(UserenaBaseProfile):
    user = models.OneToOneField(BaseUser,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')


class Post(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(_('Slug'))
    text = models.TextField(_('Text'))
    user = models.ForeignKey(BaseUser, related_name='posts', editable=False)

    date_published = models.DateField(_('Date published'), null=True,
                                                           blank=True)
    state = FSMField(_('State'), default='draft')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogages_core:post_form', args=(self.pk,))

    def get_year_month(self):
        return datetime.date(self.date_published.year,
                             self.date_published.month,
                             1)

    @transition(source='draft', target='published')
    def publish(self):
        pass

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ('-date_published',)


class Comment(BaseComment):
    def get_absolute_url(self):
        return reverse('blogages_core:comment_form', args=(self.pk,))

    class Meta:
        proxy = True
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        ordering = ('-submit_date',)
