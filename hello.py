import fire

def hello(name="Worlds"):
  return "Helllo %s!!" % name

if __name__ == '__main__':
  fire.Fire(hello)
