
import requests




def check_url(my_url: str) -> dict:
    response = requests.get(my_url, timeout=5)
    print(response)
    return {
        "url": my_url,
        "status_code": response.status_code
    }
    




if __name__ == "__main__":
    print("Check url method:")
    my_dict=check_url("https://example.com")
    print(my_dict)