"""
This module validates token
"""

import requests

AUTHENTICATION_URL="http://40.76.37.214:3000/api/authenticate"

def validate_token(token):

    # okay, to validate this token, we send a post request to /api/authenticate

    response = requests.post(
        url = AUTHENTICATION_URL,
        data = {
            "token":token
        } 
    )
    # after the request, we check the response code.
    if response.status_code == 200:
        return True

    else:
        print(response.status_code)
        return False



if __name__ == "__main__":
    print(validate_token("eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJyb2xlIjoiZGV2aWNlIiwiaWF0IjoxNjAwNTQyODEzLCJleHAiOjE2MDA2MjkyMTMsImlzcyI6IlNpZ21vaWQgQXV0aGVudGljYXRpb24gU2VydmljZSJ9.cJaPAVAFN_4UHhxKxeyaDKupVtK-3y3yEY5UR6qRP_FsEfoSIUJ9cREOxLmjMVXA13dRMrn6_bK8tMsUN_QLq6sdl8mpvkQktjt9aF-OtUBuCnGDaxPRC9SSCLpF_oUD5LiQgSEuywCbGnFqRpa_HOX-U84eHxf_Pt3Q9hMkP2c5-tngnCee4WKP2u_gtOa_TvsjeB4TWtvmedLvWrGuex_icZ-CS6mPhMeszXBjj-MJ5LdaKgEx6ff5pUtDbgWEs3QClPUu1BH291wlFpNy6xAG5J85hafrUW6toaf2hsEB4d9N7g2BuYc6nY0yTFyT4lKu_zyYznDnpPDn3kWqyypemwhP4F9LSJvLxGnNCQ8EBfqMdqroQuhe_9A4l3DH5IvUmwZMTjIUjjAxwouXgy18iNPU2ygmsKXiI4E4mcVV6BW3THznO1SSE7noSzieiVHXwSbCrRDd4ogw6RjyglN-O_0-hYNfEi16LFPnxUS6MnD0LzdYuRRP9ql4DhXxQVfDi5eEIlUP_o6kd5gE2qeEPA7uFBjD6zSjYzA2NAJBz6Vw-vv8_CoJl7zHFnh0uB7Oto7CPLnOdiGGiUORZXNGs_CBbLqrDWw6iVmiOtFsElI4SUBYEMYaEUw50bNeqZ8YdCwlYSkBCcI2VsmNNzFBycNt1lbNAjMktxxYl_8"))
