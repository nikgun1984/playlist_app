"""Forms for playlist app."""

from wtforms import SelectField, TextAreaField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired

class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    # Add the necessary code to use this form
    name = StringField('Name', validators=[InputRequired("Please enter the name of playlist")])
    description = TextAreaField('Description', validators=[InputRequired("Please enter description of the playlist")])


class SongForm(FlaskForm):
    """Form for adding songs."""

    # Add the necessary code to use this form
    title = StringField('Title', validators=[InputRequired("Please enter the title of song")])
    artist = StringField('Artist', validators=[InputRequired("Please enter the artist of name")])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
