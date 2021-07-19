from app.models import User, Post, Comment, Vote
from app.db import Session, Base, engine

#drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

# insert users
db.add_all([
    User(username='alesmonde0', email='nwestnedge0@cbc.ca', password='password123'),
    User(username='jwilloughway1', email='rmebes1@sogou.cm', password='password123'),
    User(username='iboddam2', email='cstoneman2@last.fm', password='password123'),
    User(username='dstanmer3', email='ihellier3@goo.ne.jp', password='password123'),
    User(username='djiri4', email='gmidgley4@weather.com', password='password123')
])

db.commit()

# insert posts
db.add_all([
  Post(title='How to learn data science: from data mining to machine learning', post_url='https://hub.packtpub.com/how-to-learn-data-science-from-data-mining-to-machine-learning/', user_id=1),
  Post(title='What’s new in Angular 12', post_url='https://www.infoworld.com/article/3607428/whats-new-in-angular-12.html', user_id=1),
  Post(title='Using Proxies with Redux Types', post_url='https://reactjsnews.com/', user_id=2),
  Post(title='Oracle Offers Java Management Service', post_url='https://www.infoworld.com/article/3621690/oracle-offers-java-management-service.html', user_id=3),
  Post(title='Build a Java application in Visual Studio Code', post_url='https://www.infoworld.com/article/3619031/build-a-java-application-in-visual-studio-code.html', user_id=4)
])

db.commit()

# insert comments
db.add_all([
  Comment(comment_text='Great article about data science and machine learning. Thanks for sharing.', user_id=1, post_id=2),
  Comment(comment_text='Angular is a great programming technology.', user_id=1, post_id=3),
  Comment(comment_text='This is very helpful information on Redux types.', user_id=2, post_id=1),
  Comment(comment_text='I am so excited for the Java management Service.', user_id=2, post_id=3),
  Comment(comment_text='Java is my favorite programming language.', user_id=3, post_id=3)
])

db.commit()

# insert votes
db.add_all([
  Vote(user_id=1, post_id=2),
  Vote(user_id=1, post_id=4),
  Vote(user_id=2, post_id=4),
  Vote(user_id=3, post_id=4),
  Vote(user_id=4, post_id=2)
])

db.commit()

db.close()