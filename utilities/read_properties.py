import json

with open('./Configurations/config.json', 'r') as config_file:
    config = json.load(config_file)

class ReadConfig:
    # can access the method without creating class Object
    @staticmethod
    def get_applicationURL():
        url=config["login"]["baseURL"]
        return url

    @staticmethod
    def get_loginURL():
        log_url = config["login"]["loginURL"]
        return log_url

    @staticmethod
    def get_username():
        userEmail = config["login"]["username"]
        return userEmail

    @staticmethod
    def get_password():
        password = config["login"]["password"]
        return password

    # @staticmethod
    # def get_sender():
    #     sender = config["testData"]["password"]
    #     return password

