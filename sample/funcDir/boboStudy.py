import bobo

@bobo.query('/jay/')
def hello(person : str) -> str:
    return r'Hello %s !' % person

# @bobo.query('/')
# def hello() -> str:
#     return r'hello world'