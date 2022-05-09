# PITCH-PERFECT

### Description
Its a Python-based web application that allows a user to post and interact with other pitches submitted by other users. A user must first signup and then login to the application for use.

## Author

👤 **Author**
-Kipkemoi Jared Kevin

- GitHub: [@JAREDKEVIN](https://github.com/JAREDKEVIN)

## Technologies Used

- HTML
- CSS
- PYTHON `3.8`
- PYTHON SHELL 
- FLASK
- FLASK_BOOTSTRAP
- HEROKU

### User Stories
As a user I would like to;

- see the pitches that other people have posted. 
- vote on the pitch I like and give it a downvote or upvote. 
- be signed in so that I can leave a comment.
- receive a welcoming email once I sign up. 
- view the pitches I have created in my profile page. 
- comment on the different pitches and leave feedback. 
- submit a pitch in any category. 
- view the different pitch categories.


## SPECS:
These are the actions the user will do, inputs required and their outputs on the page. 

  | Action    | Input                                      | Output                        |
  | ----------|:-------------                              | :------                       |
  | Load page | On page load                               | Displays the homepage         |
  | Sign up   | email, username, password, confirm password| Redirected to login page page |
  | Login     | username, password                         | Redirect to homepage          |
  | Select Comment| a comment                              | Your comment displayed        |
  |           |                                            |                               |
## Live Demo

[Live Demo Link]()


### Installation Process

- Clone the repository using the link below

```
$ git clone https://github.com/JAREDKEVIN/PITCH-PERFECT.git

```

- Create a directory and install the requirements

  ```
  cd Pitches
  pip install -r requirements.txt
  ```
- Export configurations
  ```
  Database URL
  Secret Key
  Mail_username
  Mail_password
  ```
- Run the application using;
  ```
  python3 manage.py server
  ```
- Test it if its working using;
  ```
  python3  manage.py test
  ```
- Open the application on your browser , preferably `chrome` using port `127.0.0.1:5000`


## Show your support

Give a ⭐️ if you like this project!

## Acknowledgments

- I would like to acknowledge Moringa school for giving me this opportunity to learn software development.
- Appreciations to  my TM `Barclay Koin` for the support she gives me.

## 📝 License

This project is [MIT](LICENCE.md) licensed.
