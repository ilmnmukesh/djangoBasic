
# from django.http.request import HttpRequest
# from django.http.response import JsonResponse


# def index(request: HttpRequest):
#     if request.method == "POST":
#         return JsonResponse({"name": "mukehs", "password": "1234"})
#     return JsonResponse({})

from rest_framework.decorators import api_view
from rest_framework.response import Response


class ApiResponse(object):
    def __init__(self, success: bool = False, data: dict = {}, description: str = "", errors: dict = {}) -> None:
        self.success: bool = success
        self.data: dict = data
        self.description: str = description
        self.errors: dict = errors

    # @property
    # def dict(self):
    #     return vars(self)


def decorator(func):
    def innerFunction(req):
        resp = ApiResponse()
        try:
            func(req, resp)
        except Exception as e:
            resp.errors = dict(e)
            resp.description = "Something went Wrong"

        return Response(resp.__dict__)
    return innerFunction


@api_view(["POST"])
@decorator
def index(_, resp: ApiResponse):
    resp.data = {"name": "mukehs", "password": "1234"}
    resp.success = True
