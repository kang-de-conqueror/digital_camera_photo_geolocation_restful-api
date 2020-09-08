from fabric import Connection, task
import requests


ROOT = "/home/batch2-avengers/digicam"
# ROOT = "/Users/khangkhag/digital-camera-photo-geolocation-restful-api-server-khang_tran_khang_vu"
droplet1 = Connection("68.183.182.223", user="batch2-avengers", port=22, connect_kwargs={'password': 'admin'})
droplet2 = Connection("165.22.99.116", user="batch2-avengers", port=22, connect_kwargs={'password': 'admin'})


def download_source(connection, source_link):
    """ Download the GitHub tar gzipped file corresponding to the release you want to deploy
    to the tmp folder
    """
    connection.run("mkdir -p tmp && cd ./tmp && curl -vLJO -H 'Authorization: token 43382a292eb5fba713db01b11285aae7bf4171fb' %s" % source_link)


def decompress_tar(connection, file_name, version):
    """ Decompress the tar gzipped file to a new folder named against the version of your release (under `~/digicam`)
    """
    # Unzip
    connection.run("cd ./tmp && tar -zxvf %s" % file_name)
    # Rename and move to home folder
    connection.run("cd ./tmp && mv %s ../%s" % (file_name.replace(".tar.gz", ""), version))
    # delete /tmp files
    connection.run("cd ./tmp && rm -rf *")


def make_symbolic_link(connection, version):
    """ Delete and create the symbolic link `current` to point to the new folder
    """
    # remove current folder
    connection.run("rm -f current")
    # Create symlink
    connection.run("ln -s %s current" % version)


def get_release_info():
    # Get the lastest release version
    url = 'https://api.github.com/repos/intek-training-jsc/digital-camera-photo-geolocation-restful-api-server-khang_tran_khang_vu/releases/latest'
    headers = {'Authorization': 'token 43382a292eb5fba713db01b11285aae7bf4171fb'}
    github_request = requests.get(url = url, headers = headers)
    response = github_request.json()
    version = response['tag_name'].replace('v', '')
    file_name = "digital-camera-photo-geolocation-restful-api-server-khang_tran_khang_vu-%s.tar.gz" % version
    source_link = "'https://github.com/intek-training-jsc/digital-camera-photo-geolocation-restful-api-server-khang_tran_khang_vu/archive/v%s.tar.gz'" % version
    return version, file_name, source_link


@task
def deploy(ctx):
    version, file_name, source_link = get_release_info()

    for connection in [droplet2, droplet1]:
        with connection.cd(ROOT):
            download_source(connection, source_link)
            decompress_tar(connection, file_name, version)
            make_symbolic_link(connection, version)


@task
def jenkin(ctx):
    for connection in [droplet2, droplet1]:
        with connection.cd(ROOT):
            connection.run('cd current && supervisorctl reread && supervisorctl update')
            connection.run('(supervisorctl stop b2-avengers-digicam-apiserver && supervisorctl start b2-avengers-digicam-apiserver) || supervisorctl start b2-avengers-digicam-apiserver')
        # connection.run('(docker container rm -f avengers && docker image rm -f khagkhangg/avengersdigicam) || docker image rm -f khagkhangg/avengersdigicam')
        # connection.run('docker run -p 8000:8000 -d --name avengers khagkhangg/avengersdigicam')
