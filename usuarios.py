class Comment:
    id_comment = 0
    comentario = ""
    fecha = ""
    comments = []
    comment = {}

    def __init__(self, id_comment, comentario, fecha):
        self.id_comment = id_comment
        self.comentario = comentario
        self.fecha = fecha

    def crear_comment(self):
        self.comment = {
            'id_comment': self.id_comment,
            'comentario': self.comentario,
            'fecha': self.fecha
        }
        self.comments.append(self.comment)


class Post(Comment):
    id_post = 0
    titulo = ""
    nombre_comment = ""
    id_post_comment = ""
    pots = []
    post = {}

    def __init__(self, id_post, titulo, nombre_comment, id_post_comment, id_comment, comentario, fecha):
        Comment.__init__(self, id_comment, comentario, fecha)
        self.id_post = id_post
        self.titulo = titulo
        self.nombre_comment = nombre_comment
        self.id_post_comment = id_post_comment

    def crear_post(self):
        self.post = {
            'id_post': self.id_post,
            'titulo': self.titulo,
            'nombre_comment': self.nombre_comment
        }
        self.pots.append(self.post)


class User(Post):
    id_user = 0
    nombre = ""
    apellido = ""
    idetificacion = 0
    id_user_post = 0
    usuarios = []
    usuario = {}

    def __init__(self, id_user, nombre, apellido, identificacion, id_user_post, id_post, titulo, nombre_comment,
                 id_post_comment, id_comment,
                 comentario, fecha):
        Post.__init__(self, id_post, titulo, nombre_comment, id_post_comment, id_comment, comentario, fecha)
        self.id_user = id_user
        self.nombre = nombre
        self.apellido = apellido
        self.idetificacion = identificacion
        self.id_user_post = id_user_post

    def crear_usuario(self):
        self.usuario = {

            'id': self.id_user,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'identificacion': self.idetificacion,
            'id_user_post': self.id_user_post,
            'id_commet': self.id_comment
        }

        self.usuarios.append(self.usuario)

    def update_usuario(self, id_user, id_post):
        for u in self.usuarios:
            if u['id'] == id_user:
                u['id_user_post'] = id_post
                print('id post: {}'.format(u['id_user_post']))

            else:
                print('usuario no encontrado')

    def update_commets(self, id_post, id_coment):
        for u in self.usuarios:
            if u['id_user_post'] == id_post:
                u['id_commet'] = id_coment
                print('id_commet: {}'.format(u[id_coment]))

    def buscar_usuario(self):

        for u in self.usuarios:
            if u['id'] == self.id_user:
                print('usuario: ' + u['nombre'])
                for y in self.pots:
                    if u['id_user_post'] == y['id_post']:
                        print('titulo post: ' + y['titulo'])


def menu():
    salir = 0
    while salir != 1:
        print('---MENU DE OPCIONES---')
        print('1) crear usuarios')
        print('2) crear post')
        print('3) crear comment')
        print('4) buscar usuarios')
        print('5) salir')
        seleccion = int(input('digite una opcion:'))
        if seleccion == 1:

            print('---crear usuarios--')
            id = int(input('Digite el id de usuario: '))
            nombre = input('Digite nombre de usuario: ')
            apellido = input('Digite apellido de usuario: ')
            identificacion = input('Digite  identificacion de usuario: ')
            usuario = User(id, nombre, apellido, identificacion, 0, 0, '', '', 0, 0, '', '')
            usuario.crear_usuario()
        elif seleccion == 2:
            print('---crear post--')
            id_user = int(input('digite el id del usuario: '))
            id = int(input('Digite el id post: '))
            titulo = input('Digite titulo: ')
            nombre_com = input('Digite nombre de comentario: ')
            post = Post(id, titulo, nombre_com, 0, 0, '', '')
            post.crear_post()
            usuario = User(0, '', '', 0, id, 0, '', '', 0, 0, '', '')
            usuario.update_usuario(id_user, id)

        elif seleccion == 3:
            print('---crear comments---')
            id_post = int(input('digite id de post: '))
            id_comment = int(input('digite id de commentario: '))
            comentario = input('digite su comentatio: ')
            fecha = input('digite fecha: ')
            commentario = Comment(id_comment, comentario, fecha)
            commentario.crear_comment()
            usuario = User(0, '', '', 0, 0, 0, '', '', 0, id_comment, '', '')
            usuario.update_usuario(id_post, id_comment)
        elif seleccion == 4:
            print('buscar usuarios')
            id = int(input('digite id a buscar: '))
            usuario = User(id, '', '', 0, 0, 0, '', '', 0, 0, '', '')
            usuario.buscar_usuario()


        elif seleccion == 5:
            print('salir')
            salir = 1


menu()
