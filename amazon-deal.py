from amazon.api import AmazonAPI
import sys, re, math

AMAZON_ACCESS_KEY = "XXXXXXXXXXXXXXXXXXXX"
AMAZON_SECRET_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
AMAZON_ASSOC_TAG = "haguremetaru-20"

#	Example Inputs
# ASIN = 'B000MFF89G'
# url = 'http://www.amazon.com/dp/B000MFF89G/ref=gb1h_tit_c-2_0842_f4bc7aa6?smid=ATVPDKIKX0DER&pf_rd_m=ATVPDKIKX0DER&pf_rd_t=701&pf_rd_s=center-new-2&pf_rd_r=1Z20MF39VQZ8ACJPZSYT&pf_rd_i=20&pf_rd_p=2072380842'

# --- - --- - --- - --- - --- - --- - --- - ---

def get_amazon_item_id(url):

	asin_pattern = r'/([A-Z0-9]{10})'

	match = re.search(asin_pattern, url)

	if match:
		ASIN = match.group(1)
	return ASIN

# --- - --- - --- - --- - --- - --- - --- - ---

#	Get Input from command line. Argument 0 is always the calling function
url = sys.argv[1]

ASIN = get_amazon_item_id(url)
amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)
product = amazon.lookup(ItemId=ASIN)

dealtweet = "#DEAL " + product.title + " $" + str(int(math.ceil(product.price_and_currency[0]))) + " @amazon\n\n\n" + product.large_image_url + "\n" + product.offer_url