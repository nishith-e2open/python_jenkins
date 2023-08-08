import fire

def hello(name="World"):
  return "Helllooooo %s!!" % name

if __name__ == '__main__':
  fire.Fire(hello)
