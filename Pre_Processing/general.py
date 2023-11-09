import os


# Each website is a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)


# Create queue and crawled files (if not created)
def createDataFiles(Project_Name, baseUrl):
    queue = os.path.join(Project_Name , 'queue.txt')
    crawled = os.path.join(Project_Name,"crawled.txt")
    if not os.path.isfile(queue):
        writeFile(queue, baseUrl)
    if not os.path.isfile(crawled):
        writeFile(crawled, '')


# Create a new file
def writeFile(path, data):
    with open(path, 'w') as f:
        f.write(data)


# Add data onto an existing file
def appendToFile(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Delete the contents of a file
def deleteFileContents(path):
    open(path, 'w').close()


# Read a file and convert each line to set items
def fileToSet(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Iterate through a set, each item will be a line in a file
def setToFile(links, file_name):
    with open(file_name,"w",encoding="utf-8") as f:
        for l in sorted(links):
            f.write(l+"\n")
