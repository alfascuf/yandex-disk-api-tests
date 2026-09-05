import requests


class YandexDiskClient:
    BASE_URL = "https://cloud-api.yandex.net/v1/disk"
    TIMEOUT = (20, 30)

    def __init__(self, token: str):
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"OAuth {token}"
        })

    def get_resource(self, path: str):
        return self.session.get(
            f"{self.BASE_URL}/resources",
            params={"path": path},
            timeout=self.TIMEOUT,
        )

    def create_folder(self, path: str):
        return self.session.put(
            f"{self.BASE_URL}/resources",
            params={"path": path},
            timeout=self.TIMEOUT,
        )

    def copy_resource(self, source: str, destination: str):
        return self.session.post(
            f"{self.BASE_URL}/resources/copy",
            params={
                "from": source,
                "path": destination,
            },
            timeout=self.TIMEOUT,
        )

    def delete_resource(self, path: str, permanently: bool = True):
        return self.session.delete(
            f"{self.BASE_URL}/resources",
            params={
                "path": path,
                "permanently": str(permanently).lower(),
            },
            timeout=self.TIMEOUT,
        )