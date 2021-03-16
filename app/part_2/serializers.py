def note_serializer(note):
    """ Сериализация возвращаемого объекта Note """
    return {
        'id': note.pk,
        'title': note.title,
        'message': note.message,
        'public': note.public,
        'date_add': note.date_add,
        'author_id': note.author_id,
        'author': {
            'pk': note.author.pk,
            'name': note.author.username,
        },
    }
