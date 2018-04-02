from user_agents import parse

def parse_user_agent(data):
    data['browser']= []
    data['os'] = []
    try:
        for ua_string in data['ua_string']:
            user_agent = parse(ua_string)
            browser = user_agent.browser.family
            os = user_agent.os.family
            data['browser'].append(browser)
            data['os'].append(os)
    except:
        print ('here')
        data['browser'].append(None)
        data['os'].append(None)
    return data
