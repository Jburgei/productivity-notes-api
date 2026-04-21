from app import app
from models import db
from models.user import User
from models.note import Note

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create users
    user1 = User(username='alice')
    user1.password = 'password123'

    user2 = User(username='bob')
    user2.password = 'password123'

    db.session.add_all([user1, user2])
    db.session.commit()

    # Create notes
    notes = [
        Note(title='Alice Note 1', content='Finish Flask lab', user_id=user1.id),
        Note(title='Alice Note 2', content='Study session auth', user_id=user1.id),
        Note(title='Bob Note 1', content='Buy groceries', user_id=user2.id),
    ]

    db.session.add_all(notes)
    db.session.commit()

    print("Database seeded successfully!")