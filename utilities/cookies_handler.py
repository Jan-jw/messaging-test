import json

class CookiesHandler:
    @staticmethod
    def read_cookies(cookies):
        with open("./Configurations/config.json", 'r') as f:
            json_data = json.load(f)
        json_data['cookies'] = []
        with open("./Configurations/config.json", 'w') as f:
            json.dump(json_data, f)
            for ck in cookies:
                ck = {
                    "name": ck["name"],
                    "value": ck["value"],
                    "domain": ck["domain"],
                    "path": ck["path"],
                    "secure": ck["secure"],
                }
                json_data["cookies"].append(
                    ck)  # file data append cookies in the middle of cookies key but the json keys above are still connect together
            f.seek(0)
            json.dump(json_data, f, indent=4)
            f.close()

    @staticmethod
    def write_cookies(driver):
        with open("./Configurations/config.json", "r") as file:
            json_data = json.load(file)
            for ck in json_data["cookies"]:
                driver.add_cookie(ck)