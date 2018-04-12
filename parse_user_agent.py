from user_agents import parse

def parse_user_agent(data):
    data['browser']= []
    data['os'] = []
    print ('Starting to convert user agent strings to os, browser')
    try:
        for ua_string in data['ua_string']:
            user_agent = parse(ua_string)
            browser = user_agent.browser.family
            os = user_agent.os.family
            data['browser'].append(browser)
            data['os'].append(os)
    except:
        print ('Error converting browser and os')
        data['browser'].append(None)
        data['os'].append(None)
    print ('Finished convert user agent strings to os and browser')
    return data
