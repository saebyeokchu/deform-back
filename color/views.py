from django.http import JsonResponse
from color.logic.FindColor import FindColor
from django.views.decorators.csrf import csrf_exempt
import json

def getClosestColor(request):
    r = int(request.GET.get("r"))
    g = int(request.GET.get("g"))
    b = int(request.GET.get("b"))
    print(r, g, b)
    getColorResult = FindColor.getColor(r,g,b)
    print(getColorResult)
    return JsonResponse(getColorResult, safe=False)

@csrf_exempt
def getColors(request) :
    # print("Raw request body:", request.body.decode("utf-8"))
    data = json.loads(request.body)
    clampedAry  = data.get('rgb',[])

    if clampedAry is None:
        return JsonResponse({"error": "Invalid Uint8ClampedArray data"}, status=400)
    
    colors = FindColor.runDetection(clampedAry)
    # return JsonResponse(detectionResult, safe=False)
    return JsonResponse(colors, safe=False)

