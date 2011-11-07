from django.contrib.comments.models import Comment

FIELD_INDEXES = {
    Comment: {'indexed': ['object_pk']}
}
