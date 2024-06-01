def context_processor_example(request):
    return {
        'example': 'veio do context processor (example)',
        'teste':'testando o context',
    }

def site_setup(request):
    return {
        'site_setup': 'veio do context processor (site setup)',
        'teste':'testando o context',
    }