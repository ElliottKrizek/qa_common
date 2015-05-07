from random import randint
import platform, os

REPORT_DIR = os.getcwd() + "/reports/"
SCREENSHOT_DIR = os.getcwd() + "/reports/screenshots/"
CHROME_DRIVER_DIR = "/Users/Briel/qa/common/chromedriver"
IE_DRIVER_DIR = "/Users/Briel/qa/common/IEDriverServer.exe"


EMAILPASS = os.environ['FP_QA_EMAIL_PASS']

CHROME = 'chrome'
FF = 'firefox'
SAFARI = 'safari'
IE = 'ie11'
IPHONE = 'iphone'
IPAD = 'ipad'
HEADLESS = 'headless'
SAUCE = 'sauce'
SAUCE_CHROME = 'sauce_chrome'
SAUCE_FIREFOX = 'sauce_firefox'
SAUCE_IE8 = 'sauce_ie8'
SAUCE_IE9 = 'sauce_ie9'
SAUCE_IE10 = 'sauce_ie10'
SAUCE_IE11 = 'sauce_ie11'
SAUCE_IPHONE = 'sauce_iphone'
SAUCE_IPAD = 'sauce_ipad'
BROWSER_LIST = [CHROME, FF, SAFARI, IE, IPHONE, IPAD, SAUCE_CHROME,
                SAUCE_FIREFOX, SAUCE_IE11, SAUCE_IPHONE, SAUCE_IPAD]
BROWSER_HELP = '''Browser to run tests on.  All options are listed in basetestcase.py,
and include one of the following (no quotes): ''' + str(BROWSER_LIST)


PUBLISH_HELP = "Optional True or False argument to publish results to a junitxml file (defaults to False)."

#WEBDRIVER
ID="ID"
LT="LINK_TEXT"
PLT="PARTIAL_LINK_TEXT"
NAME="NAME"
TAG="TAG_NAME"
CN="CLASS_NAME"
CSS="CSS_SELECTOR"
XPATH="XPATH"

TIMEOUT= 20
TIMEOUTSHORT= 10
TIMEOUTSHORTEST = 5
TIMEOUTLONG= 50
TIMEOUT_RETRY_INTERVAL= 0.1
TRANSFORM_TRANSITION_TIME= 1
LONG_TRANSITION_TIME = 2

FAILURE_MSG = "FAILED - The following verifications failed:\n"
