# deal-tweet
Script that takes an Amazon product URL &amp; uses it to parse product information from the AmazonAPI. The Product Title, Price, Affiliate Link &amp; Product Image Link are outputted in a format used to post deals on twitter


# USAGE:

##  Output 'Deal-Tweet'

```
$> python /path/to/script/amazon-deal.py http://www.amazon.com/Ultimate-Marvel-Vs-Capcom-Xbox-360/dp/B005C7R8I8/ref=sr_1_1_twi_2_gam?tag=haguremetaru-20

$> #DEAL Ultimate Marvel Vs. Capcom 3 - Xbox 360 $37.96 @amazon

http://www.amazon.com/dp/B005C7R8I8/?tag=haguremetaru-20
http://ecx.images-amazon.com/images/I/51IatU5xMjL.jpg
$> 
```

##  Output Image Link Only

```
$> python /path/to/script/amazon-image.py http://www.amazon.com/Ultimate-Marvel-Vs-Capcom-Xbox-360/dp/B005C7R8I8/ref=sr_1_1_twi_2_gam?tag=haguremetaru-20
$> http://ecx.images-amazon.com/images/I/51IatU5xMjL.jpg
$> 
```

# SETUP:

Edit the scripts to enter your respective keys at Affiliate Tags in the variables at the top of the `amazon-deal.py` or amazon-image.py scripts. The shell script is a simple Bash script used to execute the script on a remote server.

# FORMAT:
```
#DEAL Ultimate Marvel Vs. Capcom 3 - Xbox 360 $37.96 @amazon

http://www.amazon.com/dp/B005C7R8I8/?tag=haguremetaru-20
http://ecx.images-amazon.com/images/I/51IatU5xMjL.jpg
```
