def error_response(code, message, data):
    """
    Error response API for 
    """
    return {"code": code, "message": message, "data": data}

def success_response(data):
    """
    Success response API for 
    """
    return {"code": 200, "data": data}
