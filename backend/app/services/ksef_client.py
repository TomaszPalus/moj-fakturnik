def test_connection(
    token: str
):
    if not token:
        return {
            "success": False,
            "message": "Missing token"
        }

    return {
        "success": True,
        "message": "Mock KSeF connection successful"
    }