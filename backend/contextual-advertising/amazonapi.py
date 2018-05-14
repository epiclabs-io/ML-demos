import bottlenose
import json
import time
from urllib.error import HTTPError
import xmltodict


config = json.load(open('./config.json'))
AWS_ACCESS_KEY_ID = config['access_key']
AWS_SECRET_ACCESS_KEY = config['secret_api_key']
AWS_ASSOCIATE_TAG = config['associate_tag']


def create_amazon_instance():
    return bottlenose.Amazon(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ASSOCIATE_TAG, ErrorHandler=error_handler)


def browse_node(node_id):
    tmp = amazon.BrowseNodeLookup(BrowseNodeId=node_id, ResponseGroup="TopSellers")
    return xmltodict.parse(tmp.decode())


def node_exists(response):
    try:
        code = response["BrowseNodeLookupResponse"]["BrowseNodes"]["Request"]["Errors"]["Error"]["Code"]
        if code:
            return False
        else:
            return True
    except KeyError:
        return True


def item_lookup(item_id):
    tmp = amazon.ItemLookup(ItemId=item_id, ResponseGroup="ItemAttributes, Images, OfferSummary")
    return xmltodict.parse(tmp.decode())


def error_handler(err):
    ex = err['exception']
    if isinstance(ex, HTTPError) and ex.code == 503:
        print("Amazon API returned error, retrying...")
        time.sleep(0.01)
        return True


def get_top_seller_id(response):
    try:
        return response["BrowseNodeLookupResponse"]["BrowseNodes"]["BrowseNode"]["TopSellers"]["TopSeller"][0]["ASIN"]
    except KeyError:
        return 0


def get_url_image_price(response, directSearch=False):
    try:
        if directSearch:
            response = response["ItemSearchResponse"]["Items"]["Item"][0]
        else:
            response = response["ItemLookupResponse"]["Items"]["Item"]
    except KeyError:
        return 0, 0, 0
    try:
        url = response["DetailPageURL"]
    except KeyError:
        url = 0
    try:
        image = response["MediumImage"]["URL"]
    except KeyError:
        image = 0
    try:
        price = response["ItemAttributes"]["ListPrice"]["FormattedPrice"]
    except KeyError:
        price = 0
    return url, image, price


def get_direct_item(tag):
    tmp = amazon.ItemSearch(Keywords=tag, SearchIndex="All", ResponseGroup="ItemAttributes, Images, OfferSummary")
    return xmltodict.parse((tmp.decode()))


amazon = create_amazon_instance()
