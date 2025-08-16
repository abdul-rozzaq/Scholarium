
def remove_api(hostname: str):

    if hostname.startswith("api."):
        return hostname[4:]

    return hostname
