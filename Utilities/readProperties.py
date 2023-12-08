import configparser


config = configparser.RawConfigParser()
config.read("/Users/Raghu/qa_formy_app_pytest_sele_html/Configurations/config.ini")
print(config.sections())


class ReadConfig:

   @staticmethod
   def getApplicationURL():
        url =  config.get('common.info', 'baseURL')
        return url
