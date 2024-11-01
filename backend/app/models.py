from . import db  
from datetime import datetime

class Word(db.Model):
    __tablename__ = 'words'
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)
    definition = db.Column(db.String(255), nullable=False)
    example = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow, nullable=False)

    def __repr__(self):
        return f'<Word {self.word}>'

    def 