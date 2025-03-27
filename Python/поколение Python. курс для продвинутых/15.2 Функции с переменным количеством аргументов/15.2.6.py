def info_kwargs(**kwargs):
    for key in sorted(kwargs.keys()):
        print(f"{key}: {kwargs[key]}")
