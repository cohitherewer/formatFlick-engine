from formatflick import formatflick
from formatflick.engine import Logger_Config
from formatflick.engine.handler import source
if __name__ == "__main__":
    # testing main format flick
    obj = formatflick.Formatflick("abhinaba")
    print(obj.destination)
    # testing logger
    obj = Logger_Config.logger
    obj.error("An error occured", exc_info=False)

    # testing source isExits
    obj = source.Sourcefile_handler("main.py")
    # obj.is_exists()