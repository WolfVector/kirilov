import subprocess

def get_requirements(file) -> set:
    with open(file) as f:
        data = f.read().splitlines()
    
    return set(data)

def pip_freeze() -> set:
    requirements = subprocess.getoutput("pip freeze").split("\n")
    return set(requirements)

def cmpreq(file1_requirements, file2_requirements, output, download, path) -> None:
    print("---------Added requiriments---------")
    
    with open("kirilov_added.txt", "w") as f:
        for requirement in file1_requirements:
            if requirement not in file2_requirements and "kirilov" not in requirement:
                print(requirement)
                
                if output:
                    f.write(requirement + '\n')
                if download:
                    try:
                        subprocess.run(["pip", "download", "--no-deps", requirement, "-d", path])
                    except Exception as e:
                        print(e)
