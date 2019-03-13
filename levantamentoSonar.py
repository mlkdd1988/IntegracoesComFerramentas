#pip install requests
import requests

def getUrlSonarAPI():
    return 'https://sonarcloud.io/api'

def getToken():
    #substituir por token de usuário com permissão de apenas leitura
    return 'ae939677f51aade6b2f9d8623c0a54c5a14a3c67'

def getUrlProjectKeys():
     return getUrlSonarAPI()+'/components/search?qualifiers=TRK'

def getUrlMetricKey(projectKey,metricKey):
    return getUrlSonarAPI()+'/measures/component?metricKeys='+metricKey+'&component='+projectKey

def requestGet(url):
    head = {'Authorization': 'token {}'.format(getToken())}
    response = requests.get(url, headers=head)
    data = response.json()
    return data

def getProjectKeys():
    projectKeys = []
    data = requestGet(getUrlProjectKeys())
    for component in data['components']:
        projectKeys.append(component['key'])
    return projectKeys


def getMetric(projectKey,metricKey):
    data = requestGet(getUrlMetricKey(projectKey,metricKey))
    for measure in data['component']['measures']:
        return measure['value']

def printMetric(metricKey):
    projectKeys = getProjectKeys()
    for projectKey in projectKeys:
        metric = getMetric(projectKey,metricKey)
        print (projectKey,metric)

#main
printMetric('ncloc')
