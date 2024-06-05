from site_setup.models import SiteSetup

def context_processor_example(request):
    return {
        'example': 'veio do context processor (example)',
        'teste':'testando o context',
    }

def site_setup(request):
    setup = SiteSetup.objects.order_by('-id').first()
    

    return {
        'site_setup': setup,
    }