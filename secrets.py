import os


secret = os.environ.get("SECRET")
envvar = os.environ.get("ENV_VARIABLE")


print(f"secret = {secret}")
print(f"envvar = {envvar}")