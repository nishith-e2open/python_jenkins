import fire

def hello(name="Worlds"):
  return "Ola %s!!" % name

if __name__ == '__main__':
  fire.Fire(hello)
