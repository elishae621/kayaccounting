from main.models import Instance

class AddConfigToAllContext():
    def __init__(self, get_response):
        self.get_response = get_response
        if len(Instance.objects.all()) != 1:
            Instance.objects.all().delete()
            Instance.objects.create()
        self.instance = Instance.objects.values()[0]

    def __call__(self, request):
        return self.get_response(request)

    def process_template_response(self, request, response):
        response.context_data['config'] = self.instance
        return response
