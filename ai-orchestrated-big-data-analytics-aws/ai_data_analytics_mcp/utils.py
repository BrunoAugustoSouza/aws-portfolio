def load_prompt(path: str, **kwargs):

    with open(path, "r") as f:
        template = f.read()

    return template.format(**kwargs)