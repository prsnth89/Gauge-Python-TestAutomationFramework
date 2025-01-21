import os
from getgauge.python import before_spec, after_spec, before_scenario, after_scenario, after_step 
from framework.actions.web.playwright_actions import PlayWrightActions
from framework.actions.web.selenium_actions import SeleniumActions
from framework.actions.mobile.mobile_actions import MobileActions
from getgauge.python import data_store as data
from framework.interface.iweb import IWeb


execute = os.getenv('execute')
browserName = os.getenv('browserName')
headless = os.getenv('headless')
tool_type=os.getenv('toolType')
url=os.getenv('webBaseURL')
os.environ["GAUGE_LOG_LEVEL"] = "ERROR"


class Hooks:
 
    iWeb=None
    @before_scenario
    def before_scenario_execution(self):
        if execute.lower()=='ui' or execute.lower()=='both':
            if tool_type=='selenium':
                iWeb=SeleniumActions()
                iWeb.open_selenium_browser(browserName)
            elif tool_type=='playwright':
                iWeb=PlayWrightActions()
                iWeb.open_playwright_browser()
            data.scenario.iweb=iWeb 
            iWeb.navigate(url)
            data.spec.url=url
        elif execute.lower()=='api':
            pass
        elif execute.lower()=='mobile':
            iWeb=MobileActions()
            iWeb.open_mob_selenium_browser(browserName)
            data.scenario.iweb=iWeb 
            iWeb.navigate(url)
            data.spec.url=url
       

    @after_step
    def after_step(context):
        #path = "\html-report\demo\features\specs"
        if execute.lower()=='ui' or execute.lower()=='both' or execute.lower()=='mobile':
            print("Step Name is - ", context._ExecutionContext__step.text)
            print("Failing status is - ", context._ExecutionContext__step._Step__is_failing)
        elif execute.lower()=='api':
            pass
       

    @after_scenario
    def quit_browser(context):
        if execute.lower()=='ui' or execute.lower()=='both':
            print("Scenario Name is - ", context._ExecutionContext__scenario.name)
            print("Tag Name is - ", context._ExecutionContext__scenario.tags)
            print("Failing status is - ", context._ExecutionContext__scenario.is_failing)
            if tool_type=='selenium':
                iWeb=data.scenario.iweb
                iWeb.quit_selenium_browser()        
            elif tool_type=='playwright':
                iWeb: PlayWrightActions
                iWeb=data.scenario.iweb
                iWeb.quit_playwright_browser()
        elif execute.lower()=='mobile':
            iWeb=data.scenario.iweb
            iWeb.quit_mob_selenium_browser()
        elif execute.lower()=='api':
            pass


