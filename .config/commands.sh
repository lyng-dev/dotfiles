# make directory and nagivate to it
mkcd() { mkdir -p "$1" && cd "$1"; }

# show my ip, and a bit more info
myip() { curl -qs https://ifconfig.co/json | jq -r '.ip,.city,.country,.hostname,.asn_org' }
