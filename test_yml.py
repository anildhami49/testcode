import yaml

with open('First.ymal', 'r') as file:
    try:
        print(yaml.safe_load(file))
    except yaml.YAMLEError as exc:
        print(exc)
        