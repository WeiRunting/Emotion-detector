import requests # 导入请求库以处理 HTTP 请求
import json

def sentiment_analyzer(text_to_analyse): # 定义一个名为 sentiment_analyzer 的函数，接受一个字符串输入 (text_to_analyse) 
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict' # 情感分析服务的 URL
    myobj = { "raw_document": { "text": text_to_analyse } } # 创建一个字典，包含要分析的文本
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"} # 设置 API 请求所需的头部
    response = requests.post(url, json = myobj, headers=header) # 向 API 发送 POST 请求，包含文本和头部
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None
    else:
        label = None
        score = None
    return {'label': label, 'score': score}

