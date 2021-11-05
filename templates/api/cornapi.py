import random

from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')

corns = []
corns_list = [
    "https://www.amazon.com/Bi-color-White-Corn-Tray-Pack/dp/B00E3JAP5Y/ref=sr_1_3_0o_fs?keywords=corn&qid=1636067902&qsid=138-7077979-0009264&sr=8-3&sres=B074J6RKQJ%2CB00E3JAP5Y%2CB000RPXSNY%2CB07WSBWHMS%2CB07V7K8WX6%2CB074H6YNGS%2CB000V9YYAW%2CB074H7KL69%2CB00099XPOU%2CB000RA9R7K%2CB074H81LWW%2CB0147RUUXS%2CB000REQBZW%2CB00CIJR5VS%2CB06XDL5FW1%2CB000VA49CY%2CB0044R36OW%2CB07K8RN9D7%2CB001ET703G%2CB01NCPW3FX&srpt=VEGETABLE"
    "https://www.walmart.com/ip/Fresh-Corn-on-the-Cob/44391430",
    "https://shop.sprouts.com/search?search_term=corn",
    "https://www.target.com/p/sweet-corn-4pk-package/-/A-14919033#lnk=sametab",
    "https://www.ralphs.com/p/corn-on-the-cob/0000000004590?fulfillment=PICKUP",
    "https://www.costco.com/del-monte-whole-kernel-corn%2c-15.25-oz%2c-12-count.product.100443694.html",
]

def _find_next_id():
    return max(corns["id"] for corn in corns) + 1


def _init_corns():
    id = 1
    for corn in corns_list:
        corns.append({"id": id, "corn": corn, "haha": 0, "boohoo": 0})
        id += 1

@api_bp.route('/corn')
def get_corn():
    if len(corn) == 0:
        _init_corns()
    return jsonify(random.choice(corns))

@api_bp.route('/corns')
def get_corns():
    if len(corns) == 0:
        _init_corns()
    return jsonify(corns)


if __name__ == "__main__":
    print(random.choice(corns_list))