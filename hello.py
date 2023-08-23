import fire

def hello(name="World"):
  return "Hi!! Welcome to E2open @%s!" % name
if __name__ == '__main__':
  fire.Fire(hello)
