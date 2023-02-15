import os


secret = os.environ.get("SECRET")
envvar = os.environ.get("ENV_VARIABLE")


print(f"secret = {secrets.secret}")
print(f"envvar = {variables.envvar}")