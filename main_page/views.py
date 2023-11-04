# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class Main(APIView):
    def get(self, request):
        name = request.query_params['name']
        return Response({'name':name})

    def post(self, request):
        name = request.data['name']
        return Response({"name":name})







def header_component(request):

    return  render(request, 'components/header_component.html')


def footer_component(request):
    return render(request, 'components/footer_component.html')