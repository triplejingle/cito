# name is PyGithub !
import os


import git
from git import Repo


def getAllContentFromRoot():
    print("hoi")
    # g = Github("53a08804b5baf4420aae08909dcffc262c024371")
    # repo = g.get_repo("triplejingle/OSRSPB")
    # files = repo.get_contents("")
    # path = os.getcwd()
    # os.chdir('./scripts/')
    # for content_file in files:
    #    file = content_file
    #    print(file.name)
    #    if file.encoding is not None:
    #        f = open(file.name, "w+")
    #        content = base64.b64decode(file.content)
    #        f.write(content.decode('utf-8'))
    #        f.close()
    #    os.chdir(path)


def download_scripts():
    destination="./scripts"
    #Repo.clone_from("https://github.com/triplejingle/OSRSPB", destination)

    path = os.getcwd()
    os.chdir(destination)
    cmd = git.cmd.Git()
    cmd.execute("git fetch --all")
    cmd.execute("git reset --hard ")
    os.chdir(path)
    try:
        print("")
        #o.fetch(refspec=None, progress=None)
        #o.pull()
    except Exception as error:
        print(error)

    # path = os.getcwd()
    # os.chdir('./scripts/')
    # repo.fetch()
    # contents = repo.get_contents("")
    # os.chdir(path)


# 53a08804b5baf4420aae08909dcffc262c024371

if __name__ == "__main__":
    download_scripts()
