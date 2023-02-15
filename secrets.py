import os


secret = os.environ.get("SECRET")
envvar = os.environ.get("ENV_VARIABLE")
envvars = os.environ



print(f"secret = {secret}")
print(f"envvar = {envvar}")
print(f"envvars = {envvars}")