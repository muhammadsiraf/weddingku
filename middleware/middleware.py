from firebase import firebase

firebase = firebase.FirebaseApplication(
    'https://wedding-invitation-52b05-default-rtdb.firebaseio.com/', None)

def create():
    
    data = {
        'Name': 'helmy rafi nawawi',
        'Email': 'lionissinga@gmail.com',
        'phone': '08122222222',
        'afiliation': 'Friend',
        'confirmation': 'Yes'
    }

    result = firebase.post('Register', data)
    print(result)

def get():

    result = firebase.get('/Register/','')
    print(result)

def put():

    result = firebase.put('Register/-MSpyfd0O1gkxFznPEtU','Name','Santoyono')
    print(result)

def delete():
    result = firebase.delete('Register', '-MSpyfd0O1gkxFznPEtU')
    print('deleted')

# get()
create()
