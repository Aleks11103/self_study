def build_query_string(params):
    ans = []
    for key in sorted(params.keys()):
        ans.append(f'{key}={params[key]}')
    return '&'.join(ans)


print(build_query_string({'name': 'timur', 'age': 28}))
