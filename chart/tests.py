[uwsgi]

chdir           = /home/app/blog

module          = blog.wsgi --chmod-socket=666

home            = /home/app/virtualenv


master          = true

processes       = 10

socket          = /home/app/blog/blog.sock

vacuum          = true